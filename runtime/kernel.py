"""Elyria Field Laws movement kernel.

This module is intentionally small. It is the executable surface for the
field-law doctrine:

    BIND(M) is defined only when K(M) = ALLOW.

The kernel does not try to model the whole field. It preserves the minimum
non-compensable invariants required to decide whether a proposed movement may
reach consequence status.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional


class Decision(str, Enum):
    ALLOW = "ALLOW"
    REDIRECT = "REDIRECT"
    ESCALATE = "ESCALATE"
    REFUSE = "REFUSE"
    HALT = "HALT"


HARD_GATES = (
    "authority",
    "lineage",
    "evidence",
    "consequence",
    "witness",
)


@dataclass(frozen=True)
class Movement:
    """A proposed consequence-state transition."""

    movement_id: str
    origin_state: str
    target_state: str
    authority_standing: bool
    lineage_integrity: bool
    evidence_freshness: bool
    recovery_viability: bool
    consequence_admissibility: bool
    witness_replay_validity: bool
    trajectory_validity: bool
    admissibility_distance: float
    external_resolution_available: bool = False
    lawful_redirect_available: bool = False
    redirect_distance: Optional[float] = None
    continued_movement_expands_risk: bool = False
    notes: List[str] = field(default_factory=list)


@dataclass(frozen=True)
class KernelReceipt:
    movement_id: str
    decision: Decision
    bind_defined: bool
    hard_gates: Dict[str, bool]
    admissibility_distance: float
    reason: str
    rule_trace: List[str]


def _hard_gates(movement: Movement) -> Dict[str, bool]:
    return {
        "authority": movement.authority_standing,
        "lineage": movement.lineage_integrity,
        "evidence": movement.evidence_freshness,
        "consequence": movement.consequence_admissibility,
        "witness": movement.witness_replay_validity,
    }


def _failed_gates(gates: Dict[str, bool]) -> List[str]:
    return [name for name, passed in gates.items() if not passed]


def _lawful_redirect_reduces_distance(movement: Movement) -> bool:
    if not movement.lawful_redirect_available:
        return False
    if movement.redirect_distance is None:
        return False
    return movement.redirect_distance < movement.admissibility_distance


def resolve(movement: Movement) -> KernelReceipt:
    """Resolve proposed movement into ALLOW/REDIRECT/ESCALATE/REFUSE/HALT.

    Binding is defined only when the decision is ALLOW.
    """

    trace: List[str] = []
    gates = _hard_gates(movement)
    failed = _failed_gates(gates)

    trace.append("movement.object.present")
    trace.append(f"admissibility.distance={movement.admissibility_distance}")

    if movement.continued_movement_expands_risk:
        trace.append("halt.continued_movement_expands_illegitimate_consequence")
        return KernelReceipt(
            movement_id=movement.movement_id,
            decision=Decision.HALT,
            bind_defined=False,
            hard_gates=gates,
            admissibility_distance=movement.admissibility_distance,
            reason="Continued movement expands consequence exposure.",
            rule_trace=trace,
        )

    if failed:
        trace.append("hard_gate.failure:" + ",".join(failed))
        return KernelReceipt(
            movement_id=movement.movement_id,
            decision=Decision.REFUSE,
            bind_defined=False,
            hard_gates=gates,
            admissibility_distance=movement.admissibility_distance,
            reason="Non-compensable hard gate failure: " + ", ".join(failed),
            rule_trace=trace,
        )

    trace.append("hard_gates.pass")

    if not movement.trajectory_validity:
        trace.append("trajectory.invalid")
        if _lawful_redirect_reduces_distance(movement):
            trace.append("redirect.distance_reduces")
            return KernelReceipt(
                movement_id=movement.movement_id,
                decision=Decision.REDIRECT,
                bind_defined=False,
                hard_gates=gates,
                admissibility_distance=movement.admissibility_distance,
                reason="Trajectory is not valid, but a lawful redirect reduces admissibility distance.",
                rule_trace=trace,
            )
        if movement.external_resolution_available:
            trace.append("escalate.external_resolution_available")
            return KernelReceipt(
                movement_id=movement.movement_id,
                decision=Decision.ESCALATE,
                bind_defined=False,
                hard_gates=gates,
                admissibility_distance=movement.admissibility_distance,
                reason="Trajectory validity requires external resolution.",
                rule_trace=trace,
            )
        return KernelReceipt(
            movement_id=movement.movement_id,
            decision=Decision.REFUSE,
            bind_defined=False,
            hard_gates=gates,
            admissibility_distance=movement.admissibility_distance,
            reason="Trajectory invalid and no lawful correction path is available.",
            rule_trace=trace,
        )

    trace.append("trajectory.pass")

    if movement.admissibility_distance <= 0:
        trace.append("kernel.allow")
        return KernelReceipt(
            movement_id=movement.movement_id,
            decision=Decision.ALLOW,
            bind_defined=True,
            hard_gates=gates,
            admissibility_distance=movement.admissibility_distance,
            reason="Movement is inside the admissible region.",
            rule_trace=trace,
        )

    if _lawful_redirect_reduces_distance(movement):
        trace.append("redirect.distance_reduces")
        return KernelReceipt(
            movement_id=movement.movement_id,
            decision=Decision.REDIRECT,
            bind_defined=False,
            hard_gates=gates,
            admissibility_distance=movement.admissibility_distance,
            reason="Movement is outside admissible region; lawful redirect reduces distance.",
            rule_trace=trace,
        )

    if movement.external_resolution_available:
        trace.append("escalate.external_resolution_available")
        return KernelReceipt(
            movement_id=movement.movement_id,
            decision=Decision.ESCALATE,
            bind_defined=False,
            hard_gates=gates,
            admissibility_distance=movement.admissibility_distance,
            reason="Movement requires external resolution before consequence status.",
            rule_trace=trace,
        )

    trace.append("kernel.refuse.no_admissible_path")
    return KernelReceipt(
        movement_id=movement.movement_id,
        decision=Decision.REFUSE,
        bind_defined=False,
        hard_gates=gates,
        admissibility_distance=movement.admissibility_distance,
        reason="Movement is outside admissible region with no lawful correction path.",
        rule_trace=trace,
    )


def bind_defined(receipt: KernelReceipt) -> bool:
    """Return whether BIND(M) is defined for this kernel receipt."""

    return receipt.decision is Decision.ALLOW and receipt.bind_defined
