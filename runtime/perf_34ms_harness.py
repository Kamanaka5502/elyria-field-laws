"""Performance harness for the 34 ms hot-path corridor.

This harness measures local execution timing for the 34 ms contract. It does not
replace the contract itself. The contract remains:

    fast when complete
    safe-path when uncertain
    replayable always

Use this harness to produce repeatable local timing samples for the hot path.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from statistics import mean, median
from time import perf_counter_ns
from typing import Dict, List

from runtime.hot_path_34ms import (
    STAGE_BUDGET_MS,
    TARGET_TOTAL_MS,
    HotPathInput,
    resolve_hot_path,
)


NANOSECONDS_PER_MS = 1_000_000


@dataclass(frozen=True)
class PerfSummary:
    iterations: int
    target_total_ms: int
    budget_total_ms: int
    min_ms: float
    mean_ms: float
    median_ms: float
    max_ms: float
    p95_ms: float
    pass_target: bool
    verdict_counts: Dict[str, int]


def valid_hot_input() -> HotPathInput:
    """Return a complete, current, hot-path eligible input."""

    return HotPathInput(
        event_id="EV-PERF-34MS",
        envelope_id="ENV-PERF-34MS",
        movement_id="M-PERF-34MS",
        corridor_id="C-PERF-34MS",
        envelope_shape_known=True,
        movement_type_known=True,
        standing_refs_current=True,
        standing_ttl_ms=100,
        standing_age_ms=10,
        field_state_hash_available=True,
        field_hash_before="hash-field",
        field_hash_after="hash-field",
        protected_effect_mapped=True,
        law_version_current=True,
        replay_material_present=True,
        prior_receipt_hash_matches=True,
        changed_condition_pending=False,
        route_or_transfer_ambiguity=False,
        capacity_boundary_reached=False,
        hard_gates_pass=True,
        inside_lawful_region=True,
        protected_effect_formed=True,
        measured_stage_latency_ms={stage: float(ms) for stage, ms in STAGE_BUDGET_MS.items()},
    )


def _percentile(values: List[float], pct: float) -> float:
    if not values:
        return 0.0
    sorted_values = sorted(values)
    index = int(round((pct / 100.0) * (len(sorted_values) - 1)))
    return sorted_values[index]


def run_perf(iterations: int = 1000) -> PerfSummary:
    """Run repeated local hot-path resolution measurements."""

    if iterations <= 0:
        raise ValueError("iterations must be positive")

    samples_ms: List[float] = []
    verdict_counts: Dict[str, int] = {}
    hot = valid_hot_input()

    for _ in range(iterations):
        started = perf_counter_ns()
        receipt = resolve_hot_path(hot)
        finished = perf_counter_ns()

        elapsed_ms = (finished - started) / NANOSECONDS_PER_MS
        samples_ms.append(elapsed_ms)
        verdict_counts[receipt.verdict.value] = verdict_counts.get(receipt.verdict.value, 0) + 1

    return PerfSummary(
        iterations=iterations,
        target_total_ms=TARGET_TOTAL_MS,
        budget_total_ms=sum(STAGE_BUDGET_MS.values()),
        min_ms=min(samples_ms),
        mean_ms=mean(samples_ms),
        median_ms=median(samples_ms),
        max_ms=max(samples_ms),
        p95_ms=_percentile(samples_ms, 95),
        pass_target=max(samples_ms) <= TARGET_TOTAL_MS,
        verdict_counts=verdict_counts,
    )


def main() -> None:
    summary = run_perf()
    for key, value in asdict(summary).items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
