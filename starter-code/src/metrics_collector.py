"""Task 5: Execution-plan and runtime-metrics collector.

TODO: implement a collector that, for a given pipeline run, captures:
  - df.explain(mode="formatted") (logical/physical plan)
  - per-stage task-duration distribution
  - shuffle read/write bytes
  - spill (memory/disk) bytes
  via the Spark UI REST API (localhost:4040/api/v1) or a SparkListener
  (no manual screenshots), and persists a timestamped JSON/CSV per run to
  logs/runtime_metrics/ so runs can be compared.
"""

from pyspark.sql import DataFrame, SparkSession

from . import config


def capture_plan(df: DataFrame) -> str:
    """TODO: return df.explain(mode='formatted') as a string."""
    raise NotImplementedError


def fetch_stage_metrics(spark: SparkSession) -> list[dict]:
    """TODO: pull stage/task metrics (REST API or SparkListener)."""
    raise NotImplementedError


def summarize_task_durations(stage: dict) -> dict:
    """TODO: min/median/p95/max/stddev of task durations for a stage."""
    raise NotImplementedError


def collect_run(spark: SparkSession, df: DataFrame, scenario: str, label: str = "run") -> dict:
    """TODO: assemble the full run record (plan, stages, shuffle, spill, wall-clock, peak memory)."""
    raise NotImplementedError


def persist_run(record: dict, out_dir=config.RUNTIME_METRICS_DIR) -> str:
    """TODO: write <scenario>_<label>_<timestamp>.json; return the path."""
    raise NotImplementedError
