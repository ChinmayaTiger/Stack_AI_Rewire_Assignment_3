"""Task 4: Execute the generated pipeline against a scenario (G1-G3).

TODO: wire together
    get_spark -> read Silver Parquet -> generated transform -> write Gold Parquet
    (partitioned by billing_month) -> collect plan/metrics (Task 5)

Requirements:
  - scenario selectable via CLI arg (G1 | G2 | G3)
  - print/log row counts at each stage
  - exactly one row per (customer_id, plan_tier, billing_month)
  - the pipeline must be runnable with or without approved optimizations
    (so Task 8 before/after runs use the same entry point)
"""

import argparse

from src.spark_session import get_spark


def run(scenario: str, apply_optimizations: bool = False) -> dict:
    """TODO: run the pipeline; return run summary (rows in/out per stage, wall-clock, output path)."""
    raise NotImplementedError


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--scenario", default="G1", choices=["G1", "G2", "G3"])
    parser.add_argument("--apply-optimizations", action="store_true")
    args = parser.parse_args()
    # TODO: call run(...) and print the summary
    raise NotImplementedError


if __name__ == "__main__":
    main()
