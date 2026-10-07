"""
utils/helpers.py
Defines data structures, serialization models, and formatting utilities for FarmAgent.
Standardizes agent communication, debate processing, and the Defend stage report.
"""

import sys
from dataclasses import dataclass, field, asdict
from typing import List, Dict, Any, Optional

# Ensure Windows console supports UTF-8 / safe emojis
if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

@dataclass
class FarmContext:
    crop: str
    growth_stage: str = "Unknown"
    location: str = "Local Farm"
    soil_type: str = "Loam"
    symptoms: str = "None specified"
    soil_moisture: Optional[float] = None  # percentage
    recent_rainfall: Optional[float] = None  # mm
    weather_preset: str = "default"
    additional_info: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class AgentResponse:
    agent_name: str
    role: str
    recommendation: str
    confidence: str  # "Low", "Medium", "High"
    key_findings: List[str] = field(default_factory=list)
    supporting_evidence: List[str] = field(default_factory=list)
    likely_cause: Optional[str] = None
    possible_causes: List[str] = field(default_factory=list)
    uncertain_info: List[str] = field(default_factory=list)
    challenges_raised: List[str] = field(default_factory=list)
    urgency: str = "Normal"  # "Low", "Normal", "High", "Critical"

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class Disagreement:
    dimension: str
    agent_a: str
    position_a: str
    agent_b: str
    position_b: str
    core_conflict: str

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class RejectedAlternative:
    alternative: str
    advocated_by: str
    rejection_reason: str
    evidence_against: str

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class DebateOutcome:
    consensus_level: str  # "High Consensus", "Moderate Debate", "Sharp Conflict"
    disagreements: List[Disagreement] = field(default_factory=list)
    debate_synthesis: str = ""
    winning_recommendation: str = ""
    reasons_for_decision: List[str] = field(default_factory=list)
    rejected_alternatives: List[RejectedAlternative] = field(default_factory=list)
    confidence: str = "Medium"
    residual_risks: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class FarmDecisionReport:
    problem_summary: str
    observations: List[str]
    agent_opinions: Dict[str, AgentResponse]
    disagreements: List[Disagreement]
    debate_summary: str
    final_decision: str
    reasons_for_decision: List[str]
    rejected_alternatives: List[RejectedAlternative]
    confidence: str
    risks_and_uncertainty: List[str]
    recommended_next_steps: List[str]
    safety_disclaimer: str = (
        "SAFETY NOTICE: FarmAgent is an AI-powered agricultural decision-support system. "
        "It provides evidence-based analysis but does NOT replace qualified local agronomists, "
        "soil testing laboratories, or plant pathologists. Always verify pesticide, fertilizer, "
        "and disease treatments with local agricultural extension services before application."
    )

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        # Ensure nested dataclasses in agent_opinions are converted to dicts
        d["agent_opinions"] = {k: v.to_dict() if hasattr(v, "to_dict") else v for k, v in self.agent_opinions.items()}
        d["disagreements"] = [x.to_dict() if hasattr(x, "to_dict") else x for x in self.disagreements]
        d["rejected_alternatives"] = [x.to_dict() if hasattr(x, "to_dict") else x for x in self.rejected_alternatives]
        return d


def print_cli_banner():
    print("=" * 80)
    print(" 🌾 FarmAgent — AutoAgent 3D: DEVELOP • DEBATE • DEFEND")
    print(" Intelligent Multi-Agent Agricultural Decision Support System")
    print("=" * 80)


def print_cli_report(report: FarmDecisionReport):
    """Prints a beautiful, structured CLI summary of the 3D process."""
    print("\n" + "=" * 80)
    print(" 📋 PROBLEM OVERVIEW")
    print("=" * 80)
    print(f"Problem: {report.problem_summary}")
    print("\nKey Observations:")
    for obs in report.observations:
        print(f"  • {obs}")

    print("\n" + "=" * 80)
    print(" 🤖 DEVELOP: SPECIALIST AGENT PERSPECTIVES")
    print("=" * 80)
    for name, agent in report.agent_opinions.items():
        print(f"\n▶ [{agent.agent_name.upper()}] (Confidence: {agent.confidence}, Urgency: {agent.urgency})")
        print(f"  Recommendation: {agent.recommendation}")
        if agent.likely_cause:
            print(f"  Likely Cause: {agent.likely_cause}")
        if agent.possible_causes:
            print(f"  Possible Causes: {', '.join(agent.possible_causes)}")
        if agent.uncertain_info:
            print(f"  Uncertainty Note: {', '.join(agent.uncertain_info)}")
        if agent.challenges_raised:
            print("  Challenges / Caveats:")
            for ch in agent.challenges_raised:
                print(f"    - ⚠️ {ch}")
        if agent.supporting_evidence:
            print("  Evidence:")
            for ev in agent.supporting_evidence[:2]:
                print(f"    - {ev}")

    print("\n" + "=" * 80)
    print(" ⚔️ DEBATE: IDENTIFIED CONFLICTS & REASONING CLASHES")
    print("=" * 80)
    if report.disagreements:
        for idx, dis in enumerate(report.disagreements, 1):
            print(f"\nDisagreement #{idx} [{dis.dimension}]:")
            print(f"  • {dis.agent_a}: \"{dis.position_a}\"")
            print(f"  • {dis.agent_b}: \"{dis.position_b}\"")
            print(f"  ⚡ Core Clash: {dis.core_conflict}")
    else:
        print("\nAll specialist agents are in general consensus. No irreconcilable clashes.")

    print(f"\nDebate Summary:\n{report.debate_summary}")

    print("\n" + "=" * 80)
    print(" 🛡️ DEFEND: FINAL DECISION & DEFENSE")
    print("=" * 80)
    print(f"\n🎯 FINAL DECISION: {report.final_decision}")
    print(f"📊 CONFIDENCE LEVEL: {report.confidence.upper()}")

    print("\nWHY THIS DECISION (Supporting Arguments):")
    for r in report.reasons_for_decision:
        print(f"  ✅ {r}")

    if report.rejected_alternatives:
        print("\nALTERNATIVES REJECTED & WHY:")
        for alt in report.rejected_alternatives:
            print(f"  ❌ \"{alt.alternative}\" (advocated by {alt.advocated_by})")
            print(f"     Reason: {alt.rejection_reason}")
            print(f"     Evidence: {alt.evidence_against}")

    print("\nRISKS & UNCERTAINTIES NOTED:")
    for risk in report.risks_and_uncertainty:
        print(f"  ⚠️ {risk}")

    print("\nRECOMMENDED NEXT STEPS:")
    for step in report.recommended_next_steps:
        print(f"  👉 {step}")

    print("\n" + "-" * 80)
    print(f"{report.safety_disclaimer}")
    print("=" * 80 + "\n")
