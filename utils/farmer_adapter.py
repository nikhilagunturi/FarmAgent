"""
utils/farmer_adapter.py
Bridges simple farmer observations with FarmAgent's technical multi-agent engine.
1. Translates simple observations (crop icon, problem buttons, soil feel) into FarmContext.
2. Transforms technical multi-agent reports into simple, jargon-free advice for farmers.
"""

from typing import Dict, Any, List, Optional
from utils.helpers import FarmContext, FarmDecisionReport

# Visual crop mapping
CROP_DISPLAY_MAP = {
    "tomato": "Tomato",
    "rice": "Rice",
    "maize": "Corn",
    "corn": "Corn",
    "potato": "Potato",
    "chilli": "Chilli",
    "groundnut": "Groundnut",
    "cotton": "Cotton",
    "wheat": "Wheat",
    "other": "General Crop"
}

# Internal estimates used by the existing specialist agents. These are coarse
# farmer-reported proxies, not sensor readings or measured percentages.
SOIL_FEEL_MAP = {
    "very_dry": 14.0,       # Below permanent wilting point
    "slightly_dry": 21.0,   # Moderate deficit
    "normal": 30.0,         # Optimal field capacity
    "wet": 42.0,            # High moisture
    "very_wet": 52.0,       # Waterlogged / oversaturated
    "unknown": None
}

# Simple problem tag descriptions
PROBLEM_TAG_DESCRIPTIONS = {
    "thirsty": "Plant looks thirsty and droopy",
    "yellow_leaves": "Leaves are turning yellow",
    "curling_leaves": "Leaves are curling inward or downward",
    "insects": "Visible insects or bug damage on leaves",
    "disease": "Dark spots, lesions, or mold suggesting disease",
    "poor_growth": "Plant is stunted or not growing well",
    "too_much_water": "Standing water or soil is soaked",
    "heat_stress": "Extreme scorching heat and sun stress",
    "unknown": "Uncertain plant issue"
}

def parse_farmer_input(data: Dict[str, Any]) -> FarmContext:
    """
    Takes simple farmer UI inputs and builds a complete FarmContext for the specialist agents.
    Respects any optional advanced inputs if provided.
    """
    # 1. Resolve Crop Name
    crop_selected = (data.get("crop_choice") or "").strip().lower()
    custom_crop = (data.get("custom_crop") or "").strip()
    if custom_crop:
        crop = custom_crop.title()
    elif crop_selected and crop_selected in CROP_DISPLAY_MAP:
        crop = CROP_DISPLAY_MAP[crop_selected]
    else:
        crop = data.get("crop", "Tomato").title()

    # 2. Resolve Symptoms from Simple Choices + Natural Language Description
    selected_problems: List[str] = data.get("problem_tags", [])
    if isinstance(selected_problems, str):
        selected_problems = [p.strip() for p in selected_problems.split(",") if p.strip()]

    problem_phrases = [PROBLEM_TAG_DESCRIPTIONS.get(p, p) for p in selected_problems if p in PROBLEM_TAG_DESCRIPTIONS or p]
    own_words = (data.get("own_words") or data.get("symptoms") or "").strip()

    combined_symptoms_parts = []
    if problem_phrases:
        combined_symptoms_parts.append("Observed issues: " + "; ".join(problem_phrases))
    if own_words:
        combined_symptoms_parts.append(f"Farmer notes: \"{own_words}\"")
    
    symptoms = " | ".join(combined_symptoms_parts) if combined_symptoms_parts else "General crop observation"

    # 3. Resolve Soil Moisture from "How does soil look/feel?"
    soil_feel = data.get("soil_feel") or "unknown"
    if data.get("soil_moisture") not in [None, ""]:
        try:
            soil_moisture = float(data.get("soil_moisture"))
        except ValueError:
            soil_moisture = SOIL_FEEL_MAP.get(soil_feel)
    else:
        soil_moisture = SOIL_FEEL_MAP.get(soil_feel)

    # A yes/no observation cannot be converted into a rainfall measurement.
    rained_recently = data.get("rained_recently")  # "yes", "no", "unknown"
    if data.get("recent_rainfall") not in [None, ""]:
        try:
            recent_rainfall = float(data.get("recent_rainfall"))
        except ValueError:
            recent_rainfall = None
    else:
        recent_rainfall = None

    # 5. Resolve Weather Preset / Simulation
    weather_preset = data.get("weather_preset") or "default"
    if "too_much_water" in selected_problems or soil_feel == "very_wet":
        if weather_preset == "default" and "rain_forecast" in data and data["rain_forecast"] == "heavy":
            weather_preset = "heavy_rain_incoming"
    if "heat_stress" in selected_problems or (data.get("temperature_feel") == "scorching"):
        weather_preset = "dry_heatwave"

    # 6. Additional Context (Watering history, location, photo flag)
    last_watered = data.get("last_watered", "")
    location = (data.get("location") or "Location not provided").strip()
    growth_stage = (data.get("growth_stage") or "Unknown").strip()
    soil_type = (data.get("soil_type") or "Unknown").strip()
    has_photo = bool(data.get("has_photo") or data.get("photo_data"))

    extra_notes = []
    if last_watered and last_watered != "unknown":
        extra_notes.append(f"Last watered: {last_watered}")
    if data.get("soil_moisture") not in [None, ""]:
        extra_notes.append("Soil moisture entered by farmer as a measured value")
    elif soil_feel != "unknown":
        extra_notes.append(f"Farmer-reported soil feel: {soil_feel.replace('_', ' ')} (not a sensor measurement)")
    if rained_recently in {"yes", "no"}:
        extra_notes.append(f"Farmer-reported recent rain: {rained_recently} (amount not measured)")
    if data.get("temperature") not in [None, ""]:
        extra_notes.append(f"Farmer-provided temperature: {data['temperature']}°C")
    if has_photo:
        extra_notes.append("Photo uploaded by farmer for visual pathology check")
    if data.get("additional_info"):
        extra_notes.append(str(data["additional_info"]))

    return FarmContext(
        crop=crop,
        growth_stage=growth_stage,
        location=location,
        soil_type=soil_type,
        symptoms=symptoms,
        soil_moisture=soil_moisture,
        recent_rainfall=recent_rainfall,
        weather_preset=weather_preset,
        additional_info="; ".join(extra_notes)
    )


