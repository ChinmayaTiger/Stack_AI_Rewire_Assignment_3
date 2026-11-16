"""Task 8 / Task 12: Benchmarking.

TODO: implement
  - before/after comparison for the SAME query: wall-clock, peak memory,
    shuffle read/write, spill volume -> outputs/artifacts/
  - honest reporting (include changes that did not help or made things worse)
  - benchmark suite: (a) CSV->Parquet throughput, (b) baseline on original volume,
    (c) baseline on G2 volume, (d) G3 before/after
  - an evidence-based row-count ceiling for the 8 GB / 4-core budget and
    what would need to change to scale further
"""

from . import config


def compare_runs(before_path, after_path) -> dict:
    """TODO: return deltas + verdict per metric."""
    raise NotImplementedError


def write_before_after_report(comparison: dict, out_path=config.ARTIFACTS_DIR / "g3_before_after.md") -> str:
    """TODO"""
    raise NotImplementedError


def run_benchmark_suite() -> dict:
    """TODO: (a)-(d) above."""
    raise NotImplementedError


def estimate_scaling_ceiling(results: dict) -> dict:
    """TODO: row-count ceiling + what to change to scale; cite measurements."""
    raise NotImplementedError
