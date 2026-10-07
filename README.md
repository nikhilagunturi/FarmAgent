# 🌾 FarmAgent — AutoAgent 3D: DEVELOP • DEBATE • DEFEND

An intelligent, multi-agent agricultural decision-support assistant built in Python for the **AutoAgent 3D Challenge**. FarmAgent helps farmers make high-confidence, evidence-backed decisions regarding crop pathology, irrigation scheduling, meteorological risks, soil health, and farming hazards.

---

## 🏛️ Architecture Overview

FarmAgent implements a modular, debate-driven multi-agent architecture:

```
                    Farmer (Observation Intake)
                               ↓
              FarmAgent Coordinator (core/farm_agent.py)
                               ↓
  ┌───────────────────────────────────────────────────────────────┐
  │  DEVELOP: Independent Specialist Perspectives                 │
  │  ───────────────────────────────────────────                  │
  │  🌱 Crop Agent        (Crop growth, symptoms & pathogens)    │
  │  💧 Irrigation Agent  (Soil moisture balance & water need)   │
  │  🌦️ Weather Agent     (Forecasts, heat stress, rain alerts)  │
  │  🧪 Soil Agent        (Texture, estimated pH, NPK leaching)  │
  │  🛡️ Risk Agent        (Devil's Advocate, chemical cautions)  │
  └───────────────────────────────────────────────────────────────┘
                               ↓
                Debate Engine (core/debate_engine.py)
  ┌───────────────────────────────────────────────────────────────┐
  │  DEBATE: Cross-Examination & Clash Adjudication               │
  │  ──────────────────────────────────────────────               │
  │  • Identifies policy disagreements and conflicting data       │
  │  • Cross-examines supporting physical evidence                │
  │  • Weighs risks, irreversibility penalties & urgency         │
  │  • Adjudicates the winning strategy & rejects alternatives    │
  └───────────────────────────────────────────────────────────────┘
                               ↓
                    DEFEND: Structured Defense
  ┌───────────────────────────────────────────────────────────────┐
  │  • Synthesis of observations & specialist positions          │
  │  • Winning recommendation with explicit supporting arguments  │
  │  • Alternatives explicitly rejected with counter-evidence    │
  │  • Residual uncertainties and farmer next steps checklist     │
  └───────────────────────────────────────────────────────────────┘
```

---

## 📁 Repository Structure & File Guide

