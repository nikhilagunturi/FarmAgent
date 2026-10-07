"""
data/mock_data.py
Contains mock weather datasets, crop profiles, soil characteristics, common plant diseases,
and 5 pre-configured demo scenarios illustrating agent agreements and conflicts.
Works 100% offline without needing any API keys.
"""

from typing import Dict, Any, List

# Standard crop water & soil guidelines
CROP_PROFILES: Dict[str, Dict[str, Any]] = {
    "tomato": {
        "optimal_ph": (6.0, 6.8),
        "water_need": "medium",  # ~25-35mm per week
        "soil_pref": ["loam", "sandy loam", "well-drained clay loam"],
        "temp_range": (18, 29),  # Celsius
        "critical_stages": ["flowering", "fruit setting"],
        "common_issues": ["bacterial wilt", "early blight", "blossom end rot", "fusarium wilt"]
    },
    "corn": {
        "optimal_ph": (5.8, 7.0),
        "water_need": "high",  # ~35-45mm per week
        "soil_pref": ["loam", "silt loam"],
        "temp_range": (18, 32),
        "critical_stages": ["silking", "grain filling"],
        "common_issues": ["leaf blight", "nitrogen deficiency", "corn borer"]
    },
    "wheat": {
        "optimal_ph": (6.0, 7.5),
        "water_need": "low_to_medium",
        "soil_pref": ["loam", "clay loam"],
        "temp_range": (15, 24),
        "critical_stages": ["tillering", "booting", "flowering"],
        "common_issues": ["rust", "powdery mildew", "aphids"]
    },
    "rice": {
        "optimal_ph": (5.5, 6.5),
        "water_need": "very_high",
        "soil_pref": ["clay", "clay loam"],
        "temp_range": (20, 35),
        "critical_stages": ["tillering", "panicle initiation"],
        "common_issues": ["bacterial blight", "sheath blight", "stem borer"]
    },
    "potato": {
        "optimal_ph": (5.0, 6.0),
        "water_need": "medium",
        "soil_pref": ["sandy loam", "loose loam"],
        "temp_range": (15, 22),
        "critical_stages": ["tuber initiation", "tuber bulking"],
        "common_issues": ["late blight", "scab", "aphids", "waterlogging rot"]
    },
    "cotton": {
        "optimal_ph": (5.8, 8.0),
        "water_need": "medium",
        "soil_pref": ["deep sandy loam", "black clay loam"],
        "temp_range": (21, 35),
        "critical_stages": ["squaring", "flowering", "boll development"],
        "common_issues": ["bollworm", "root rot", "potassium deficiency"]
    }
}

# Soil profile default behaviors
SOIL_PROFILES: Dict[str, Dict[str, Any]] = {
    "sandy": {
        "drainage": "very fast",
        "water_retention": "low",
        "leaching_risk": "high",
        "ideal_moisture_range": (15, 25),  # percentage
        "note": "Dries out rapidly; requires frequent light irrigation."
    },
    "loam": {
        "drainage": "well-drained",
        "water_retention": "balanced",
        "leaching_risk": "medium",
        "ideal_moisture_range": (25, 40),
        "note": "Ideal balance of drainage and moisture retention for most crops."
    },
    "clay": {
        "drainage": "slow",
        "water_retention": "very high",
        "leaching_risk": "low",
        "ideal_moisture_range": (30, 45),
        "note": "Prone to waterlogging and compaction; high risk of root suffocation."
    },
    "silt": {
        "drainage": "moderate",
        "water_retention": "high",
        "leaching_risk": "low to moderate",
        "ideal_moisture_range": (25, 40),
        "note": "Holds nutrients and water well, but easily compacted."
    }
}

# Regional mock weather conditions (used when no external API key is present)
MOCK_WEATHER_DATABASE: Dict[str, Dict[str, Any]] = {
    "default": {
        "location": "Central Farmland Region",
        "temperature": 27.5,
        "humidity": 62,
        "wind_speed": 12.0,
        "current_condition": "Partly Cloudy",
        "forecast_next_24h": {
            "rain_probability": 20,
            "expected_rain_mm": 1.0,
            "condition": "Mainly Sunny with light breeze"
        },
        "forecast_next_48h": {
            "rain_probability": 15,
            "expected_rain_mm": 0.0,
            "condition": "Clear and warm"
        }
    },
    "heavy_rain_incoming": {
        "location": "Midwest / River Valley",
        "temperature": 24.0,
        "humidity": 85,
        "wind_speed": 22.0,
        "current_condition": "Overcast and humid",
        "forecast_next_24h": {
            "rain_probability": 90,
            "expected_rain_mm": 45.0,
            "condition": "Severe thunderstorm with heavy precipitation"
        },
        "forecast_next_48h": {
            "rain_probability": 75,
            "expected_rain_mm": 25.0,
            "condition": "Continuous showers and cool winds"
        }
    },
    "dry_heatwave": {
        "location": "Arid Plains",
        "temperature": 36.5,
        "humidity": 28,
        "wind_speed": 18.0,
        "current_condition": "Scorching Sun",
        "forecast_next_24h": {
            "rain_probability": 5,
            "expected_rain_mm": 0.0,
            "condition": "High thermal stress, 0% cloud cover"
        },
        "forecast_next_48h": {
            "rain_probability": 0,
            "expected_rain_mm": 0.0,
            "condition": "Continuing heatwave"
        }
    }
}

