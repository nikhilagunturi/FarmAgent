"""
app.py
Flask web application for FarmAgent (AutoAgent 3D: DEVELOP • DEBATE • DEFEND).
Provides both an interactive web dashboard and REST API endpoints for agricultural multi-agent analysis.
"""

import os
from flask import Flask, render_template, request, jsonify
from utils.helpers import FarmContext
from utils.farmer_adapter import parse_farmer_input, create_farmer_view
from data.mock_data import DEMO_SCENARIOS
from core.farm_agent import FarmAgentCoordinator

app = Flask(__name__, template_folder="templates", static_folder="static")

coordinator = FarmAgentCoordinator()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/scenarios", methods=["GET"])
def get_scenarios():
    """Returns the 5 pre-configured demo scenarios."""
    return jsonify({
        "status": "success",
        "scenarios": DEMO_SCENARIOS
    })

@app.route("/api/analyze", methods=["POST"])
def analyze_farm_problem():
    """
    Analyzes farmer input through FarmAgent's 3D pipeline:
    DEVELOP (Specialist agents) -> DEBATE (Clash adjudication) -> DEFEND (Final decision & rationale)
    Produces both a farmer-friendly plain-language view and full technical report.
    """
    try:
        data = request.get_json() or {}

        # Parse simple observations into multi-agent context
        ctx = parse_farmer_input(data)

        # Run multi-agent pipeline: DEVELOP -> DEBATE -> DEFEND
        report = coordinator.analyze(ctx)

        # Generate simplified, compassionate farmer response
        farmer_view = create_farmer_view(report, data, coordinator.debate_engine.llm_client)

        return jsonify({
            "status": "success",
            "report": report.to_dict(),
            "farmer_view": farmer_view
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "service": "FarmAgent 3D Engine"})

@app.route("/api/status", methods=["GET"])
def get_status():
    """Returns AI engine status and active Groq model."""
    llm = coordinator.debate_engine.llm_client
    return jsonify({
        "status": "success",
        "groq_enabled": llm.is_enabled(),
        "model": llm.get_model_name(),
        "has_api_key": bool(llm.api_key)
    })

@app.route("/api/set-groq-key", methods=["POST"])
def set_groq_key():
    """Dynamically sets or updates the Groq API key."""
    if os.getenv("RENDER", "").lower() == "true":
        return jsonify({
            "status": "error",
            "message": "Runtime API-key updates are disabled on hosted deployments. Configure GROQ_API_KEY in the hosting environment settings."
        }), 403

    data = request.get_json() or {}
    key = data.get("api_key", "").strip()
    model = data.get("model", "llama-3.3-70b-versatile").strip()

    llm = coordinator.debate_engine.llm_client
    success, message = llm.set_api_key(key, model)

    if success:
        # Also update .env file if it exists so key persists
        try:
            env_path = os.path.join(os.path.dirname(__file__), ".env")
            lines = []
            if os.path.exists(env_path):
                with open(env_path, "r", encoding="utf-8") as f:
                    for line in f:
                        if line.startswith("GROQ_API_KEY="):
                            continue
                        if line.startswith("GROQ_MODEL="):
                            continue
                        lines.append(line)
            lines.insert(0, f"GROQ_API_KEY={key}\nGROQ_MODEL={model}\n")
            with open(env_path, "w", encoding="utf-8") as f:
                f.writelines(lines)
        except Exception as e:
            print(f"[app.py] Note: Could not write key to .env: {e}")

        return jsonify({
            "status": "success",
            "message": message,
            "groq_enabled": llm.is_enabled(),
            "model": llm.get_model_name()
        })
    else:
        return jsonify({
            "status": "error",
            "message": message
        }), 400

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    print(f"🌾 FarmAgent Server starting on http://127.0.0.1:{port}")
    app.run(host="0.0.0.0", port=port, debug=False)
