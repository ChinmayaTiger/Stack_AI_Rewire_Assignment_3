"""Task 10: Tools for the NL query agent.

TODO: implement the four tools + their Anthropic tool-use JSON schemas:
  - get_metric_spec(metric_name)   -> definition from spec/metrics.yaml
  - get_schema(table_name)         -> columns/types of an ALLOWED gold table
  - run_sql(sql)                   -> executes ONLY after governance checks pass
  - validate_grain(group_by_cols)  -> checks a non-standard grouping against
                                      the gold grain and min group size
Engine choice: Spark SQL, or DuckDB if you justify it against the assignment's
Section 5 requirement (write the justification in README.md).
"""

TOOL_SCHEMAS: list[dict] = []  # TODO: Anthropic tool definitions


def get_metric_spec(metric_name: str) -> dict:
    raise NotImplementedError


def get_schema(table_name: str) -> dict:
    raise NotImplementedError


def run_sql(sql: str) -> dict:
    """TODO: must call governance.validate_query() first; return rows + executed SQL."""
    raise NotImplementedError


def validate_grain(group_by_cols: list[str]) -> dict:
    raise NotImplementedError


def dispatch(tool_name: str, tool_input: dict) -> dict:
    """TODO: route tool calls."""
    raise NotImplementedError