| File / Folder | Role & Description |
| :--- | :--- |
| [`agents/crop_agent.py`](agents/crop_agent.py | **Crop Specialist**: Evaluates crop vulnerability at each growth stage, analyzes foliar symptoms, and distinguishes strictly between *Likely Cause*, *Possible Causes*, and *Uncertain Information*. Never diagnoses with false certainty. |
| [`agents/irrigation_agent.py`](agents/irrigation_agent.py | **Hydrology Specialist**: Evaluates soil moisture balance, crop transpiration demands, and irrigation schedules. Recommends *irrigate now*, *irrigate lightly*, *delay irrigation*, or *check soil moisture first*. |
| [`agents/weather_agent.py`](agents/weather_agent.py | **Agrometeorology Specialist**: Analyzes temperature, rainfall forecast, humidity, and wind. Includes offline mock simulation presets and optional live OpenWeatherMap API support. |
| [`agents/soil_agent.py`](agents/soil_agent.py | **Pedology Specialist**: Evaluates soil texture, water retention thresholds, and nutrient leaching patterns (NPK). Insists on certified laboratory soil testing before chemical amendments. |
| [`agents/risk_agent.py`](agents/risk_agent.py | **Safety Auditor & Devil's Advocate**: Challenges other agents on over-irrigation, root anoxia, premature disease diagnosis, thermal leaf scorch, and fertilizer misuse. |
| [`core/debate_engine.py`](core/debate_engine.py | **Debate Engine**: Identifies policy clashes (e.g. Irrigation wanting water vs Weather warning of a 45mm storm), scores physical evidence, applies safety penalties, and constructs explicit alternative rejections. |
| [`core/llm_client.py`](core/llm_client.py | **Groq LLM Client**: Isolated adapter for ultra-fast LLaMA 3.3/3.1 inference on Groq. Automatically falls back to offline rule engine if no API key is supplied. |
| [`core/farm_agent.py`](core/farm_agent.py | **Master Coordinator**: Orchestrates the 3D pipeline (Develop, Debate, Defend) and synthesizes the final actionable report. |
| [`data/mock_data.py`](data/mock_data.py | Mock agronomic profiles for crops, soils, weather presets, and the 5 benchmark test scenarios. Enables 100% offline functionality. |
| [`utils/helpers.py`](utils/helpers.py | Structured dataclasses (`FarmContext`, `AgentResponse`, `Disagreement`, `FarmDecisionReport`) and UTF-8 console output formatters. |
| [`app.py`](../app.py | Flask web server exposing the interactive web UI, Groq key manager, and REST API (`/api/analyze`, `/api/scenarios`, `/api/status`, `/api/set-groq-key`). |
| [`main.py`](../main.py | CLI runner for running any of the 5 benchmark scenarios or batch-testing all scenarios. |
| [`templates/index.html`](templates/index.html | Mobile-friendly farmer intake with visual choices, optional photo/location, language selection, demos, and simple results. |
| [`static/style.css`](static/style.css | Responsive, high-contrast touch UI for the farmer-first intake and recommendation flow. |
| [`static/app.js`](static/app.js | Regional UI language selection, demo scenarios, API communication, and farmer-friendly result rendering. |
| [`requirements.txt`](../requirements.txt | Lightweight dependencies: `flask`, `requests`, `python-dotenv`, `pydantic`. |
| [`.env.example`](../.env.example | Template for optional environment variables (port, optional weather API key). |

---

## 🎯 5 Benchmark Demo Scenarios

The system includes 5 pre-configured scenarios designed to test agent consensus versus sharp debates:

1. **Scenario 1: Tomato Wilting + Low Soil Moisture (High Consensus)**
   - *Dynamics*: Drought stress under high heat (34°C) with low soil moisture (14%). All agents agree on urgent morning irrigation; Risk Agent cautions against midday thermal shock.
2. **Scenario 2: Tomato Wilting + Impending Heavy Rain (Sharp Clash!)**
   - *Dynamics*: Plants are wilting and soil feels dry, prompting an initial instinct to irrigate. However, Weather Agent projects a 45mm severe storm within hours. The Debate Engine adjudicates the clash, overruling immediate irrigation to prevent severe waterlogging.
3. **Scenario 3: Yellow Leaves on Corn (Nutrient vs Leaching Debate)**
   - *Dynamics*: Basal leaves yellowing along the midrib. Soil Agent suspects nitrogen leaching from prior rains. Risk Agent challenges uncalibrated chemical fertilizer application without pH/EC testing.
4. **Scenario 4: Crop Disease Symptoms with Diagnostic Uncertainty**
   - *Dynamics*: Foliar spots with white sporulation on potato leaves. Crop Agent refuses to fabricate a definitive diagnosis, categorizing Late Blight as likely and Early Blight as possible. Risk Agent rejects chemical fungicides until extension confirmation.
5. **Scenario 5: Excessive Soil Moisture & Root Rot (Emergency Irrigation Halt)**
   - *Dynamics*: Plants wilting despite saturated clay soil (52% moisture). Crop and Risk agents identify root suffocation and Pythium/Phytophthora root rot. Irrigation is halted immediately.

---

## 💻 How to Run Locally

### 1. Requirements & Setup
Ensure Python 3.10+ is installed:
```powershell
# From the project root directory
py -m pip install -r requirements.txt
```

### ⚡ 2. Optional: Configure Groq API Key
You can empower the multi-agent debate synthesis with ultra-fast LLaMA models via Groq:

- Configure it on the server in [`.env`](../.env:
  ```ini
  GROQ_API_KEY=gsk_your_groq_api_key_here
  GROQ_MODEL=llama-3.3-70b-versatile
  ```

*(If no key is configured, FarmAgent transparently operates in 100% offline rule & heuristic reasoning mode!)*
Do not enter or expose API keys in the farmer-facing interface.

### 3. Run via Command Line Interface (CLI)
You can test any specific scenario or all 5 scenarios directly in your terminal:

```powershell
# Run Scenario 2 (Sharp Conflict / Debate Demo)
py main.py 2

# Run Scenario 1 (Consensus Demo)
py main.py 1

# Run all 5 scenarios sequentially
py main.py all
```

### 4. Run the Modern Web Dashboard
Start the local web server:
```powershell
py app.py
```
Then open your web browser to:
**`http://127.0.0.1:5000`**

- Choose a language from the top-right menu. The selection is saved in this browser.
- Describe observations using the crop/problem buttons and simple soil-feel choices.
- Try one of the one-click sample scenarios. Demo weather is marked as sample data, not a live reading.
- Photos are not uploaded or analyzed yet; sharing location is optional.
- Expand **More details (optional)** only when you already know those details.
- Read the plain-language recommendation first; expand **Agent debate** for simplified agent views.

Live Demo:- https://github.com/nikhilagunturi/FarmAgent

---

## 🛡️ Agricultural Safety Notice

FarmAgent is an AI-powered agricultural decision-support tool designed for informational guidance. It does **not** replace certified local agronomists, soil testing laboratories, or plant pathologists. Always consult regional agricultural extension services before applying regulated chemical pesticides or fertilizers.

## Deploying to Render

This repository includes a Render Blueprint (`render.yaml`). To publish the app:

1. Create a Git repository for this project and push it to a GitHub repository you control. The `.gitignore` file excludes `.env`, virtual environments, and Python cache files; verify that `.env` is not staged before pushing.
2. In Render, choose **New → Blueprint** and connect the GitHub repository.
3. Review the Blueprint and create the web service. Render builds with `pip install -r requirements.txt`, starts the app with Gunicorn, and checks `/api/health`.
4. After the first deploy completes, Render provides a public `*.onrender.com` URL. Add `GROQ_API_KEY` through the service’s Environment settings if you want Groq-backed responses; the app also runs in offline mode without it. Never add the key to `render.yaml` or Git.

The free web-service plan may spin down after inactivity, so the first request after a quiet period can take longer. See [Render’s free-plan limits](https://render.com/docs/free).

On Render, runtime key changes through /api/set-groq-key are disabled; configure provider keys in the service Environment settings instead.
