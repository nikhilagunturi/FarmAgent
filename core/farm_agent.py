"""
core/farm_agent.py
Master Coordinator Agent for FarmAgent (AutoAgent 3D: DEVELOP • DEBATE • DEFEND).
Orchestrates problem intake, specialist dispatch (Develop), multi-agent debate (Debate),
and decision synthesis with robust argumentation (Defend).
"""

from typing import Dict, Any, List, Optional
from utils.helpers import (
    FarmContext,
    AgentResponse,
    FarmDecisionReport
)
from agents.crop_agent import CropAgent
from agents.irrigation_agent import IrrigationAgent
from agents.weather_agent import WeatherAgent
from agents.soil_agent import SoilAgent
from agents.risk_agent import RiskAgent
from core.debate_engine import DebateEngine

class FarmAgentCoordinator:
    def __init__(self):
        self.crop_agent = CropAgent()
        self.irrigation_agent = IrrigationAgent()
        self.weather_agent = WeatherAgent()
        self.soil_agent = SoilAgent()
        self.risk_agent = RiskAgent()
        self.debate_engine = DebateEngine()

    def determine_relevant_specialists(self, ctx: FarmContext) -> List[str]:
        """
        Dynamically routes the problem to relevant specialist agents based on context.
        All 5 agents participate in full agricultural assessments.
        """
        # In this complete agricultural decision system, all 5 specialist domains
        # provide essential perspectives to ensure no blind spots.
        return ["Crop Agent", "Irrigation Agent", "Weather Agent", "Soil Agent", "Risk Agent"]

    def analyze(self, ctx: FarmContext) -> FarmDecisionReport:
        """
        Executes the complete AutoAgent 3D Pipeline:
        1. DEVELOP: Specialist agents analyze domain factors independently.
        2. DEBATE: Debate engine discovers clashes, cross-examines evidence, and resolves tension.
        3. DEFEND: FarmAgent coordinates the final synthesis, explains rationale, and defends against rejected alternatives.
        """
        # -------------------------------------------------------------
        # 1. DEVELOP STAGE: Specialist Agent Analysis
        # -------------------------------------------------------------
        agent_opinions: Dict[str, AgentResponse] = {}

        # First pass: Domain specialist perspectives
        weather_info = self.weather_agent.fetch_weather_data(ctx)
        agent_opinions["Weather Agent"] = self.weather_agent.analyze(ctx)
        agent_opinions["Crop Agent"] = self.crop_agent.analyze(ctx)
        agent_opinions["Irrigation Agent"] = self.irrigation_agent.analyze(ctx, weather_data=weather_info)
        agent_opinions["Soil Agent"] = self.soil_agent.analyze(ctx)

        # Risk Agent reviews all prior specialist outputs to audit and challenge
        agent_opinions["Risk Agent"] = self.risk_agent.analyze(ctx, agent_opinions)

        # -------------------------------------------------------------
        # 2. DEBATE STAGE: Clash Identification & Evidence Adjudication
        # -------------------------------------------------------------
        debate_outcome = self.debate_engine.adjudicate(ctx, agent_opinions)

        # -------------------------------------------------------------
        # 3. DEFEND STAGE: Rationale Formulation & Defense Construction
        # -------------------------------------------------------------
        moisture_label = "Not provided"
        if ctx.soil_moisture is not None:
            proxy_note = " (rough estimate from soil feel; not a sensor reading)" if "not a sensor measurement" in ctx.additional_info else " (value entered by farmer)"
            moisture_label = f"{ctx.soil_moisture}%{proxy_note}"
        rainfall_label = "Not provided"
        if ctx.recent_rainfall is not None:
            rainfall_label = f"{ctx.recent_rainfall} mm (value entered by farmer)"
        observations = [
            f"Crop: {ctx.crop} at {ctx.growth_stage} stage in {ctx.location}",
            f"Soil Type: {ctx.soil_type} | Soil moisture: {moisture_label}",
            f"Recent Rainfall: {rainfall_label}",
            f"Weather Context: {weather_info.get('temperature')}°C, {weather_info.get('current_condition')}, 24h Rain Prob: {weather_info.get('forecast_next_24h', {}).get('rain_probability')}%",
            f"Reported Symptoms: {ctx.symptoms}"
        ]

        # Formulate actionable next steps based on debate outcome
        next_steps = []
        if "HALT" in debate_outcome.winning_recommendation:
            next_steps.extend([
                "Turn off all drip/sprinkler lines immediately.",
                "Dig 30cm inspection holes between rows to check for water table ponding.",
                "Extract 2 root samples to check for brown, mushy cortical tissue (root rot).",
                "Ensure drainage furrows are cleared of silt and organic debris."
            ])
        elif "DELAY" in debate_outcome.winning_recommendation:
            next_steps.extend([
                "Hold off on turning on irrigation valves.",
                "Verify local radar / rain gauge after 12-24 hours.",
                "Re-check soil moisture after the storm passes before resetting schedule."
            ])
        elif "IRRIGATE PROMPTLY" in debate_outcome.winning_recommendation:
            next_steps.extend([
                "Schedule irrigation cycle for early morning (5:00 AM - 8:00 AM) or sunset.",
                "Verify water penetration depth reaches the root zone (20-30cm).",
                "Monitor leaf turgidity recovery within 4 hours after watering."
            ])
        elif "Nitrogen" in debate_outcome.winning_recommendation:
            next_steps.extend([
                "Perform a quick field soil test (pH and Nitrate-N) or send sample to local lab.",
                "If deficient, apply recommended side-dress of urea/compost along row margins.",
                "Avoid foliar fertilization during direct midday sunlight."
            ])
        elif "ISOLATE" in debate_outcome.winning_recommendation:
            next_steps.extend([
                "Flag and isolate affected crop rows to minimize equipment/foot traffic transmission.",
                "Disinfect pruning tools with 70% alcohol or 10% bleach solution between rows.",
                "Take clear photos of upper and lower leaf surfaces and contact county agricultural extension agent.",
                "Do not use overhead sprinklers which splash fungal spores to adjacent foliage."
            ])
        else:
            next_steps.extend([
                "Monitor crop vigor every morning and evening.",
                "Take physical soil core readings at 15cm and 30cm depths."
            ])

        # Synthesize consolidated uncertainties
        risks_and_uncertainty = list(debate_outcome.residual_risks)
        for resp in agent_opinions.values():
            for unc in resp.uncertain_info:
                if unc not in risks_and_uncertainty:
                    risks_and_uncertainty.append(unc)

        problem_summary = f"{ctx.crop} in {ctx.location} exhibiting: '{ctx.symptoms}'"

        report = FarmDecisionReport(
            problem_summary=problem_summary,
            observations=observations,
            agent_opinions=agent_opinions,
            disagreements=debate_outcome.disagreements,
            debate_summary=debate_outcome.debate_synthesis,
            final_decision=debate_outcome.winning_recommendation,
            reasons_for_decision=debate_outcome.reasons_for_decision,
            rejected_alternatives=debate_outcome.rejected_alternatives,
            confidence=debate_outcome.confidence,
            risks_and_uncertainty=risks_and_uncertainty,
            recommended_next_steps=next_steps
        )

        return report