def create_farmer_view(report: FarmDecisionReport, data: Dict[str, Any], llm_client=None) -> Dict[str, Any]:
    """
    Transforms the technical FarmDecisionReport into 6 clear, friendly farmer sections:
    1. WHAT WE FOUND
    2. WHAT YOU SHOULD DO
    3. BE CAREFUL
    4. WATCH FOR
    5. WHY FARMAGENT THINKS THIS
    6. AGENT DEBATE (Simplified Dialogue)
    """
    crop = (data.get("custom_crop") or data.get("crop") or "plant").capitalize()
    soil_feel = data.get("soil_feel") or "unknown"
    problem_tags = data.get("problem_tags", [])
    has_photo = bool(data.get("has_photo") or data.get("photo_data"))

    decision_lower = report.final_decision.lower()
    
    # ---------------------------------------------------------
    # 1. WHAT WE FOUND
    # ---------------------------------------------------------
    if "halt" in decision_lower or soil_feel == "very_wet" or "saturated" in decision_lower:
        finding_key = "too_wet"
        what_we_found = f"Your {crop} may be getting too much water. Soil that stays very wet can harm the roots."
    elif "delay" in decision_lower or "rain" in decision_lower:
        weather_agent = report.agent_opinions.get("Weather Agent")
        weather_source = " ".join(weather_agent.key_findings).lower() if weather_agent else ""
        if "mock" in weather_source or "demo" in weather_source:
            finding_key = "sample_rain"
            what_we_found = "The sample weather used for this check suggests rain may come soon. Please check your local weather before changing watering."
        else:
            finding_key = "rain_check"
            what_we_found = f"Rain may be coming soon. Check your local weather and soil before watering your {crop}."
    elif "irrigate" in decision_lower or "rehydrate" in decision_lower or soil_feel == "very_dry":
        finding_key = "needs_water"
        what_we_found = f"Your {crop} may need water. You reported that the soil feels very dry."
    elif "nitrogen" in decision_lower or "yellow" in str(report.observations).lower():
        finding_key = "yellow_leaves"
        what_we_found = f"Yellow leaves can have several causes, including water, insects, disease, or soil nutrients. We cannot confirm the cause from this alone."
    elif "isolate" in decision_lower or "fungal" in decision_lower or "blight" in decision_lower:
        finding_key = "possible_leaf_issue"
        what_we_found = f"Your {crop} may have a leaf problem. A description alone cannot confirm whether it is disease or insect damage."
    else:
        finding_key = "unclear"
        what_we_found = f"We do not have enough information to identify the cause of the problem with your {crop} yet."

    # ---------------------------------------------------------
    # 2. WHAT YOU SHOULD DO (Clear Actionable Steps)
    # ---------------------------------------------------------
    what_to_do = []
    if "halt" in decision_lower:
        action_key = "stop_water"
        what_to_do = [
            "Do not add more water while the soil is very wet.",
            "If water is pooling, help it drain away from the plants.",
            "Check the soil again after the extra water has drained."
        ]
    elif "delay" in decision_lower:
        action_key = "wait_rain"
        what_to_do = [
            "Wait before watering. Check your local weather first.",
            "Make sure extra water can drain from the field.",
            "Check the soil again after the rain, if it comes."
        ]
    elif "irrigate" in decision_lower or "rehydrate" in decision_lower:
        action_key = "water_once"
        what_to_do = [
            "Water the plants once during the cool early morning or evening.",
            "Water the soil around the plants, not just the surface.",
            "Check the soil again before watering a second time."
        ]
    elif "nitrogen" in decision_lower or "yellow" in str(report.observations).lower():
        action_key = "check_yellow"
        what_to_do = [
            "Look closely at both sides of the leaves for insects or spots.",
            "Check whether the soil is too dry or stays very wet.",
            "Ask a local farm expert before adding fertilizer."
        ]
    elif "isolate" in decision_lower:
        action_key = "leaf_issue"
        what_to_do = [
            "Take a clear photo of the affected leaves in good light.",
            "Avoid touching healthy plants after handling affected leaves.",
            "Ask a local farm expert before using a chemical spray."
        ]
    else:
        action_key = "monitor"
        what_to_do = [
            "Check the soil moisture 5 cm below the surface with your finger every morning.",
            "Keep monitoring the leaves over the next 2 days to see if the symptoms spread."
        ]

    # ---------------------------------------------------------
    # 3. BE CAREFUL (Risks & Traps to Avoid)
    # ---------------------------------------------------------
    if "halt" in decision_lower:
        careful_key = "wet_soil"
        be_careful = ["Do not keep watering if the soil is already very wet."]
    elif "delay" in decision_lower:
        careful_key = "sample_weather"
        be_careful = ["Do not rely on a sample weather forecast. Check local conditions before watering."]
    elif "nitrogen" in decision_lower or "yellow" in str(report.observations).lower():
        careful_key = "fertilizer"
        be_careful = ["Do not add fertilizer until you have checked the soil or asked a local expert."]
    else:
        careful_key = "spray"
        be_careful = ["Do not use a chemical spray until you know what is causing the problem."]

    # ---------------------------------------------------------
    # 4. WATCH FOR (What to Monitor Next)
    # ---------------------------------------------------------
    watch_for = []
    if "halt" in decision_lower:
        watch_key = "wet_soil"
        watch_for.append("See whether the leaves look better as the soil dries.")
        watch_for.append("Watch for yellowing or a bad smell near the plants.")
    elif "delay" in decision_lower:
        watch_key = "rain"
        watch_for.append("Check whether rain actually falls in your area.")
        watch_for.append("If no rain comes, check the soil again before watering.")
    elif "irrigate" in decision_lower:
        watch_key = "watering"
        watch_for.append("See whether the leaves look better after watering.")
        watch_for.append("If leaves stay curled, take a clear photo and check for insects or spots.")
    else:
        watch_key = "general"
        watch_for.append("Check whether new leaves sprouting at the top are healthy and green.")
        watch_for.append("Inspect the undersides of leaves with good light to look for tiny crawling insects.")

    # ---------------------------------------------------------
    # 5. WHY FARMAGENT THINKS THIS (Plain Language Rationale)
    # ---------------------------------------------------------
    why_farmagent_thinks_this = [
        f"We considered the {crop} problem you described and the soil condition you selected.",
        "FarmAgent compared advice about the crop, water, weather, and possible risks."
    ]

    # ---------------------------------------------------------
    # 6. SIMPLIFIED AGENT DEBATE (Conversational Dialogue)
    # ---------------------------------------------------------
    agents = report.agent_opinions
    simplified_debate = [
        {
            "icon": "💧",
            "agent": "Water Agent",
            "domain": "water",
            "dialogue": _simplify_agent_dialogue(agents.get("Irrigation Agent"), "water")
        },
        {
            "icon": "🌦️",
            "agent": "Weather Agent",
            "domain": "weather",
            "dialogue": _simplify_agent_dialogue(agents.get("Weather Agent"), "weather")
        },
        {
            "icon": "🌱",
            "agent": "Crop Agent",
            "domain": "crop",
            "dialogue": _simplify_agent_dialogue(agents.get("Crop Agent"), "crop")
        },
        {
            "icon": "🛡️",
            "agent": "Risk Agent (Safety)",
            "domain": "risk",
            "dialogue": _simplify_agent_dialogue(agents.get("Risk Agent"), "risk")
        }
    ]

    # ---------------------------------------------------------
    # CONFIDENCE & PHOTO NOTICE
    # ---------------------------------------------------------
    conf_level = report.confidence.lower()
    if conf_level == "high":
        confidence_text = "🟢 High confidence — your observations give a clear, consistent picture."
    elif conf_level == "medium":
        confidence_text = "🟡 Medium confidence — " + ("a photo of your leaves would help us confirm!" if not has_photo else "visual confirmation is ongoing.")
    else:
        confidence_text = "🔴 Low confidence — we need a bit more information or a clear photo of the leaves."

    return {
        "what_we_found": what_we_found,
        "finding_key": finding_key,
        "what_to_do": what_to_do,
        "action_key": action_key,
        "be_careful": be_careful,
        "careful_key": careful_key,
        "watch_for": watch_for,
        "watch_key": watch_key,
        "why_farmagent_thinks_this": why_farmagent_thinks_this,
        "simplified_debate": simplified_debate,
        "final_decision_simple": _simple_final_decision(decision_lower),
        "final_decision_key": _simple_final_decision_key(decision_lower),
        "confidence_friendly": confidence_text,
        "confidence_level": report.confidence,
        "has_photo": has_photo
    }


