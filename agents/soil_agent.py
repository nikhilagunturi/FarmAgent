"""
agents/soil_agent.py
Specialist agent analyzing soil physical properties, texture, estimated pH, moisture retention,
and nutrient dynamics (NPK).
Explicitly identifies when laboratory soil testing is required before applying chemical amendments.
"""

from typing import Dict, Any, List
from utils.helpers import FarmContext, AgentResponse
from data.mock_data import SOIL_PROFILES, CROP_PROFILES

class SoilAgent:
    def __init__(self):
        self.name = "Soil Agent"
        self.role = "Pedology & Soil Nutrition Specialist"

    def analyze(self, ctx: FarmContext) -> AgentResponse:
        soil_type_lower = ctx.soil_type.strip().lower()
        matched_soil_type = "loam"
        soil_meta = SOIL_PROFILES["loam"]

        for st, meta in SOIL_PROFILES.items():
            if st in soil_type_lower:
                matched_soil_type = st
                soil_meta = meta
                break

        crop_lower = ctx.crop.strip().lower()
        crop_meta = CROP_PROFILES.get(crop_lower, {"optimal_ph": (6.0, 7.0)})
        opt_ph_min, opt_ph_max = crop_meta.get("optimal_ph", (6.0, 7.0))

        key_findings = [
            f"Soil Texture: {ctx.soil_type} (Characteristic: {soil_meta['drainage']} drainage, {soil_meta['water_retention']} water retention).",
            f"Crop Optimal pH range: {opt_ph_min} - {opt_ph_max}.",
            f"Agronomic note: {soil_meta['note']}"
        ]

        supporting_evidence = []
        possible_causes = []
        uncertain_info = []
        challenges_raised = []
        recommendation = ""
        confidence = "Medium"
        urgency = "Normal"

        moisture = ctx.soil_moisture
        symptoms_lower = ctx.symptoms.lower()
        additional_lower = ctx.additional_info.lower()

        # Physical and chemical evaluation
        if moisture is not None:
            ideal_min, ideal_max = soil_meta.get("ideal_moisture_range", (20, 35))
            if moisture > ideal_max + 10:
                supporting_evidence.append(f"Soil moisture at {moisture}% severely exceeds field capacity ({ideal_max}%).")
                supporting_evidence.append("Pores are water-filled, suffocating aerobic root respiration and preventing mineral uptake.")
                challenges_raised.append("Waterlogged soil induces anaerobic conditions, leading to denitrification and toxic sulfide accumulation.")
            elif moisture < ideal_min:
                supporting_evidence.append(f"Soil moisture at {moisture}% is near or below wilting point for {matched_soil_type} soil.")
                supporting_evidence.append("Nutrient diffusion in dry soil drops dramatically; roots cannot extract dissolved minerals.")

        # Nutrient deficiency reasoning
        if "yellow" in symptoms_lower or "chlorosis" in symptoms_lower or "npk" in additional_lower or "fertilizer" in additional_lower:
            if "old" in symptoms_lower or "lower" in symptoms_lower or "v-shaped" in symptoms_lower or "midrib" in symptoms_lower:
                supporting_evidence.append("Symptom geography (older basal leaves yellowing first) strongly correlates with Nitrogen (N) mobility.")
                if "rain" in additional_lower or (ctx.recent_rainfall and ctx.recent_rainfall > 20):
                    supporting_evidence.append("Recent significant rainfall likely caused downward nitrate leaching through the root profile.")
                recommendation = "Suspected Nitrogen deficiency due to leaching. Consider side-dressing slow-release nitrogen or compost after verifying soil saturation."
            elif "leaf tip" in symptoms_lower or "scorch" in symptoms_lower:
                supporting_evidence.append("Leaf margin browning points to Potassium (K) deficiency or salinity accumulation.")
                recommendation = "Test soil electrical conductivity (EC) and potassium balance."
            else:
                recommendation = "General chlorosis detected. Perform comprehensive N-P-K soil and leaf tissue test."

            uncertain_info.append("Precise active soil N-P-K (ppm) and cation exchange capacity (CEC) are unmeasured.")
            uncertain_info.append("Soil pH is unverified; an extreme pH (<5.5 or >7.8) locks out nutrients even if present in soil.")
            confidence = "Medium"

        elif "rot" in symptoms_lower or "stagnant" in symptoms_lower or (moisture and moisture > 45):
            recommendation = "Drainage remediation required immediately. Aerate soil beds and avoid mechanical compaction."
            supporting_evidence.append("Poor soil aeration and persistent water ponding promote anaerobic root rot pathogen buildup.")
            urgency = "High"

        else:
            recommendation = f"Maintain organic matter to support {matched_soil_type} soil microbial health and structural aggregation."
            supporting_evidence.append("No acute physical soil breakdown reported.")

        # Mandatory caveat: Laboratory soil testing preference
        uncertain_info.append("Field visual inspection cannot substitute for a calibrated laboratory soil test.")
        recommendation += " (Laboratory soil testing is strongly recommended before adjusting fertilizer or lime applications)."

        return AgentResponse(
            agent_name=self.name,
            role=self.role,
            recommendation=recommendation,
            confidence=confidence,
            key_findings=key_findings,
            supporting_evidence=supporting_evidence,
            possible_causes=possible_causes,
            uncertain_info=uncertain_info,
            challenges_raised=challenges_raised,
            urgency=urgency
        )
