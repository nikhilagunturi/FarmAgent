"""
agents/risk_agent.py
Specialist agent acting as the Chief Agricultural Safety Auditor and Devil's Advocate.
Scrutinizes all specialist proposals for over-irrigation hazards, chemical misuse,
pathogen proliferation, extreme weather clashes, and premature diagnostic certainty.
Directly challenges other agents rather than passively agreeing.
"""

from typing import Dict, Any, List
from utils.helpers import FarmContext, AgentResponse

class RiskAgent:
    def __init__(self):
        self.name = "Risk Agent"
        self.role = "Agricultural Risk, Safety & Conflict Auditor"

    def analyze(self, ctx: FarmContext, other_responses: Dict[str, AgentResponse]) -> AgentResponse:
        crop_resp = other_responses.get("Crop Agent")
        irr_resp = other_responses.get("Irrigation Agent")
        weather_resp = other_responses.get("Weather Agent")
        soil_resp = other_responses.get("Soil Agent")

        key_findings = []
        supporting_evidence = []
        challenges_raised = []
        uncertain_info = []
        urgency = "Normal"
        confidence = "High"

        # 1. Challenge: Over-irrigation vs Incoming Torrential Weather
        if irr_resp and weather_resp:
            irr_rec = irr_resp.recommendation.lower()
            weather_rec = weather_resp.recommendation.lower()
            if ("irrigate now" in irr_rec or "irrigate" in irr_rec) and ("severe rainfall" in weather_rec or "45.0mm" in str(weather_resp.supporting_evidence) or "heavy" in weather_rec):
                challenges_raised.append(
                    "CHALLENGE TO IRRIGATION: Weather forecast warns of imminent heavy precipitation. "
                    "Running irrigation now will cause severe soil saturation, root asphyxiation, nutrient leaching, and wasted energy!"
                )
                urgency = "High"

        # 2. Challenge: Wilting Misdiagnosis (Water Deficit vs Root Disease / Anoxia)
        moisture = ctx.soil_moisture
        symptoms_lower = ctx.symptoms.lower()
        if "wilt" in symptoms_lower and moisture is not None and moisture >= 38.0:
            challenges_raised.append(
                f"CRITICAL RISK TO DIAGNOSIS: Wilting observed at high soil moisture ({moisture}%). "
                "Assuming wilting always implies water shortage is a fatal trap! Roots are drowning or decaying from fungal pathogens (Pythium/Phytophthora). "
                "Any irrigation will accelerate root mortality!"
            )
            urgency = "Critical"

        # 3. Challenge: Chemical & Fertilizer Misuse Without Lab Testing
        if "yellow" in symptoms_lower or "deficiency" in symptoms_lower or (soil_resp and "fertilizer" in soil_resp.recommendation.lower()):
            challenges_raised.append(
                "CAUTION ON FERTILIZER APPLICATION: Adding synthetic chemical fertilizers without calibrated soil EC/pH test "
                "risks root burn, salt accumulation, ground-water nitrate pollution, and financial waste."
            )

        # 4. Challenge: Premature Pathogen Diagnosis & Pesticide Escalation
        if crop_resp and crop_resp.likely_cause and ("blight" in crop_resp.likely_cause.lower() or "fungal" in crop_resp.likely_cause.lower() or "wilt" in crop_resp.likely_cause.lower()):
            challenges_raised.append(
                f"DIAGNOSTIC UNCERTAINTY: Visual foliar symptoms alone cannot guarantee species identity ({crop_resp.likely_cause}). "
                "Applying unverified chemical fungicides without local agronomist confirmation could breed chemical resistance or harm beneficial microflora."
            )
            uncertain_info.append("Absence of microscopic pathogen spore verification.")

        # 5. Challenge: Midday Spraying / Thermal Stress Hazards
        if weather_resp and "heat stress" in weather_resp.recommendation.lower():
            challenges_raised.append(
                "THERMAL SHOCK HAZARD: High ambient temperatures increase risk of chemical leaf scorch and droplet flash-evaporation. "
                "All field interventions must be restricted to dawn or late twilight."
            )

        # 6. Check for general missing data uncertainty
        if ctx.soil_moisture is None:
            uncertain_info.append("Soil moisture percentage is unmeasured; decisions carry increased uncertainty.")
        if ctx.recent_rainfall is None:
            uncertain_info.append("Recent 7-day cumulative rainfall was not reported.")

        # Formulate proactive risk mitigation recommendation
        if urgency == "Critical":
            recommendation = (
                "EMERGENCY RISK DIRECTIVE: Halt all irrigation immediately! High risk of catastrophic root rot or anoxia. "
                "Inspect subterranean root tissues and initiate drainage remedies."
            )
        elif challenges_raised:
            recommendation = (
                f"RISK AUDIT ACTIVE: Identified {len(challenges_raised)} critical friction point(s). "
                "Enforce precautionary principle: prioritize crop survival, avoid unnecessary chemical input, and delay irreversible actions."
            )
        else:
            recommendation = (
                "STANDARD RISK PROTOCOL: No high-severity conflicts detected. Proceed with measured, progressive intervention."
            )

        key_findings.append(f"Safety checks performed across {len(other_responses)} specialist outputs.")
        key_findings.append(f"Flagged {len(challenges_raised)} operational and agronomic risks.")

        return AgentResponse(
            agent_name=self.name,
            role=self.role,
            recommendation=recommendation,
            confidence=confidence,
            key_findings=key_findings,
            supporting_evidence=supporting_evidence,
            challenges_raised=challenges_raised,
            uncertain_info=uncertain_info,
            urgency=urgency
        )
