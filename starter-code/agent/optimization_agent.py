"""Task 7/8: AI optimization agent.

Read .claude/skills/optimization_agent/SKILL.md (you author it in Task 7).

TODO: implement an agent that
  - takes (execution plan, runtime metrics, skew report) as input
  - uses the Anthropic API to produce a STRUCTURED report ranking 2-4 candidate
    optimizations, each with: proposed change, rationale citing a specific
    observed metric, expected impact, risk/tradeoff
  - NEVER applies a change itself
  - rejects/flags any recommendation with no supporting metric
Human approval gate (Task 8):
  - record approve/reject + one-line reason for EVERY recommendation
  - only approved changes are applied (to config/code, by the human)
"""

from . import __name__ as _pkg  # noqa: F401


def build_prompt(plan: str, metrics: dict, skew_report: dict) -> str:
    """TODO"""
    raise NotImplementedError


def get_recommendations(plan: str, metrics: dict, skew_report: dict) -> list[dict]:
    """TODO: return ranked list of recommendations (structured)."""
    raise NotImplementedError


def validate_recommendation(rec: dict, metrics: dict) -> dict:
    """TODO: check the cited metric actually exists and supports the claim."""
    raise NotImplementedError


def record_decision(rec_id: str, decision: str, reason: str, path="outputs/artifacts/approval_record.md") -> None:
    """TODO: decision in {'approved', 'rejected'}; reason is required (one line)."""
    raise NotImplementedError


def write_report(recs: list[dict], out_path="outputs/artifacts/g3_recommendation_report.md") -> str:
    """TODO"""
    raise NotImplementedError
