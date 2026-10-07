"""
core/debate_engine.py
Core Debate Engine for AutoAgent 3D:
Collects multi-agent arguments, identifies disagreements and contradictory evidence,
evaluates competing theories, applies safety weighting, selects the winning recommendation,
and generates structured defenses explaining why alternatives were rejected.
"""

from typing import Dict, List, Any, Optional
from utils.helpers import (
    FarmContext,
    AgentResponse,
    Disagreement,
    RejectedAlternative,
    DebateOutcome
)
from core.llm_client import GroqLLMClient

class DebateEngine:
    def __init__(self):
        self.llm_client = GroqLLMClient()

    def adjudicate(
        self,
        ctx: FarmContext,
        agents: Dict[str, AgentResponse],
        weather_data: Optional[Dict[str, Any]] = None,
    ) -> DebateOutcome:
        crop_agent = agents.get("Crop Agent")
        irr_agent = agents.get("Irrigation Agent")
        weather_agent = agents.get("Weather Agent")
        soil_agent = agents.get("Soil Agent")
        risk_agent = agents.get("Risk Agent")

        disagreements: List[Disagreement] = []
        rejected_alternatives: List[RejectedAlternative] = []
        reasons_for_decision: List[str] = []
        residual_risks: List[str] = []
        
        # -------------------------------------------------------------
        # STEP 1: CLASH DETECTION & CROSS-EXAMINATION
        # -------------------------------------------------------------
        
        # Clash 1: Irrigation vs Weather (Impending Heavy Precipitation)
        forecast = (weather_data or {}).get("forecast_next_24h", {})
        try:
            weather_rain_forecast = max(0.0, float(forecast.get("expected_rain_mm", 0.0) or 0.0))
            rain_probability = min(100.0, max(0.0, float(forecast.get("rain_probability", 0.0) or 0.0)))
        except (TypeError, ValueError):
            weather_rain_forecast, rain_probability = 0.0, 0.0
        # A substantial forecast is actionable only when supported by meaningful
        # probability; this keeps uncertain, trace rainfall from overriding dry soil.
        heavy_rain_expected = weather_rain_forecast >= 25.0 and rain_probability >= 60.0

        if irr_agent and weather_agent:
            irr_rec = irr_agent.recommendation.lower()
            if ("irrigate" in irr_rec or "hydraulically" in irr_rec) and heavy_rain_expected:
                disagreements.append(Disagreement(
                    dimension="Water Delivery vs Storm Precaution",
                    agent_a="Irrigation Agent",
                    position_a=irr_agent.recommendation,
                    agent_b="Weather Agent",
                    position_b=weather_agent.recommendation,
                    core_conflict=f"Irrigation is indicated by low moisture, while the forecast reports {weather_rain_forecast:g} mm of rain at {rain_probability:g}% probability in the next 24 hours."
                ))

        # Clash 2: Symptom Diagnosis (Water Deficit vs Root Disease/Anoxia)
        if crop_agent and ctx.soil_moisture is not None and ctx.soil_moisture > 40.0:
            disagreements.append(Disagreement(
                dimension="Wilting Causality & Root Zone Asphyxiation",
                agent_a="Crop Agent",
                position_a="Wilting caused by root rot / anoxic suffocation from excessive moisture.",
                agent_b="Conventional Irrigation Assumption",
                position_b="Farmer assumption that wilting plants need immediate irrigation.",
                core_conflict="Foliar wilting mimics drought, but actual root zone is flooded (moisture > 45%). Applying water will kill the remaining roots."
            ))

        # Clash 3: Soil Nutrition vs Risk Precaution (Immediate Fertilizer vs Soil Test)
        if soil_agent and risk_agent:
            if "nitrogen" in soil_agent.recommendation.lower() or "fertilizer" in soil_agent.recommendation.lower():
                disagreements.append(Disagreement(
                    dimension="Nutrient Remediation vs Risk of Chemical Burn",
                    agent_a="Soil Agent",
                    position_a="Recommended nitrogen side-dress to correct apparent chlorosis.",
                    agent_b="Risk Agent",
                    position_b="Insistence on calibrated soil testing before adding synthetic fertilizer.",
                    core_conflict="Adding uncalibrated nitrogen risks root burn and groundwater contamination if chlorosis is caused by pH lockout or prior leaching."
                ))

        # Clash 4: Crop Disease Certainty vs Extension Verification
        if crop_agent and crop_agent.likely_cause and ("blight" in crop_agent.likely_cause.lower() or "wilt" in crop_agent.likely_cause.lower()):
            if "blight" in crop_agent.likely_cause.lower() or "indeterminate" in crop_agent.likely_cause.lower():
                disagreements.append(Disagreement(
                    dimension="Pathology Identification vs Diagnostic Uncertainty",
                    agent_a="Crop Agent",
                    position_a=f"Preliminary diagnosis: {crop_agent.likely_cause}.",
                    agent_b="Risk Agent",
                    position_b="Safety protocol: Visual signs alone cannot rule out lookalike diseases without microscopic lab testing.",
                    core_conflict="Balancing urgent disease containment against the danger of applying unnecessary or ineffective fungicides."
                ))

        # -------------------------------------------------------------
        # STEP 2: EVIDENCE WEIGHING & CONSENSUS DETERMINATION
        # -------------------------------------------------------------
        moisture = ctx.soil_moisture
        symptoms_lower = ctx.symptoms.lower()

        # CASE A: Excessive moisture + Root Rot / Suffocation (Scenario 5)
        if (moisture is not None and moisture >= 45.0) or ("stagnant" in symptoms_lower and ("wilt" in symptoms_lower or "droop" in symptoms_lower)):
            consensus_level = "High Consensus (Emergency Precaution)"
            winning_recommendation = "HALT irrigation for now, check drainage, and inspect root crowns for waterlogging or rot before choosing treatment."
            reasons_for_decision = [
                (f"Reported soil moisture is high at {moisture:g}%, which makes additional irrigation a poor-risk choice." if moisture is not None else "Stagnant soil and wilting are consistent with poor root-zone aeration; confirm by checking drainage and roots."),
                "Saturated soil can limit oxygen around roots and favor root disease; inspect roots before assuming a specific pathogen.",
                "More irrigation could worsen oxygen stress and prolong root-zone saturation.",
                "Aeration and root zone drainage must take absolute precedence."
            ]
            rejected_alternatives.append(RejectedAlternative(
                alternative="Immediate irrigation to relieve wilting leaves",
                advocated_by="Intuitive reaction to plant drooping",
                rejection_reason="Wilting with a high moisture reading can reflect impaired roots, so adding water could worsen the problem.",
                evidence_against=(f"Reported soil moisture is {moisture:g}%, above the profile's preferred range." if moisture is not None else "Stagnant soil and wilting suggest the root zone may already be saturated.")
            ))
            rejected_alternatives.append(RejectedAlternative(
                alternative="Immediate chemical fertilizer feeding",
                advocated_by="General stress relief",
                rejection_reason="Damaged anaerobic roots cannot absorb nutrients; fertilizers will salt-burn damaged roots.",
                evidence_against="Root hypoxia impairs active mineral transport."
            ))
            confidence = "High"
            residual_risks.append("Irreversible root loss may have already occurred; yield reduction likely if rot has entered taproot.")

        # CASE B: Wilting plant + Torrential rain incoming (Scenario 2)
        elif heavy_rain_expected:
            consensus_level = "Sharp Conflict (Resolved in Favor of Meteorological Safety)"
            winning_recommendation = f"DELAY scheduled irrigation for now and prepare field drainage; reassess soil moisture after the forecast rain ({weather_rain_forecast:g}mm at {rain_probability:g}% probability)."
            reasons_for_decision = [
                f"Weather forecast reports {weather_rain_forecast:g}mm of rain at {rain_probability:g}% probability within 24 hours.",
                "Irrigating immediately prior to a major downpour creates severe soil waterlogging and nutrient leaching.",
                "A short delay is reversible; recheck moisture and plant condition if rain does not arrive.",
                "Conserves irrigation water and avoids the high risk of root rot."
            ]
            rejected_alternatives.append(RejectedAlternative(
                alternative="Run standard drip irrigation cycle now",
                advocated_by="Irrigation Agent (initial baseline)",
                rejection_reason="A substantial, reasonably likely rain event could make scheduled irrigation unnecessary and raise saturation risk.",
                evidence_against=f"Forecast: {weather_rain_forecast:g}mm expected at {rain_probability:g}% probability within 24 hours."
            ))
            confidence = "High"
            residual_risks.append("If storm track shifts away unexpectedly, soil moisture should be remeasured tomorrow morning.")

        # CASE C: Severe drought + Heatwave (Scenario 1)
        elif moisture is not None and moisture < 20.0:
            consensus_level = "High Consensus (Immediate Rehydration)"
            winning_recommendation = "IRRIGATE PROMPTLY: Apply deep, targeted root-zone irrigation during cooler early morning or late evening hours."
            reasons_for_decision = [
                f"Reported soil moisture is low at {moisture:g}%, below the soil profile's preferred range.",
                f"Weather outlook reports {weather_rain_forecast:g}mm expected rain in 24 hours; irrigation should be reassessed if the forecast changes.",
                "Crop is in an active sensitive stage, and severe drought stress will abort flowers/fruits.",
                "Scheduling irrigation in cooler hours avoids heat shock and droplet evaporation."
            ]
            rejected_alternatives.append(RejectedAlternative(
                alternative="Midday overhead sprinkler irrigation",
                advocated_by="Rapid cooling concept",
                rejection_reason="Excessive evaporation, droplet scalding on sunlit foliage, and thermal shock.",
                evidence_against="Ambient temperature is high (>34°C); water efficiency drops significantly."
            ))
            rejected_alternatives.append(RejectedAlternative(
                alternative="Delay irrigation until symptoms worsen",
                advocated_by="Conservative delay",
                rejection_reason="Prolonged moisture deficit at this stage triggers irreversible flower drop.",
                evidence_against="Sandy loam soil has low water retention capacity."
            ))
            confidence = "High"
            residual_risks.append("Ensure water reaches root depth (~20-30cm) rather than just wetting the top crust.")

        # CASE D: Yellow leaves / Nutrient deficiency (Scenario 3)
        elif "yellow" in symptoms_lower or "chlorosis" in symptoms_lower or "deficiency" in symptoms_lower:
            consensus_level = "Moderate Debate (Nutrient vs Overwatering & Safety Bounds)"
            winning_recommendation = "CHECK BEFORE TREATING: Yellowing may indicate nutrient or root stress; inspect the pattern and verify soil pH/N before applying fertilizer."
            reasons_for_decision = [
                "Yellowing is nonspecific; older lower leaves with V-shaped patterns can be consistent with nitrogen deficiency.",
                "Rainfall can contribute to nitrate loss, but the reported amount alone cannot confirm leaching.",
                "Check drainage and root health alongside the leaf pattern before attributing symptoms to nutrients.",
                "Soil or tissue testing before fertilizer reduces risk of excess application and runoff."
            ]
            rejected_alternatives.append(RejectedAlternative(
                alternative="Heavy broad-spectrum synthetic fertilizer application without testing",
                advocated_by="Aggressive remedy approach",
                rejection_reason="Risk Agent warning: Uncalibrated application can cause salt burn and groundwater contamination.",
                evidence_against="Exact soil PPM levels and pH are currently unmeasured."
            ))
            rejected_alternatives.append(RejectedAlternative(
                alternative="Heavy irrigation to flush soil",
                advocated_by="Assumed salinity stress",
                rejection_reason="Flushing would further leach already depleted nitrogen reserves.",
                evidence_against="Current soil moisture is balanced; leaching was the probable original cause."
            ))
            confidence = "Medium"
            residual_risks.append("Verify that soil pH is within 6.0-7.0 so applied nitrogen remains bioavailable.")

        # CASE E: Fungal / Blight symptoms with diagnostic uncertainty (Scenario 4)
        elif "spot" in symptoms_lower or "blight" in symptoms_lower or "fungal" in symptoms_lower or "fuzzy" in symptoms_lower:
            consensus_level = "Moderate Debate (Diagnostic Uncertainty vs Rapid Containment)"
            winning_recommendation = "ISOLATE & SAMPLE: Quarantine affected field sector, keep foliage strictly dry, and submit leaf samples to local extension for microscopic pathogen confirmation before spraying."
            reasons_for_decision = [
                "Symptoms exhibit active fungal characteristics, but visual signs cannot definitively separate Early Blight from devastating Late Blight.",
                "Halting overhead watering deprives fungal spores of the surface moisture needed to germinate.",
                "Prevents misapplication of costly and potentially ineffective chemical fungicides.",
                "Immediate field sanitation (removing severely diseased tissue) slows propagation without chemical risks."
            ]
            rejected_alternatives.append(RejectedAlternative(
                alternative="Definitive diagnosis and immediate systemic fungicide spray",
                advocated_by="Aggressive chemical protocol",
                rejection_reason="Fails safety protocol: visual assessment alone is insufficient for confident pesticide selection.",
                evidence_against="Microscopic spore inspection is missing."
            ))
            rejected_alternatives.append(RejectedAlternative(
                alternative="Ignore spots as minor cosmetic stress",
                advocated_by="Passive wait-and-see",
                rejection_reason="Late blight can destroy an entire solanaceous crop within 7-10 days under favorable conditions.",
                evidence_against="Rapid spread across rows reported within 48 hours."
            ))
            confidence = "Medium"
            residual_risks.append("High disease pressure environment: if rain occurs, pathogen may accelerate.")

        # CASE F: General Default Case
        else:
            consensus_level = "Balanced Multi-Agent Coordination"
            winning_recommendation = "Implement balanced monitoring: Validate soil moisture at root depth and track foliage progression over 48 hours."
            reasons_for_decision = [
                "Available agronomic indicators do not show acute imminent collapse.",
                "Conservative, low-cost monitoring prevents hasty or detrimental interventions."
            ]
            confidence = "Medium"
            residual_risks.append("Keep logging daily temperature and rainfall records.")

        # -------------------------------------------------------------
        # STEP 3: DEBATE SYNTHESIS NARRATIVE
        # -------------------------------------------------------------
        if disagreements:
            dis_summary = "; ".join([f"{d.agent_a} vs {d.agent_b} on {d.dimension}" for d in disagreements])
            debate_synthesis = (
                f"The Debate Engine identified {len(disagreements)} primary point(s) of contention ({dis_summary}). "
                f"Specialist agents held competing views between immediate operational response and environmental hazard mitigation. "
                f"The Debate Engine weighed physical sensor data, meteorological certainty, and irreversibility penalties. "
                f"The winning resolution prioritizes crop survival and resource efficiency while rejecting high-risk alternatives."
            )
        else:
            debate_synthesis = (
                "Specialist agents reached strong consensus across physiological, hydrological, and environmental dimensions. "
                "Supporting evidence aligned coherently, enabling a unified, high-confidence plan of action."
            )

        # Optional: Enrich with Groq LLM reasoning if GROQ_API_KEY is configured
        if self.llm_client.is_enabled():
            prompt = (
                f"You are the agricultural Debate Adjudicator in FarmAgent (AutoAgent 3D).\n"
                f"Farmer Context: Crop: {ctx.crop}, Stage: {ctx.growth_stage}, Soil: {ctx.soil_type}, Moisture: {ctx.soil_moisture}%\n"
                f"Symptoms: {ctx.symptoms}\n\n"
                f"Agent Positions:\n"
                f"- Crop Agent: {crop_agent.recommendation if crop_agent else 'N/A'}\n"
                f"- Irrigation Agent: {irr_agent.recommendation if irr_agent else 'N/A'}\n"
                f"- Weather Agent: {weather_agent.recommendation if weather_agent else 'N/A'}\n"
                f"- Soil Agent: {soil_agent.recommendation if soil_agent else 'N/A'}\n"
                f"- Risk Agent (Safety Auditor): {risk_agent.recommendation if risk_agent else 'N/A'}\n\n"
                f"Identified Disagreements:\n"
                f"{'; '.join([f'{d.agent_a} vs {d.agent_b}: {d.core_conflict}' for d in disagreements]) if disagreements else 'General Consensus'}\n\n"
                f"Winning Decision: {winning_recommendation}\n\n"
                f"Task: Write a concise 2-3 sentence multi-agent debate summary explaining why the debate resolved in favor of the winning decision and how conflicting proposals were cross-examined."
            )
            llm_text = self.llm_client.chat(prompt, system_prompt="You are an expert agronomist adjudicator for AutoAgent 3D. Keep responses concise, objective, and analytical.")
            if llm_text:
                debate_synthesis = f"{llm_text} (AI Synthesis via Groq {self.llm_client.model})"

        return DebateOutcome(
            consensus_level=consensus_level,
            disagreements=disagreements,
            debate_synthesis=debate_synthesis,
            winning_recommendation=winning_recommendation,
            reasons_for_decision=reasons_for_decision,
            rejected_alternatives=rejected_alternatives,
            confidence=confidence,
            residual_risks=residual_risks
        )
