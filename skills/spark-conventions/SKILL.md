---
name: spark_conventions
description: Spark session configuration conventions for this assignment's fixed 8 GB RAM / 4-core single-machine hardware budget.
status: MODIFIED by learner for Task 1 (original provided version did not specify local-mode memory, shuffle-partition, or serializer settings for this hardware profile)
---

# Spark Conventions (8 GB RAM / 4 cores, local mode)

## Modification log (Task 1 requirement)

The originally provided version of this skill described general Spark best
practices without committing to concrete values for a constrained
single-machine budget. It has been modified to specify exact, justified
values for this assignment's fixed hardware profile (8 GB RAM, 4 CPU cores,
`local[4]`), because "review and modify if it doesn't already specify
local-mode settings suited to that constraint" was a required, not optional,
step.

## Required SparkSession configuration

| Config | Value | Why |
| --- | --- | --- |
| `spark.master` | `local[4]` | Matches the fixed 4-core budget exactly; do not request more threads than cores available. |
| `spark.driver.memory` | `5g` | Caps the driver (which in local mode also runs all executors) at 5 GB, leaving ~3 GB headroom for the OS/JVM overhead/collect() calls, out of the 8 GB total budget. |
| `spark.driver.maxResultSize` | `1g` | Prevents an accidental `collect()` of a large DataFrame from silently OOM-killing the driver; fail fast with a clear error instead. |
| `spark.serializer` | `org.apache.spark.serializer.KryoSerializer` | Lower memory and CPU overhead than Java serialization, meaningful at this RAM budget. |
| `spark.sql.shuffle.partitions` | `8` | NOT the 200 default. With `local[4]`, 200 partitions means heavy task-scheduling overhead relative to actual work per partition on a mart this size. Tune this explicitly per dataset volume (see "Scaling" below) rather than leaving the default. |
| `spark.default.parallelism` | `8` | Matches shuffle.partitions for consistency across RDD-level and DataFrame-level operations. |
| `spark.sql.parquet.compression.codec` | `snappy` | Required by the assignment; good balance of compression ratio vs. CPU cost at this core budget. |

## AQE (Adaptive Query Execution): disabled, deliberately

`spark.sql.adaptive.enabled = false` (and its sub-flags
`coalescePartitions.enabled`, `skewJoin.enabled`, also `false`).

This is a deliberate, documented departure from the usual "turn AQE on"
default recommendation, for three reasons specific to THIS assignment:

1. **Task 6 (skew detection) needs raw signal.** The whole point of
   `skew_detector.py` is to detect partition/task skew FROM OBSERVED RUNTIME
   METRICS, not to rely on Spark's own adaptive skew-join handling to quietly
   fix it first. If AQE is on, it may coalesce or re-plan around the exact
   skew Scenario G3 seeds, and the detector would have nothing left to find
   -- which defeats the grading intent of Task 6 (a real negative case AND a
   real positive case).
2. **Task 5/8 need a stable, reproducible plan for benchmarking.** AQE
   re-plans based on runtime statistics, so the physical plan (and partition
   count) between a "before" and "after" run of the same config can legally
   differ even without any pipeline change. Before/after benchmark
   comparisons in Task 8 are only meaningful if the only thing that changed
   between runs is the approved optimization -- not Spark's own
   non-deterministic adaptive behavior.
3. **Scale does not currently justify it.** AQE's main benefit (avoiding
   hand-tuned `shuffle.partitions` at large, unpredictable volume) is
   explicitly substituted here by the required metadata-driven,
   explicitly-tuned `shuffle.partitions` value above -- which is itself the
   point: a reviewable config value, not an opaque runtime decision.

**When you WOULD turn AQE back on:** if you extend this pipeline past the
assignment's scope to a genuinely large, unpredictable production volume
(see Task 12's scaling-ceiling discussion), re-enabling AQE is a reasonable
production default. Do so as an explicit, documented config change -- and if
you still need the skew detector to work, keep a diagnostic run path with
AQE off (or collect metrics from pre-AQE-replan stages) so Task 6's module
still has raw partition-level signal to work from.

## Reading this skill programmatically

`src/spark_session.py` implements this table as the `SPARK_CONVENTIONS` dict.
If you change a value here, change it there too -- they must not drift.

## Scaling note

If row counts grow materially beyond the assignment's G2 volume,
`shuffle.partitions` should scale roughly with (total shuffle data size) /
(target ~128MB per partition), recomputed and re-documented here, not
guessed at runtime.
