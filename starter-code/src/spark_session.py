"""Task 1: Reusable SparkSession factory.

Read .claude/skills/spark_conventions/SKILL.md first and MODIFY it for the
8 GB RAM / 4-core budget.

TODO: implement get_spark() so that:
  - settings (master, driver memory <= 5g, Kryo, shuffle.partitions, ...) are
    READ from the modified skill/conventions, not hard-coded inline
  - the returned session is local[4] and within budget
"""

from pyspark.sql import SparkSession

from . import config


def load_spark_settings(skill_path=config.SPARK_SKILL) -> dict:
    """TODO: parse the settings block from the modified spark_conventions skill."""
    raise NotImplementedError


def get_spark(app_name: str = "gold-layer") -> SparkSession:
    """TODO: build and return the SparkSession using load_spark_settings()."""
    raise NotImplementedError
