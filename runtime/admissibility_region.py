"""Executable lawful-region model for Elyria Field Laws.

This module exposes the public mathematical spine:

    R = { z | A(z) >= 0, Phi(z) >= 0, U(z) = 1 }

where:
    A(z)   = admissibility field
    Phi(z) = remaining lawful capacity
    U(z)   = authority-validity

The point is not binary permission. The point is lawful continuation geometry.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import List


class RegionVerdict(str, Enum):
    INSIDE_R = "INSIDE_R"
    OUTSIDE_R = "OUTSIDE_R"
    PARTIAL_CAPACITY = "PARTIAL_CAPACITY"


@dataclass(frozen=True)
class ContinuationState:
    """A candidate state evaluated against lawful continuation geometry."""

    state_id: str
    admissibility: float
    available_capacity: float
    carried_burden: float
    authority_valid: bool

    @property
    def phi(self) -> float:
        """Remaining lawful capacity: Phi(x) = C(x) - M(x)."""

        return self.available_capacity - self.carried_burden


@dataclass(frozen=True)
class RegionReceipt:
    state_id: str
    verdict: RegionVerdict
    inside_R: bool
    admissibility: float
    phi: float
    authority_valid: bool
    reason: str
    rule_trace: List[str]


def evaluate_region(state: ContinuationState) -> RegionReceipt:
    """Evaluate whether state z is inside R.

    R = { z | A(z) >= 0, Phi(z) >= 0, U(z) = 1 }
    """

    trace: List[str] = [
        "region.object.present",
        f"A(z)={state.admissibility}",
        f"Phi(z)={state.phi}",
        f"U(z)={int(state.authority_valid)}",
    ]

    if not state.authority_valid:
        trace.append("outside_R.authority_invalid")
        return RegionReceipt(
            state_id=state.state_id,
            verdict=RegionVerdict.OUTSIDE_R,
            inside_R=False,
            admissibility=state.admissibility,
            phi=state.phi,
            authority_valid=state.authority_valid,
            reason="Authority-validity failed; state is outside lawful continuation region.",
            rule_trace=trace,
        )

    if state.admissibility < 0:
        trace.append("outside_R.admissibility_negative")
        return RegionReceipt(
            state_id=state.state_id,
            verdict=RegionVerdict.OUTSIDE_R,
            inside_R=False,
            admissibility=state.admissibility,
            phi=state.phi,
            authority_valid=state.authority_valid,
            reason="Admissibility is negative; state is outside lawful continuation region.",
            rule_trace=trace,
        )

    if state.phi < 0:
        trace.append("outside_R.capacity_negative")
        return RegionReceipt(
            state_id=state.state_id,
            verdict=RegionVerdict.OUTSIDE_R,
            inside_R=False,
            admissibility=state.admissibility,
            phi=state.phi,
            authority_valid=state.authority_valid,
            reason="Remaining lawful capacity is negative; basin cannot carry the proposed burden.",
            rule_trace=trace,
        )

    if state.phi == 0:
        trace.append("inside_R.capacity_boundary")
        return RegionReceipt(
            state_id=state.state_id,
            verdict=RegionVerdict.PARTIAL_CAPACITY,
            inside_R=True,
            admissibility=state.admissibility,
            phi=state.phi,
            authority_valid=state.authority_valid,
            reason="State is inside R at capacity boundary; no additional burden may be admitted without new capacity or transfer.",
            rule_trace=trace,
        )

    trace.append("inside_R.pass")
    return RegionReceipt(
        state_id=state.state_id,
        verdict=RegionVerdict.INSIDE_R,
        inside_R=True,
        admissibility=state.admissibility,
        phi=state.phi,
        authority_valid=state.authority_valid,
        reason="State satisfies A(z) >= 0, Phi(z) >= 0, and U(z) = 1.",
        rule_trace=trace,
    )
