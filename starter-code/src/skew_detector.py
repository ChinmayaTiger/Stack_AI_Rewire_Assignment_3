"""Task 6: Data-skew and bottleneck detection.

TODO: consume the Task 5 output and flag:
  (a) stages where task-duration variance exceeds a DOCUMENTED threshold
  (b) any spill event (memory/disk)
  (c) partitions whose row count exceeds a DOCUMENTED multiple of the stage median
Requirements:
  - thresholds live in named constants/config with a short justification
  - must flag the seeded skewed account in G3
  - must NOT flag the G1 baseline (real negative case)
  - output a structured skew report (JSON) usable by agent/optimization_agent.py
"""

from . import config

# TODO: document and justify these
DURATION_VARIANCE_THRESHOLD = None
PARTITION_SKEW_MULTIPLE = None


def load_run(path) -> dict:
    """TODO: load a persisted runtime-metrics record."""
    raise NotImplementedError


def detect_duration_variance(run: dict) -> list[dict]:
    """TODO: (a)"""
    raise NotImplementedError


def detect_spill(run: dict) -> list[dict]:
    """TODO: (b)"""
    raise NotImplementedError


def detect_partition_skew(run: dict) -> list[dict]:
    """TODO: (c)"""
    raise NotImplementedError


def build_skew_report(run: dict) -> dict:
    """TODO: combine (a)-(c) -> {'flagged': bool, 'findings': [...]}"""
    raise NotImplementedError