# 5 Core Test Scenarios mandated by project instructions
DEMO_SCENARIOS: List[Dict[str, Any]] = [
    {
        "id": "scenario_1",
        "title": "Scenario 1: Tomato Wilting + Low Soil Moisture (Agreement on Irrigation)",
        "description": "Tomato plants showing classic drought stress under high heat and dried out soil with no upcoming rain.",
        "input": {
            "crop": "Tomato",
            "growth_stage": "Fruit setting / Flowering",
            "location": "Valley Farm, Field 4",
            "soil_type": "Sandy Loam",
            "symptoms": "Leaves are droopy and curling inward during midday. Stems still firm. Soil surface is dry and crusty.",
            "soil_moisture": 14.0,  # Below threshold
            "recent_rainfall": 0.0,  # None in past 7 days
            "weather_preset": "dry_heatwave",
            "additional_info": "Last irrigated 5 days ago. Sunlight is intense (34°C)."
        },
        "expected_debate_dynamics": "High consensus: Irrigation Agent strongly urges immediate watering, Weather confirms hot & dry, Crop identifies drought stress, Risk Agent cautions against midday thermal shock."
    },
    {
        "id": "scenario_2",
        "title": "Scenario 2: Tomato Wilting + Heavy Rain Forecast (Sharp Agent Conflict!)",
        "description": "Tomato plants wilting, prompting irrigation recommendation, but heavy rain is forecasted in 12 hours.",
        "input": {
            "crop": "Tomato",
            "growth_stage": "Vegetative / Early Flowering",
            "location": "South Basin",
            "soil_type": "Clay Loam",
            "symptoms": "Upper leaves drooping slightly, topsoil feels dry to touch.",
            "soil_moisture": 22.0,  # Moderate/low top layer
            "recent_rainfall": 2.0,
            "weather_preset": "heavy_rain_incoming",
            "additional_info": "Farmer is preparing to run drip system for 4 hours."
        },
        "expected_debate_dynamics": "Direct clash: Irrigation Agent suggests watering, but Weather Agent and Risk Agent vehemently reject irrigation due to 45mm impending storm causing waterlogging and fungal risks."
    },
    {
        "id": "scenario_3",
        "title": "Scenario 3: Yellow Leaves on Corn (Nutrient vs Overwatering Debate)",
        "description": "Lower leaves turning yellow along midrib in corn field. Soil has normal moisture.",
        "input": {
            "crop": "Corn",
            "growth_stage": "V6 (Vegetative rapid growth)",
            "location": "North Meadow",
            "soil_type": "Loam",
            "symptoms": "Oldest lower leaves showing V-shaped yellowing starting at leaf tips and moving down midrib. Upper leaves green.",
            "soil_moisture": 32.0,
            "recent_rainfall": 15.0,
            "weather_preset": "default",
            "additional_info": "NPK fertilizer applied at planting 4 weeks ago, but heavy rain occurred 2 weeks ago."
        },
        "expected_debate_dynamics": "Crop & Soil agents suspect Nitrogen deficiency (leached by previous rains). Risk agent warns against indiscriminate chemical nitrogen application without soil testing."
    },
    {
        "id": "scenario_4",
        "title": "Scenario 4: Crop Disease Symptoms with Uncertain Diagnosis",
        "description": "Dark spots and fuzzy margins on potato leaves; insufficient information to rule out Early vs Late Blight.",
        "input": {
            "crop": "Potato",
            "growth_stage": "Tuber bulking",
            "location": "Highland Patch",
            "soil_type": "Loam",
            "symptoms": "Irregular brownish-black spots on foliage. Some white fungal growth observed under moist morning conditions.",
            "soil_moisture": 38.0,
            "recent_rainfall": 25.0,
            "weather_preset": "default",
            "additional_info": "Spreading to neighboring rows over last 48 hours."
        },
        "expected_debate_dynamics": "Crop agent must distinguish between Likely Cause (Late Blight / Phytophthora) vs Possible Cause (Early Blight) vs Uncertain Info. Risk agent forbids definitive diagnosis and insists on agricultural extension confirmation."
    },
    {
        "id": "scenario_5",
        "title": "Scenario 5: Excessive Soil Moisture & Root Rot Risk (Agreement on Halting Water)",
        "description": "Saturated clay soil with wilting plants; adding water would be catastrophic.",
        "input": {
            "crop": "Tomato",
            "growth_stage": "Fruiting",
            "location": "River Bend Lowland",
            "soil_type": "Heavy Clay",
            "symptoms": "Plants are wilting despite wet soil. Lower stems dark near soil line. Soil smells stagnant.",
            "soil_moisture": 52.0,  # Over-saturated
            "recent_rainfall": 60.0,
            "weather_preset": "default",
            "additional_info": "Farmer thought plants were wilting from thirst and almost turned on water pump."
        },
        "expected_debate_dynamics": "High risk warning: Wilting is caused by root anoxia / Pythium root rot, NOT water deficiency! All agents reject irrigation. Risk Agent issues severe hazard warning."
    }
]
