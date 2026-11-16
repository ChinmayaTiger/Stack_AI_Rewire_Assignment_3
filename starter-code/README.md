# Gold Layer Transformation -- Tiger Retail Billing Revenue Mart

Metadata-driven PySpark Gold Layer pipeline producing a finance revenue mart
(MRR by plan tier, churn, upgrade/downgrade attribution) from Silver Layer
output, with AI-assisted performance optimization (human-approved) and a
governed natural-language query agent.

See `Helper Guide - Gold Layer.md` for the full skill-driven workflow and
`Stack AI Rewire - Data Engineering - Gold Layer - Evaluation Rubric.xlsx`
for scoring.

## Quickstart

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Task 1: ingest
python src/convert_csv_to_parquet.py --variant baseline

# Task 4: run the baseline pipeline (Scenario G1)
python src/run_pipeline.py --scenario G1

# Task 5: collect runtime metrics (run while the Spark UI is still up,
# or re-run with event logging + history server if you need it after the fact)
python src/metrics_collector.py --scenario G1

# Task 6: detect skew (try it against G1 -- should be clean -- then G3)
python src/skew_detector.py --metrics-file logs/runtime_metrics/metrics_G1_<ts>.json

# Task 7: AI optimization agent
python agent/optimization_agent.py --skew-report logs/runtime_metrics/skew_report_G3_<ts>.json

# Task 13: tests
pytest tests/ -v
```

## Data

`data/silver/` contains three starter CSVs (synthetic, seeded for
reproducibility) plus two invoice variants for Scenario exercises:

- `invoices.csv` -- baseline (~474 rows, Scenario G1).
- `invoices_growth_g2.csv` -- multi-year volume extension (~42k rows here as
  a runnable sample; re-run the generator with a higher `yr_offset` range to
  push into the millions the assignment describes for a true Scenario G2
  stress test on your own machine).
- `invoices_skew_g3.csv` -- same shape as baseline plus one seeded skewed
  account (`CUST0007`) with a disproportionate share of invoice rows, for
  Scenario G3.

Regenerate or rescale any of these with the data-generation script this
project shipped with (ask your assignment reviewer / Claude Code session
for `gen_data.py` if you need to regenerate it locally -- the logic is
straightforward: seeded random billing rows per customer per month, with an
optional skew multiplier on one account).

## Project structure

See Section 8 of the assignment doc for the required submission layout;
this repo already follows it.

## AQE

Adaptive Query Execution is disabled in `src/spark_session.py` /
`.claude/skills/spark_conventions/SKILL.md`. Short version: AQE's runtime
re-planning would mask the exact skew signal Task 6's detector needs to
catch, and would make Task 8's before/after benchmark non-reproducible.
Full rationale is in the skill file.
