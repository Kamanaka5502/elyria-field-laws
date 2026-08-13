#!/usr/bin/env python3
"""Elyria Field Laws — admissible performance benchmark harness.

The harness converts a performance assertion into a replayable proof object.
It does not decide general system admissibility; it validates benchmark
conditions and emits a structured performance receipt.
"""

from __future__ import annotations

import hashlib
import json
import statistics
import time
from dataclasses import dataclass
from typing import Any, Callable, Dict, Iterable, List, Mapping, Sequence


@dataclass(frozen=True)
class BenchmarkSpec:
    metric: str
    semantic_dimension: int | str
    target_dimension: int | str
    policy_hash: str
    runs: int = 30
    maximum_relative_spread: float = 1.0

    def validate(self) -> None:
        if self.metric != "latency":
            raise ValueError("This harness currently proves latency only")
        if self.runs < 2:
            raise ValueError("runs must be >= 2")
        if not self.policy_hash:
            raise ValueError("policy_hash is required")
        if self.maximum_relative_spread < 0:
            raise ValueError("maximum_relative_spread must be >= 0")


@dataclass(frozen=True)
class TrialResult:
    latency_seconds: float
    result: Any
    valid: bool
    chi: float
    pass_count: int


class BenchmarkHarness:
    """Deterministic benchmark protocol for baseline/new-system comparison."""

    def __init__(
        self,
        baseline: Any,
        system: Any,
        spec: BenchmarkSpec,
        carryability: Callable[[Any, Mapping[str, Any]], float],
        bindable: Callable[[Any], bool],
    ) -> None:
        self.baseline = baseline
        self.system = system
        self.spec = spec
        self.carryability = carryability
        self.bindable = bindable
        self.spec.validate()

    def validate_constraint_field(
        self,
        baseline_context: Mapping[str, Any],
        system_context: Mapping[str, Any],
    ) -> None:
        for key in ("semantic_dimension", "target_dimension", "policy_hash"):
            if baseline_context.get(key) != system_context.get(key):
                raise ValueError(f"constraint field mismatch: {key}")

        if baseline_context.get("semantic_dimension") != self.spec.semantic_dimension:
            raise ValueError("baseline semantic dimension differs from spec")
        if baseline_context.get("target_dimension") != self.spec.target_dimension:
            raise ValueError("baseline target dimension differs from spec")
        if baseline_context.get("policy_hash") != self.spec.policy_hash:
            raise ValueError("baseline policy hash differs from spec")

    def run_trial(
        self,
        engine: Any,
        input_case: Any,
        context: Mapping[str, Any],
    ) -> TrialResult:
        start = time.perf_counter_ns()
        result = engine.execute(input_case, context)
        end = time.perf_counter_ns()

        latency_seconds = (end - start) / 1_000_000_000.0
        is_valid = self.bindable(result)
        chi = self.carryability(result, context)

        # Single-pass means exactly one uninterrupted execute call per trial.
        return TrialResult(
            latency_seconds=latency_seconds,
            result=result,
            valid=is_valid,
            chi=chi,
            pass_count=1,
        )

    def collect_trials(
        self,
        engine: Any,
        input_cases: Iterable[Any],
        context: Mapping[str, Any],
    ) -> List[TrialResult]:
        trials: List[TrialResult] = []
        for case in input_cases:
            for _ in range(self.spec.runs):
                trials.append(self.run_trial(engine, case, context))
        return trials

    @staticmethod
    def _relative_spread(values: Sequence[float]) -> float:
        if not values:
            return float("inf")
        med = statistics.median(values)
        if med == 0:
            return 0.0 if max(values) == 0 else float("inf")
        return (max(values) - min(values)) / med

    def evaluate(
        self,
        baseline_trials: Sequence[TrialResult],
        system_trials: Sequence[TrialResult],
    ) -> Dict[str, Any]:
        for name, trials in (("baseline", baseline_trials), ("new_system", system_trials)):
            if not trials:
                raise ValueError(f"no trials collected for {name}")
            if any(t.pass_count != 1 for t in trials):
                raise ValueError(f"{name} violated single-pass requirement")
            if any(t.chi <= 0 for t in trials):
                raise ValueError(f"{name} failed carryability: chi <= 0")
            if any(not t.valid for t in trials):
                raise ValueError(f"{name} produced a non-bindable result")

        baseline_latency = [t.latency_seconds for t in baseline_trials]
        system_latency = [t.latency_seconds for t in system_trials]

        baseline_median = statistics.median(baseline_latency)
        system_median = statistics.median(system_latency)

        if system_median <= 0 or baseline_median <= 0:
            raise ValueError("latency medians must be positive")

        factor = baseline_median / system_median

        baseline_spread = self._relative_spread(baseline_latency)
        system_spread = self._relative_spread(system_latency)

        if baseline_spread > self.spec.maximum_relative_spread:
            raise ValueError("baseline variance exceeds configured bound")
        if system_spread > self.spec.maximum_relative_spread:
            raise ValueError("new-system variance exceeds configured bound")

        return {
            "claim_type": "performance",
            "metric": self.spec.metric,
            "baseline_value": baseline_median,
            "new_value": system_median,
            "factor": factor,
            "semantic_dimension": self.spec.semantic_dimension,
            "target_dimension": self.spec.target_dimension,
            "carryability_status": "POSITIVE",
            "runs": self.spec.runs,
            "baseline_variance": baseline_spread,
            "new_system_variance": system_spread,
            "policy_hash": self.spec.policy_hash,
            "single_pass": True,
        }

    @staticmethod
    def canonical_json_bytes(value: Mapping[str, Any]) -> bytes:
        return json.dumps(
            value,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
        ).encode("utf-8")

    def receipt_hash(self, receipt: Mapping[str, Any]) -> str:
        return hashlib.sha256(self.canonical_json_bytes(receipt)).hexdigest()

    def run(
        self,
        input_cases: Iterable[Any],
        baseline_context: Mapping[str, Any],
        system_context: Mapping[str, Any],
    ) -> Dict[str, Any]:
        self.validate_constraint_field(baseline_context, system_context)

        baseline_trials = self.collect_trials(
            self.baseline,
            input_cases,
            baseline_context,
        )
        system_trials = self.collect_trials(
            self.system,
            input_cases,
            system_context,
        )

        receipt = self.evaluate(baseline_trials, system_trials)
        receipt["verification_hash"] = self.receipt_hash(receipt)
        return receipt
