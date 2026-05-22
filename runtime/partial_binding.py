"""Partial binding model for Elyria Field Laws.

Partial binding is not compromise.
Partial binding is capacity-bounded consequence admission.

The field may admit only what it can carry. Everything else remains non-binding.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import List, Optional


class PartialDecision(str, Enum):
    ALLOW_FULL = "ALLOW_FULL"
    ALLOW_PARTIAL = "ALLOW_PARTIAL"
    REFUSE = "REFUSE"


@dataclass(frozen=True)
class PartialMovement:
    movement_id: str
    q_total: float
    available_capacity: float
    carried_burden: float = 0.0
    authority_standing: bool = True
    lineage_integrity: bool = True
    evidence_freshness: bool = True
    consequence_admissibility: bool = True
    witness_replay_validity: bool = True
    sink_assignment: Optional[str] = None

    @property
    def phi(self) -> float:
        return self.available_capacity - self.carried_burden


@dataclass(frozen=True)
class PartialReceipt:
    movement_id: str
    decision: PartialDecision
    partial_bind_defined: bool
    q_total: float
    q_allowed: float
    q_refused: float
    capacity_before: float
    capacity_after: float
    sink_assignment: Optional[str]
    reason: str
    rule_trace: List[str]


def _hard_gates_pass(movement: PartialMovement) -> bool:
    return all(
        [
            movement.authority_standing,
            movement.lineage_integrity,
            movement.evidence_freshness,
            movement.consequence_admissibility,
            movement.witness_replay_validity,
        ]
    )


def resolve_partial(movement: PartialMovement) -> PartialReceipt:
    """Resolve a quantitative movement into full, partial, or refused consequence status."""

    trace: List[str] = [
        "partial.object.present",
        f"q_total={movement.q_total}",
        f"Phi(x)={movement.phi}",
    ]

    if movement.q_total <= 0:
        trace.append("refuse.non_positive_quantity")
        return PartialReceipt(
            movement_id=movement.movement_id,
            decision=PartialDecision.REFUSE,
            partial_bind_defined=False,
            q_total=movement.q_total,
            q_allowed=0.0,
            q_refused=movement.q_total,
            capacity_before=movement.phi,
            capacity_after=movement.phi,
            sink_assignment=movement.sink_assignment,
            reason="Proposed quantity must be positive.",
            rule_trace=trace,
        )

    if not _hard_gates_pass(movement):
        trace.append("refuse.hard_gate_failure")
        return PartialReceipt(
            movement_id=movement.movement_id,
            decision=PartialDecision.REFUSE,
            partial_bind_defined=False,
            q_total=movement.q_total,
            q_allowed=0.0,
            q_refused=movement.q_total,
            capacity_before=movement.phi,
            capacity_after=movement.phi,
            sink_assignment=movement.sink_assignment,
            reason="Non-compensable hard gate failure blocks partial binding.",
            rule_trace=trace,
        )

    if movement.phi <= 0:
        trace.append("refuse.no_remaining_capacity")
        return PartialReceipt(
            movement_id=movement.movement_id,
            decision=PartialDecision.REFUSE,
            partial_bind_defined=False,
            q_total=movement.q_total,
            q_allowed=0.0,
            q_refused=movement.q_total,
            capacity_before=movement.phi,
            capacity_after=movement.phi,
            sink_assignment=movement.sink_assignment,
            reason="No remaining lawful capacity is available.",
            rule_trace=trace,
        )

    if movement.phi >= movement.q_total:
        trace.append("allow_full.capacity_supports_total")
        return PartialReceipt(
            movement_id=movement.movement_id,
            decision=PartialDecision.ALLOW_FULL,
            partial_bind_defined=True,
            q_total=movement.q_total,
            q_allowed=movement.q_total,
            q_refused=0.0,
            capacity_before=movement.phi,
            capacity_after=movement.phi - movement.q_total,
            sink_assignment=movement.sink_assignment,
            reason="Full proposed quantity is capacity-supported.",
            rule_trace=trace,
        )

    trace.append("allow_partial.capacity_bounds_fraction")
    q_allowed = movement.phi
    q_refused = movement.q_total - q_allowed
    return PartialReceipt(
        movement_id=movement.movement_id,
        decision=PartialDecision.ALLOW_PARTIAL,
        partial_bind_defined=True,
        q_total=movement.q_total,
        q_allowed=q_allowed,
        q_refused=q_refused,
        capacity_before=movement.phi,
        capacity_after=0.0,
        sink_assignment=movement.sink_assignment,
        reason="Only a bounded lawful fraction is capacity-supported; remainder remains non-binding.",
        rule_trace=trace,
    )
