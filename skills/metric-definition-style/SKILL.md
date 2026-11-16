---
name: metric_definition_style
description: Conventions for authoring business metric definitions in metrics.yaml so they are unambiguous, reviewable, and directly consumable by the pipeline, tests, and the NL query agent.
status: provided (use as-is)
---

# Metric Definition Style

## Purpose

`metrics.yaml` is the single source of truth for every business metric used
in the Gold revenue mart. This skill governs HOW a metric is written down so
that three different consumers -- the pipeline generator, the pytest suite,
and the NL query agent's `get_metric_spec` tool -- can all read the same
definition without reinterpretation.

## Required fields per metric

Every entry under `metrics:` must include:

- `description` -- one sentence, plain English, no Spark/SQL jargon.
- `formula` -- a SQL-like expression string. Prefer standard SQL functions
  (`SUM`, `LAG ... OVER (...)`, `CASE WHEN`) over prose. The formula must be
  literally transcribable into a Spark SQL expression or DataFrame operation
  without the author needing to guess intent.
- `grain` -- the exact column list the metric is computed at. If this differs
  from the mart's declared top-level `grain:`, say so explicitly and explain
  why (e.g. `prior_mrr` is at `[customer_id, billing_month]`, dropping
  `plan_tier`, because a tier change is exactly what the metric needs to see
  across).
- `depends_on` -- list of other metric names this one is computed from. Used
  to build the dependency chain / execution order; must form a DAG (no
  cycles). An empty list means "computed directly from source columns."
- `data_type` -- the target Spark/SQL type, so generated code and DQ checks
  agree on precision (e.g. money fields are always `decimal(12,2)`, never
  float, to avoid floating-point drift in waterfall reconciliation).

## Optional but encouraged

- `notes` -- edge cases a reader would otherwise have to infer (e.g. what a
  NULL `prior_mrr` means).
- `correction_log` -- REQUIRED whenever an AI-drafted version of this metric
  was corrected by a human. State what the AI got wrong, in one or two
  sentences, with enough specificity that a reviewer could reproduce the bug
  if the correction were reverted. This is the evidence trail Task 3 and the
  rubric's AI-validation criteria look for -- do not skip it just because the
  correction feels obvious in hindsight.

## Formula-writing rules

1. Never define a metric in terms of what a DataFrame column happens to be
   named in one particular implementation (e.g. don't write `mrr_col_v2`).
   Write it in terms of the stable business grain columns.
2. Prefer explicit `CASE WHEN ... ELSE 0 END` over relying on NULL-handling
   defaults -- a reviewer should be able to read the formula and know the
   zero/NULL behavior without running it.
3. If a metric requires surfacing rows that don't exist in the naive grouped
   output (e.g. `churned_mrr` needs customers with zero current-month
   invoices), say so in `notes`, don't leave it implicit -- the generator
   needs to know to build a scaffold/anti-join, not just a `GROUP BY`.
4. A metric's formula must be checkable by re-deriving it by hand on a small
   sample (Task 3 requires this for at least two metrics). If a formula can't
   reasonably be hand-verified in under five minutes on ~10 rows, it's
   probably too compound -- break it into an intermediate metric with its own
   entry and `depends_on` link.

## Data quality checks block

Each check under `data_quality_checks:` must specify `description`, `check`
(a human-readable predicate, not necessarily executable SQL -- the pytest
suite translates it), and `severity` (`fail` blocks the pipeline run from
being treated as valid output; `block` is specifically for governance checks
that must prevent a query result from being returned, as opposed to failing
a batch validation run).

## What this skill is NOT for

This skill does not cover HOW metrics get joined/grouped/windowed at the
Spark code level -- that's `transform_config_design`. It only covers how the
metric's business definition is written down.
