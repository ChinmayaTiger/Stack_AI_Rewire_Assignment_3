"""Shared paths and constants. TODO: adjust to your layout; keep spark settings OUT of here
(they live in .claude/skills/spark_conventions/SKILL.md)."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

SILVER_DIR = ROOT / "data" / "silver"
GOLD_DIR = ROOT / "data" / "gold" / "revenue_mart"
TRANSFORM_CONFIG = ROOT / "spec" / "transform_config.yaml"
METRICS_SPEC = ROOT / "spec" / "metrics.yaml"
SPARK_SKILL = ROOT / ".claude" / "skills" / "spark_conventions" / "SKILL.md"
RUNTIME_METRICS_DIR = ROOT / "logs" / "runtime_metrics"
MONITORING_LOG = ROOT / "logs" / "query_monitoring_log.md"
ARTIFACTS_DIR = ROOT / "outputs" / "artifacts"

SCENARIOS = ["G1", "G2", "G3", "G4"]
# TODO: add paths to the G2/G3 synthetic growth datasets