def _simplify_agent_dialogue(agent, domain: str) -> str:
    """Translates technical agent responses into friendly quotes for the debate dialogue."""
    if not agent:
        return "I am monitoring conditions in this field."
    
    rec = agent.recommendation
    rec_lower = rec.lower()

    if domain == "water":
        if "delay" in rec_lower:
            return "Hold the water! Adding more water right now is unnecessary or dangerous."
        elif "irrigate now" in rec_lower:
            return "The soil is running dry. We should give the crop a drink soon."
        elif "lightly" in rec_lower:
            return "Give a light watering, but don't soak the ground."
        else:
            return "Let's check the moisture before turning on the water pump."

    elif domain == "weather":
        is_demo_weather = any("mock" in finding.lower() or "demo" in finding.lower() for finding in agent.key_findings)
        if "severe rainfall" in rec_lower or "rain" in rec_lower:
            if is_demo_weather:
                return "The sample weather suggests rain. Please check your local forecast before watering."
            return "Heads up! Heavy rain is forecasted soon, which will naturally water the field."
        elif "heat stress" in rec_lower or "heat" in rec_lower:
            if is_demo_weather:
                return "The sample weather is hot. Check your local conditions before acting."
            return "It's scorching hot today! Plants will lose moisture fast under this direct sun."
        else:
            return "Weather conditions look fairly normal and stable for the next couple of days."

    elif domain == "crop":
        if "root" in rec_lower or "halt" in rec_lower:
            return "Very wet soil may be affecting the roots, so the plant may not simply need more water."
        elif "spot" in rec_lower or "fungal" in rec_lower or "blight" in rec_lower:
            return "Leaf marks can have different causes. A clear photo or local expert can help identify them."
        elif "nitrogen" in rec_lower or "chlorosis" in rec_lower:
            return "Yellow leaves can have several causes. Check the soil before adding fertilizer."
        else:
            return "The leaves show stress; let's check recovery during cooler evening hours."

    elif domain == "risk":
        if "halt" in rec_lower or "critical" in rec_lower or "emergency" in rec_lower:
            return "Caution: extra water can harm roots if the soil is already very wet."
        elif "severe rainfall" in rec_lower or "storm" in rec_lower:
            return "Check local weather before watering. More water may cause problems if heavy rain is coming."
        elif "fertilizer" in rec_lower:
            return "Do not add fertilizer or spray chemicals until you know what the problem is."
        else:
            return "I am checking that the advice will not harm the plants."

    return rec[:120]


def _simple_final_decision(decision: str) -> str:
    if "halt" in decision:
        return "Do not water now. Let extra water drain, then check the soil again."
    if "delay" in decision or "rain" in decision:
        return "Wait before watering. Check your local weather and soil again soon."
    if "irrigate" in decision or "rehydrate" in decision:
        return "Water once during the cool part of the day, then check the soil again."
    if "nitrogen" in decision:
        return "Check the soil or ask a local farm expert before adding fertilizer."
    if "isolate" in decision or "fungal" in decision or "blight" in decision:
        return "Take a clear photo of the leaves and ask a local farm expert before spraying."
    return "Keep watching the plant and check the soil before changing how you water."


def _simple_final_decision_key(decision: str) -> str:
    if "halt" in decision:
        return "stop_water"
    if "delay" in decision or "rain" in decision:
        return "wait_rain"
    if "irrigate" in decision or "rehydrate" in decision:
        return "water_once"
    if "nitrogen" in decision:
        return "check_yellow"
    if "isolate" in decision or "fungal" in decision or "blight" in decision:
        return "leaf_issue"
    return "monitor"
