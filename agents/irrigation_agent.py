"""
agents/irrigation_agent.py
Specialist agent analyzing soil moisture balance, crop water requirements, evapotranspiration factors,
and irrigation scheduling.
Outputs clear actionable recommendations: 'irrigate now', 'irrigate lightly', 'delay irrigation', or 'check soil moisture first'.
"""

from typing import Dict, Any
from utils.helpers import FarmContext, AgentResponse
from data.mock_data import CROP_PROFILES, SOIL_PROFILES, MOCK_WEATHER_DATABASE

class IrrigationAgent:
    def __init__(self):
        self.name = "Irrigation Agent"
        self.role = "Hydrology & Irrigation Management Specialist"

    def analyze(self, ctx: FarmContext, weather_data: Dict[str, Any] = None) -> AgentResponse:
        crop_clean = ctx.crop.strip().lower()
        crop_info = CROP_PROFILES.get(crop_clean, {"water_need": "medium"})
        water_need = crop_info.get("water_need", "medium")

        soil_clean = ctx.soil_type.strip().lower()
        soil_info = SOIL_PROFILES.get("loam")
        for st in SOIL_PROFILES:
            if st in soil_clean:
                soil_info = SOIL_PROFILES[st]
                break

        # Weather context
        if weather_data is None:
            weather_data = MOCK_WEATHER_DATABASE.get(ctx.weather_preset, MOCK_WEATHER_DATABASE["default"])

        temp = weather_data.get("temperature", 25.0)
        expected_rain_24h = weather_data.get("forecast_next_24h", {}).get("expected_rain_mm", 0.0)
        rain_prob = weather_data.get("forecast_next_24h", {}).get("rain_probability", 0)

        key_findings = []
        supporting_evidence = []
        challenges_raised = []
        confidence = "Medium"
        urgency = "Normal"

        key_findings.append(f"Crop '{ctx.crop}' has '{water_need}' water demand.")
        key_findings.append(f"Soil '{ctx.soil_type}' drainage profile: {soil_info.get('drainage', 'moderate')}.")

        moisture = ctx.soil_moisture
        recent_rain = ctx.recent_rainfall if ctx.recent_rainfall is not None else 0.0

        # Decision Logic
        if moisture is not None:
            ideal_min, ideal_max = soil_info.get("ideal_moisture_range", (20, 35))
            key_findings.append(f"Measured soil moisture is {moisture}% (Target range: {ideal_min}-{ideal_max}%).")

            if moisture < ideal_min:
                # Soil is dry
                if expected_rain_24h >= 25.0 or rain_prob >= 75:
                    # Hydraulic need says water, but impending storm creates operational friction
                    recommendation = "Irrigation is hydraulically indicated due to low moisture (22%), but hold pending weather adjudication"
                    supporting_evidence.append(f"Current root-zone moisture ({moisture}%) is below optimal threshold ({ideal_min}%).")
                    supporting_evidence.append(f"Foliage exhibits moisture stress; normally requires ~20-25mm replenishing cycle.")
                    challenges_raised.append(f"Imminent forecast of {expected_rain_24h}mm rain ({rain_prob}% probability) conflicts with water application.")
                    confidence = "Medium"
                elif expected_rain_24h >= 10.0:
                    recommendation = "Irrigate lightly"
                    supporting_evidence.append(f"Soil moisture ({moisture}%) is below optimal, but moderate rain ({expected_rain_24h}mm) is possible.")
                    supporting_evidence.append("A light cycle prevents severe wilting without supersaturating the root bed if rain arrives.")
                    confidence = "Medium"
                else:
                    recommendation = "Irrigate now"
                    supporting_evidence.append(f"Soil moisture ({moisture}%) is well below threshold ({ideal_min}%).")
                    supporting_evidence.append(f"No significant rain expected ({expected_rain_24h}mm), and ambient temperature is {temp}°C.")
                    confidence = "High"
                    urgency = "High"

            elif moisture > ideal_max:
                # Soil is over-saturated
                recommendation = "Delay irrigation"
                supporting_evidence.append(f"Soil moisture is excessively high at {moisture}% (well above max {ideal_max}%).")
                supporting_evidence.append("Any additional water will cause root anoxia, nutrient leaching, and increase disease vulnerability.")
                challenges_raised.append("If plants are wilting under this moisture level, do not irrigate! The root system is compromised.")
                confidence = "High"
                urgency = "High"

            else:
                # Soil moisture is in healthy range
                if expected_rain_24h > 15.0:
                    recommendation = "Delay irrigation"
                    supporting_evidence.append(f"Soil moisture is adequate ({moisture}%) and incoming rain ({expected_rain_24h}mm) will replenish the profile.")
                elif temp > 32.0:
                    recommendation = "Irrigate lightly"
                    supporting_evidence.append(f"Soil moisture ({moisture}%) is currently adequate, but high temperature ({temp}°C) will rapidly drive up evapotranspiration.")
                else:
                    recommendation = "Delay irrigation"
                    supporting_evidence.append(f"Soil moisture is optimal ({moisture}%). No immediate irrigation needed.")
                confidence = "High"

        else:
            # No direct soil moisture reading available
            supporting_evidence.append("No numeric soil moisture sensor reading provided.")
            if "wilt" in ctx.symptoms.lower() or "droop" in ctx.symptoms.lower():
                if expected_rain_24h >= 20.0:
                    recommendation = "Delay irrigation"
                    supporting_evidence.append("Visual wilting observed, but substantial rain is imminent. Pre-emptive irrigation risks severe runoff and saturation.")
                    challenges_raised.append("Wilting may be heat-induced temporary transpiration drop or vascular pathogen.")
                    confidence = "Medium"
                else:
                    recommendation = "Check soil moisture first before applying heavy irrigation"
                    supporting_evidence.append("Wilting reported, but soil moisture was not measured. Wilting can stem from both dry root zones AND rotting/waterlogged root zones.")
                    confidence = "Medium"
            elif recent_rain > 30.0:
                recommendation = "Delay irrigation"
                supporting_evidence.append(f"Recent rainfall of {recent_rain}mm was substantial.")
                confidence = "High"
            else:
                recommendation = "Check soil moisture first"
                supporting_evidence.append("Establish root-zone moisture level before triggering an irrigation schedule.")
                confidence = "Medium"

        return AgentResponse(
            agent_name=self.name,
            role=self.role,
            recommendation=recommendation,
            confidence=confidence,
            key_findings=key_findings,
            supporting_evidence=supporting_evidence,
            challenges_raised=challenges_raised,
            urgency=urgency
        )
