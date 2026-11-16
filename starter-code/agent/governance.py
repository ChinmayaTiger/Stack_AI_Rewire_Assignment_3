"""Task 11: Governance - enforced IN CODE, not by prompting.

TODO: implement
  - validate_query(sql): read-only SELECT only (reject INSERT/UPDATE/DELETE/DROP/
    CREATE/ALTER/etc., multi-statements, comments used to smuggle writes)
  - enforce_table_access(sql): Gold tables/columns only (no Silver/Bronze)
  - check_min_group_size(sql_or_grouping): block queries whose groups fall below
    metrics.yaml's min_group_size (identity-exposure guard)
  - needs_human_approval(question, plan): ambiguous query (e.g. undefined time
    window) -> ask the user; if proceeding, state the assumption
  - log_event(question, sql, outcome, reason): append to logs/query_monitoring_log.md
    with outcome in {answered, blocked, escalated}
G4 must show BOTH the identity-exposing query and the write attempt as blocked, with reasons.
"""

from src import config

ALLOWED_TABLES: set[str] = set()  # TODO
ALLOWED_COLUMNS: dict[str, set[str]] = {}  # TODO (optional column-level control)


class GovernanceError(Exception):
    """Raised when a query is blocked. TODO: carry a reason string."""


def validate_query(sql: str) -> None:
    raise NotImplementedError


def enforce_table_access(sql: str) -> None:
    raise NotImplementedError


def check_min_group_size(sql: str) -> None:
    raise NotImplementedError


def needs_human_approval(question: str) -> tuple[bool, str]:
    raise NotImplementedError


def log_event(question: str, sql: str | None, outcome: str, reason: str = "") -> None:
    raise NotImplementedError
