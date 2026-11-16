"""Task 10/11: Natural-language query agent over the Gold Parquet output.

Read .claude/skills/nl_query_agent/SKILL.md (you author it in Task 10).

TODO: implement a tool-use loop (Anthropic API) that
  - ALWAYS calls get_metric_spec before querying a named metric
  - calls validate_grain before returning results for a non-standard grouping
  - routes every run_sql through agent.governance (read-only, gold-only, min group size)
  - asks the user when a question is ambiguous (human approval/escalation)
  - always shows the SQL it executed in the final answer
  - logs every question/SQL/outcome via governance.log_event
"""

from agent import governance, tools


SYSTEM_PROMPT = """TODO: concise system prompt. Governance is enforced in code - do not rely on this prompt for safety."""


def answer(question: str) -> dict:
    """TODO: run the loop; return {'answer': str, 'sql': str | None, 'outcome': str}."""
    raise NotImplementedError


def main():
    """TODO: simple CLI loop; include the G4 demo questions (identity-exposing + write attempt)."""
    raise NotImplementedError


if __name__ == "__main__":
    main()
