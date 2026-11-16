"""Task 2/4: Config-driven code generator.

Read .claude/skills/transform_config_design/SKILL.md (you author it in Task 2).

TODO: implement the generator so that:
  - it reads spec/transform_config.yaml and spec/metrics.yaml
  - it EMITS Spark code (e.g. to src/generated/gold_revenue_mart.py) - the config
    is the artifact engineers edit, never the emitted code
  - join types, broadcast hints, grain, and the ordered transformations are
    emitted faithfully (a LEFT join must never silently become INNER)
  - re-running after a config change picks it up with no manual patching
    (keep evidence of this for the deliverables)
"""

from . import config


def load_specs(config_path=config.TRANSFORM_CONFIG, metrics_path=config.METRICS_SPEC) -> tuple[dict, dict]:
    """TODO: load and validate both YAML files."""
    raise NotImplementedError


def render_joins(cfg: dict) -> str:
    """TODO: emit join code from cfg['joins'] (incl. broadcast hints)."""
    raise NotImplementedError


def render_transformations(cfg: dict, metrics: dict) -> str:
    """TODO: emit ordered transformation code."""
    raise NotImplementedError


def generate(output_path) -> str:
    """TODO: assemble and write the generated module; return its path."""
    raise NotImplementedError


def verify_generated_matches_config(generated_path, cfg: dict) -> list[str]:
    """TODO: return a list of mismatches (join types, grain keys, formulas); [] if faithful."""
    raise NotImplementedError


if __name__ == "__main__":
    generate("src/generated/gold_revenue_mart.py")
