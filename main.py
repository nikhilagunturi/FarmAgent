"""
main.py
CLI entrypoint for FarmAgent (AutoAgent 3D: DEVELOP • DEBATE • DEFEND).
Allows farmers or developers to run any of the 5 demo scenarios or interactive queries.
"""

import sys

if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

from utils.helpers import FarmContext, print_cli_banner, print_cli_report
from data.mock_data import DEMO_SCENARIOS
from core.farm_agent import FarmAgentCoordinator

def run_scenario(scenario_index: int):
    if scenario_index < 0 or scenario_index >= len(DEMO_SCENARIOS):
        print(f"Error: Scenario index {scenario_index} out of range (0-{len(DEMO_SCENARIOS)-1}).")
        return

    scenario = DEMO_SCENARIOS[scenario_index]
    inp = scenario["input"]

    print("\n" + "#" * 80)
    print(f"  RUNNING TEST SCENARIO {scenario_index + 1}: {scenario['title']}")
    print(f"  Description: {scenario['description']}")
    print(f"  Expected Dynamics: {scenario['expected_debate_dynamics']}")
    print("#" * 80)

    ctx = FarmContext(
        crop=inp.get("crop", "Tomato"),
        growth_stage=inp.get("growth_stage", "Flowering"),
        location=inp.get("location", "Valley Field"),
        soil_type=inp.get("soil_type", "Loam"),
        symptoms=inp.get("symptoms", "None"),
        soil_moisture=inp.get("soil_moisture"),
        recent_rainfall=inp.get("recent_rainfall"),
        weather_preset=inp.get("weather_preset", "default"),
        additional_info=inp.get("additional_info", "")
    )

    coordinator = FarmAgentCoordinator()
    report = coordinator.analyze(ctx)
    print_cli_report(report)


def run_all_scenarios():
    print_cli_banner()
    print("Testing all 5 benchmark scenarios for AutoAgent 3D...")
    for idx in range(len(DEMO_SCENARIOS)):
        run_scenario(idx)


def main():
    print_cli_banner()
    if len(sys.argv) > 1:
        arg = sys.argv[1].strip().lower()
        if arg == "all":
            run_all_scenarios()
            return
        elif arg.isdigit():
            scenario_num = int(arg)
            if 1 <= scenario_num <= len(DEMO_SCENARIOS):
                run_scenario(scenario_num - 1)
                return
            else:
                print(f"Please specify a scenario number between 1 and {len(DEMO_SCENARIOS)}.")
                return

    # Default: Run Scenario 2 (Sharp Conflict) and Scenario 1 (Consensus) or present menu
    print("Available Options:")
    print("  1. Run Scenario 1: Tomato Wilting + Drought (Consensus on Watering)")
    print("  2. Run Scenario 2: Tomato Wilting + Impending Torrential Rain (Sharp Agent Debate!)")
    print("  3. Run Scenario 3: Yellow Leaves on Corn (Nutrient vs Leaching Debate)")
    print("  4. Run Scenario 4: Crop Disease Spots with Diagnostic Uncertainty")
    print("  5. Run Scenario 5: Wilting in Saturated Soil (Root Rot Emergency)")
    print("  all. Run ALL 5 Scenarios sequentially")
    print("\nRunning Scenario 2 by default to demonstrate the multi-agent debate clash...\n")
    run_scenario(1)


if __name__ == "__main__":
    main()
