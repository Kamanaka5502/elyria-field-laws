"""End-to-end bounded corridor runner for Elyria Field Laws.

One corridor. One protected effect. One replayable proof.

This module composes the existing runtime surfaces:
    - lawful-region evaluation
    - movement kernel resolution
    - protected-effect guard
    - legitimacy replay verifier
    - proof-surface verifier

The runner is intentionally narrow. It proves one bounded corridor instead of
pretending to cover every possible system.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Optional

from runtime.admissibility_region import ContinuationState, evaluate_region
from runtime.effect_guard import ProtectedEffectAttempt, guard_protected_effect
from runtime.kernel import Movement, resolve
from runtime.proof_surface import ProofSurface, verify_proof_surface
from runtime.replay_verifier import ReplayObject, verify_legitimacy_replay


@dataclass(frozen=True)
class CorridorInput:
    corridor_id: str
    movement: Movement
    continuation_state: ContinuationState
    protected_effect_id: Optional[str]
    effect_formed: bool
    receipt_bound_to_effect: bool
    replay: ReplayObject
    failure_class: Optional[str] = None


@dataclass(frozen=True)
class CorridorReceipt:
    corridor_id: str
    movement_id: str
    region_verdict: str
    kernel_decision: str
    effect_verdict: str
    replay_verdict: str
    proof_surface_verdict: str
    proof_surface_valid: bool
    summary: Dict[str, object]


def run_corridor(corridor: CorridorInput) -> CorridorReceipt:
    """Run one bounded consequence-governance corridor."""

    region_receipt = evaluate_region(corridor.continuation_state)
    kernel_receipt = resolve(corridor.movement)

    effect_receipt = guard_protected_effect(
        ProtectedEffectAttempt(
            movement_id=corridor.movement.movement_id,
            protected_effect_id=corridor.protected_effect_id,
            kernel_decision=kernel_receipt.decision.value,
            effect_formed=corridor.effect_formed,
            receipt_bound_to_effect=corridor.receipt_bound_to_effect,
            replayable_prevention=True,
        )
    )

    replay_receipt = verify_legitimacy_replay(corridor.replay)

    non_allow = kernel_receipt.decision.value != "ALLOW"
    proof_surface = ProofSurface(
        surface_id=f"PS-{corridor.corridor_id}",
        fields={
            "movement_object": corridor.movement,
            "lawful_region_state": region_receipt,
            "standing_basis": kernel_receipt.hard_gates,
            "kernel_decision": kernel_receipt.decision.value,
            "protected_effect_map": {"protected_effect_id": corridor.protected_effect_id}
            if corridor.protected_effect_id
            else None,
            "effect_prevention_result": effect_receipt,
            "receipt_object": {
                "movement_id": corridor.movement.movement_id,
                "kernel_decision": kernel_receipt.decision.value,
                "protected_effect_id": corridor.protected_effect_id,
            },
            "legitimacy_replay_object": replay_receipt,
        },
        non_allow_outcome=non_allow,
        protected_effect_formed=corridor.effect_formed,
        prevention_replayable=replay_receipt.legitimacy_replay_valid,
        prevention_proven=effect_receipt.prevention_proven,
        failure_class=corridor.failure_class if non_allow else None,
    )
    proof_receipt = verify_proof_surface(proof_surface)

    return CorridorReceipt(
        corridor_id=corridor.corridor_id,
        movement_id=corridor.movement.movement_id,
        region_verdict=region_receipt.verdict.value,
        kernel_decision=kernel_receipt.decision.value,
        effect_verdict=effect_receipt.verdict.value,
        replay_verdict=replay_receipt.verdict.value,
        proof_surface_verdict=proof_receipt.verdict.value,
        proof_surface_valid=proof_receipt.proof_surface_valid,
        summary={
            "region": region_receipt.reason,
            "kernel": kernel_receipt.reason,
            "effect": effect_receipt.reason,
            "replay": replay_receipt.reason,
            "proof_surface": proof_receipt.reason,
        },
    )
