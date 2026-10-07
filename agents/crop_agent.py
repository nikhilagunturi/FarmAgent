"""
agents/crop_agent.py
Specialist agent responsible for analyzing crop health, symptoms, potential pathogens,
growth stage vulnerability, and pest risks.
Crucially distinguishes between Likely Causes, Possible Causes, and Uncertain Information.
Never diagnoses with false certainty when laboratory or close physical inspection is needed.
"""

from typing import List, Dict, Any
from utils.helpers import FarmContext, AgentResponse
from data.mock_data import CROP_PROFILES

class CropAgent:
    def __init__(self):
        self.name = "Crop Agent"
        self.role = "Crop Health & Pathology Specialist"

    def analyze(self, ctx: FarmContext) -> AgentResponse:
        crop_clean = ctx.crop.strip().lower()
        crop_info = CROP_PROFILES.get(crop_clean, {
            "optimal_ph": (6.0, 7.0),
            "water_need": "medium",
            "soil_pref": ["loam"],
            "temp_range": (18, 30),
            "critical_stages": ["flowering"],
            "common_issues": ["fungal leaf spot", "nutrient deficiency", "pest infestation"]
        })

        symptoms_lower = ctx.symptoms.lower()
        growth_lower = ctx.growth_stage.lower()

        key_findings = []
        supporting_evidence = []
        likely_cause = None
        possible_causes = []
        uncertain_info = []
        recommendation = ""
        confidence = "Medium"
        urgency = "Normal"

        # Growth stage vulnerability assessment
        critical_match = any(stage in growth_lower for stage in crop_info.get("critical_stages", []))
        if critical_match:
            key_findings.append(f"Crop is currently in a high-sensitivity stage ({ctx.growth_stage}). Any severe stress can heavily affect yield.")
            urgency = "High"
        else:
            key_findings.append(f"Growth stage noted as {ctx.growth_stage}.")

        # Diagnostic symptom reasoning
        if "wilt" in symptoms_lower or "droop" in symptoms_lower:
            # Wilting can be drought, thermal stress, or vascular disease (bacterial / fusarium / pythium)
            if ctx.soil_moisture is not None and ctx.soil_moisture < 20.0:
                likely_cause = "Transpiration stress & drought-induced temporary wilting"
                possible_causes.append("Root damage preventing water uptake")
                possible_causes.append("Early vascular wilt pathogen (Fusarium/Verticillium)")
                supporting_evidence.append(f"Soil moisture is critically low at {ctx.soil_moisture}%.")
                supporting_evidence.append("Midday curling is characteristic of water conservation mechanism.")
                recommendation = "Rehydrate root zone promptly, but verify recovery during cooler evening hours."
                confidence = "High"
            elif ctx.soil_moisture is not None and ctx.soil_moisture > 45.0:
                likely_cause = "Root suffocation / Anoxic stress / Waterlogged root rot (Pythium/Phytophthora)"
                possible_causes.append("Bacterial wilt (Ralstonia)")
                possible_causes.append("Soil compaction impedes drainage")
                supporting_evidence.append(f"Excessive soil moisture ({ctx.soil_moisture}%) despite plant wilting indicates roots cannot breathe or absorb water.")
                supporting_evidence.append("Darkening near lower stem/soil line confirms moisture-related root compromise.")
                recommendation = "Halt all irrigation immediately. Improve drainage and aerate soil; inspect roots for browning or sloughing."
                confidence = "High"
                urgency = "Critical"
            else:
                likely_cause = "Indeterminate Wilting: moisture or pathogen-induced"
                possible_causes.append("Water stress / insufficient root depth")
                possible_causes.append("Bacterial wilt or fungal root infection")
                possible_causes.append("High vapor pressure deficit (excessive heat)")
                uncertain_info.append("Root zone condition and vascular tissue color (internal stem discoloration) unknown.")
                uncertain_info.append("Cannot definitively separate drought wilting from vascular pathogen without stem cross-section or moisture reading.")
                recommendation = "Conduct stem cross-section test for vascular browning; check root health before applying large amounts of water."
                confidence = "Medium"

        elif "yellow" in symptoms_lower or "chlorosis" in symptoms_lower:
            # Chlorosis diagnosis
            if "old" in symptoms_lower or "lower" in symptoms_lower or "tip" in symptoms_lower or "v-shaped" in symptoms_lower:
                likely_cause = "Mobile nutrient deficiency (likely Nitrogen [N] or Magnesium [Mg])"
                possible_causes.append("Over-saturation causing root nitrogen leaching")
                possible_causes.append("Soil compaction restricting root exploration")
                supporting_evidence.append("Symptom expression starts strictly at older, lower foliage and travels along midrib, characteristic of mobile nitrogen mobilization.")
                uncertain_info.append("Exact soil NPK levels and soil pH are not verified through laboratory analysis.")
                recommendation = "Consider targeted nitrogen side-dress or foliar feed after confirming soil moisture and root health."
                confidence = "Medium"
            elif "young" in symptoms_lower or "upper" in symptoms_lower or "interveinal" in symptoms_lower:
                likely_cause = "Immobile micronutrient deficiency (Iron [Fe], Zinc [Zn], or Sulfur [S])"
                possible_causes.append("High soil pH inducing nutrient tie-up / lockout")
                uncertain_info.append("Trace element levels and soil pH not yet confirmed by lab test.")
                recommendation = "Verify soil pH to rule out nutrient lockout before applying micronutrient chelates."
                confidence = "Medium"
            else:
                likely_cause = "General Chlorosis (Nutrient depletion or root stress)"
                possible_causes.extend(["Nitrogen deficiency", "Root damage", "Suboptimal pH"])
                uncertain_info.append("Leaf pattern (veinal vs interveinal; upper vs lower canopy) is unclarified.")
                recommendation = "Examine whether yellowing is on old or new leaves to narrow down mobile vs immobile nutrient deficiency."
                confidence = "Low"

        elif "spot" in symptoms_lower or "blight" in symptoms_lower or "lesion" in symptoms_lower:
            # Fungal / bacterial leaf spot
            if "white" in symptoms_lower or "fuzzy" in symptoms_lower or "fast" in symptoms_lower or "spreading" in symptoms_lower:
                likely_cause = "Active fungal foliar infection (Suspected Late Blight or Downy Mildew)"
                possible_causes.append("Early Blight (Alternaria solani)")
                possible_causes.append("Bacterial leaf spot (Xanthomonas)")
                supporting_evidence.append("Presence of white fungal mycelium/sporulation under humid conditions points toward aggressive oomycete/fungal pathogen.")
                uncertain_info.append("Microscopic spore confirmation or lab pathology assay needed for 100% species identification.")
                uncertain_info.append("Field weather history (leaf wetness duration) is needed to calculate disease pressure index.")
                recommendation = "Isolate infected plants/rows immediately. Avoid overhead watering to prevent splashing spores; consult agronomist for targeted fungicide if confirmed."
                confidence = "Medium"
                urgency = "High"
            else:
                likely_cause = "Foliar Leaf Spot complex"
                possible_causes.extend(["Early Blight (Alternaria)", "Septoria leaf spot", "Bacterial speck"])
                uncertain_info.append("Lesion concentric rings and margin water-soaking details are absent.")
                recommendation = "Collect leaf samples in sealed bag for local extension diagnosis; maintain leaf canopy dryness."
                confidence = "Low"

        elif "pest" in symptoms_lower or "bug" in symptoms_lower or "hole" in symptoms_lower:
            likely_cause = "Foliar herbivore or insect pest damage"
            possible_causes.extend(["Chewing larvae / caterpillars", "Sucking insects (aphids, thrips)"])
            uncertain_info.append("Specific insect sightings, frass, or underside egg masses not detailed.")
            recommendation = "Inspect leaf undersides with hand lens; avoid prophylactic broad-spectrum insecticide without knowing pest identity."
            confidence = "Medium"

        else:
            likely_cause = "Sub-clinical plant stress or early-stage physiological disorder"
            possible_causes.extend(["Environmental fluctuation (temperature/humidity)", "Minor nutrient imbalance", "Soil pH mismatch"])
            uncertain_info.append("Visual symptom descriptions are minimal or non-specific.")
            recommendation = "Monitor crop closely for 48 hours and log symptom progression across top vs bottom foliage."
            confidence = "Low"

        # Explicit safety constraint: never pretend 100% diagnosis
        uncertain_info.append("Field visual diagnosis is preliminary; confirmation requires laboratory tissue assay or local extension visit.")

        return AgentResponse(
            agent_name=self.name,
            role=self.role,
            recommendation=recommendation,
            confidence=confidence,
            key_findings=key_findings,
            supporting_evidence=supporting_evidence,
            likely_cause=likely_cause,
            possible_causes=possible_causes,
            uncertain_info=uncertain_info,
            urgency=urgency
        )
