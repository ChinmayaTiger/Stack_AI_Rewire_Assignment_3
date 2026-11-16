# CLAUDE.md

Project-level instructions for Claude Code working in this repo.

## What this project is

A metadata-driven PySpark Gold Layer pipeline that builds a finance revenue
mart (`gold_revenue_mart`) from Silver Layer output, plus an AI optimization
agent, a governed natural-language query agent, and a pytest validation
suite. See the assignment doc and `Helper Guide - Gold Layer.md` for full
context.

## Hardware constraint (non-negotiable)

All Spark execution runs local-only: `local[4]`, `spark.driver.memory=5g`.
Never suggest a cluster config, `local[*]`, or a driver memory above 5g for
this assignment's pipeline code.

## Source-of-truth files -- edit these, not generated code

- `spec/transform_config.yaml` -- sources, joins, grain, transformation order.
- `spec/metrics.yaml` -- every metric's formula, grain, dependencies, DQ checks.

When asked to change a metric's business logic or a join's shape, edit these
YAML files first and regenerate via `src/generator.py`. Do not hand-patch
generated Spark code to work around a config gap -- extend the config schema
instead (see `.claude/skills/transform_config_design/SKILL.md`).

## Skill-driven workflow

Before implementing anything under Tasks 1, 2, 7, or 10, read the matching
`.claude/skills/<name>/SKILL.md` first. Skills in this repo:

- `metric_definition_style` -- provided, use as-is.
- `spark_conventions` -- modified for this hardware budget; also documents
  why AQE is disabled.
- `transform_config_design`, `optimization_agent`, `nl_query_agent` --
  authored for this project; read before touching the matching module.

Record any skill gap you find, and how you addressed it, in
`logs/ai_interaction_log.md`.

## Testing

Run `pytest tests/` before considering any change complete. The suite
validates grain uniqueness, waterfall reconciliation, reconciliation-to-
silver, skew-detection true/false cases, agent governance, and a benchmark-
regression assertion.

## Conventions

- Python, PySpark DataFrame/SQL API (no RDD-level code unless unavoidable).
- All config in YAML under `spec/`; no metric formulas or join logic
  hand-coded inline in `src/` beyond what the generator needs to interpret
  config generically.
- Money values: `decimal(12,2)`, never float, to avoid rounding drift in
  waterfall reconciliation checks.
- Every AI-generated code change or AI-proposed optimization must be
  reviewed and explicitly approved/rejected by a human before being applied
  (see `logs/ai_interaction_log.md`).
