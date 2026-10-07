"""
agents/weather_agent.py
Specialist agent analyzing meteorological metrics, atmospheric stress, and forecasts.
Includes transparent fallback mock data mode and optional live weather API support.
Outputs weather hazard assessments and forecasts.
"""

import os
import requests
from typing import Dict, Any, Optional
from utils.helpers import FarmContext, AgentResponse
from data.mock_data import MOCK_WEATHER_DATABASE

class WeatherAgent:
    def __init__(self):
        self.name = "Weather Agent"
        self.role = "Agrometeorology & Weather Risk Specialist"
        self.api_key = os.getenv("OPENWEATHER_API_KEY", "").strip()

    def fetch_weather_data(self, ctx: FarmContext) -> Dict[str, Any]:
        """
        Attempts to fetch live weather from OpenWeatherMap if API key is provided;
        otherwise provides transparent, rich mock weather data.
        """
        if self.api_key and ctx.location:
            try:
                # Device coordinates arrive as "latitude, longitude"; typed
                # village or town names continue to use the city lookup.
                coordinates = ctx.location.split(",")
                if len(coordinates) == 2:
                    try:
                        latitude, longitude = (float(value.strip()) for value in coordinates)
                    except ValueError:
                        coordinates = []
                params = {"units": "metric", "appid": self.api_key}
                if len(coordinates) == 2:
                    params.update({"lat": latitude, "lon": longitude})
                else:
                    params["q"] = ctx.location
                res = requests.get("https://api.openweathermap.org/data/2.5/weather", params=params, timeout=4)
                if res.status_code == 200:
                    data = res.json()
                    temp = data["main"]["temp"]
                    humidity = data["main"]["humidity"]
                    wind = data["wind"]["speed"]
                    condition = data["weather"][0]["description"].title()
                    # 1-day estimated projection from live condition
                    rain_prob = 80 if "rain" in condition.lower() or "storm" in condition.lower() else 15
                    expected_mm = 20.0 if "heavy rain" in condition.lower() else (5.0 if "rain" in condition.lower() else 0.0)
                    return {
                        "source": "Live OpenWeatherMap API",
                        "location": ctx.location,
                        "temperature": temp,
                        "humidity": humidity,
                        "wind_speed": wind,
                        "current_condition": condition,
                        "forecast_next_24h": {
                            "rain_probability": rain_prob,
                            "expected_rain_mm": expected_mm,
                            "condition": condition
                        },
                        "forecast_next_48h": {
                            "rain_probability": rain_prob // 2,
                            "expected_rain_mm": 0.0,
                            "condition": "Projected clearance"
                        }
                    }
            except Exception:
                pass  # Graceful fallback to mock data

        # Mock / Demo fallback mode (transparently stated)
        preset_key = ctx.weather_preset if ctx.weather_preset in MOCK_WEATHER_DATABASE else "default"
        base_mock = MOCK_WEATHER_DATABASE[preset_key].copy()
        base_mock["source"] = f"Mock Weather Engine (Preset: '{preset_key}')"
        base_mock["location"] = ctx.location or base_mock["location"]
        return base_mock

    def analyze(self, ctx: FarmContext) -> AgentResponse:
        weather_info = self.fetch_weather_data(ctx)
        temp = weather_info.get("temperature", 25.0)
        humidity = weather_info.get("humidity", 60)
        wind = weather_info.get("wind_speed", 10.0)
        condition = weather_info.get("current_condition", "Partly Cloudy")
        forecast_24 = weather_info.get("forecast_next_24h", {})
        rain_prob = forecast_24.get("rain_probability", 0)
        expected_rain_mm = forecast_24.get("expected_rain_mm", 0.0)
        forecast_cond = forecast_24.get("condition", "Stable")
        source = weather_info.get("source", "Mock Weather")

        key_findings = [
            f"Data Source: {source}",
            f"Current: {temp}°C, {humidity}% Relative Humidity, Wind: {wind} km/h ({condition})",
            f"Next 24h Forecast: {forecast_cond} with {rain_prob}% rain probability (~{expected_rain_mm}mm expected)."
        ]
        supporting_evidence = []
        challenges_raised = []
        confidence = "High" if "Live" in source else "Medium"
        urgency = "Normal"

        # Meteorological reasoning
        if expected_rain_mm >= 30.0 or (rain_prob >= 80 and expected_rain_mm >= 20.0):
            recommendation = f"Severe Rainfall Warning: Expecting ~{expected_rain_mm}mm precipitation within 24h. Postpone field applications & prepare field drainage."
            supporting_evidence.append(f"Forecast projects {expected_rain_mm}mm heavy precipitation ({forecast_cond}).")
            supporting_evidence.append("Heavy rain will replenish all root-zone moisture naturally and wash away surface applications.")
            challenges_raised.append(f"Any planned manual irrigation or spray applications will result in runoff and chemical leaching.")
            urgency = "High"

        elif temp >= 35.0:
            recommendation = f"Heat Stress Alert: Extreme temperature ({temp}°C) and low humidity ({humidity}%) will cause rapid transpiration loss."
            supporting_evidence.append(f"Ambient temperature of {temp}°C exceeds optimal physiological range for most temperate crops.")
            supporting_evidence.append("High vapor pressure deficit (VPD) can induce midday leaf curl even when soil moisture is marginal.")
            challenges_raised.append("Do not apply foliar sprays or liquid fertilizers during midday peak heat to avoid leaf scorch.")
            urgency = "High"

        elif humidity >= 85 and temp >= 20.0:
            recommendation = f"High Fungal Disease Pressure Alert: Elevated humidity ({humidity}%) and warm weather create ideal incubation conditions for foliar pathogens."
            supporting_evidence.append(f"Sustained relative humidity above 80% creates extended leaf wetness periods.")
            supporting_evidence.append("Optimal breeding threshold for fungal spore germination (blights, powdery/downy mildews).")
            challenges_raised.append("Avoid overhead sprinkler irrigation which increases canopy moisture duration.")
            urgency = "High"

        else:
            recommendation = f"Stable Weather Outlook: Moderate temperature ({temp}°C) and manageable precipitation risk ({expected_rain_mm}mm)."
            supporting_evidence.append("Atmospheric conditions are within standard operational ranges.")

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
