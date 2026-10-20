"""Minimum proof-surface verifier for consequence-bound governance."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Optional


class ProofSurfaceVerdict(str, Enum):
    PROOF_SURFACE_VALID = "PROOF_SURFACE_VALID"
    PROOF_SURFACE_INCOMPLETE = "PROOF_SURFACE_INCOMPLETE"
    CONTROL_SURFACE_ONLY = "CONTROL_SURFACE_ONLY"


REQUIRED_SURFACE_FIELDS = (
    "movement_object",
    "lawful_region_state",
    "standing_basis",
    "kernel_decision",
    "protected_effect_map",
    "effect_prevention_result",
    "receipt_object",
    "legitimacy_replay_object",
)


@dataclass(frozen=True)
class ProofSurface:
    surface_id: str
    fields: Dict[str, Optional[object]]
    non_allow_outcome: bool
    protected_effect_formed: bool
    prevention_replayable: bool
    prevention_proven: bool
    failure_class: Optional[str] = None


@dataclass(frozen=True)
class ProofSurfaceReceipt:
    surface_id: str
    verdict: ProofSurfaceVerdict
    proof_surface_valid: bool
    missing_fields: List[str]
    reason: str
    rule_trace: List[str]


def verify_proof_surface(surface: ProofSurface) -> ProofSurfaceReceipt:
    """Verify the minimum proof surface and enforce its prevention obligation."""

    trace: List[str] = ["proof_surface.object.present"]
    missing = [name for name in REQUIRED_SURFACE_FIELDS if not surface.fields.get(name)]

    if missing:
        trace.append("surface_fields.missing:" + ",".join(missing))
        return ProofSurfaceReceipt(
            surface_id=surface.surface_id,
            verdict=ProofSurfaceVerdict.PROOF_SURFACE_INCOMPLETE,
            proof_surface_valid=False,
            missing_fields=missing,
            reason="Minimum proof-surface fields are missing.",
            rule_trace=trace,
        )

    trace.append("surface_fields.present")

    if surface.non_allow_outcome and surface.protected_effect_formed:
        trace.append("control_surface_only.effect_formed_under_non_allow")
        return ProofSurfaceReceipt(
            surface_id=surface.surface_id,
            verdict=ProofSurfaceVerdict.CONTROL_SURFACE_ONLY,
            proof_surface_valid=False,
            missing_fields=[],
            reason="Protected effect formed under non-allow outcome; governance proof fails.",
            rule_trace=trace,
        )

    if surface.non_allow_outcome and not surface.failure_class:
        trace.append("control_surface_only.failure_class_missing")
        return ProofSurfaceReceipt(
            surface_id=surface.surface_id,
            verdict=ProofSurfaceVerdict.CONTROL_SURFACE_ONLY,
            proof_surface_valid=False,
            missing_fields=[],
            reason="Non-allow outcome lacks specific failure class.",
            rule_trace=trace,
        )

    if surface.non_allow_outcome and not surface.prevention_proven:
        trace.append("control_surface_only.prevention_not_proven")
        return ProofSurfaceReceipt(
            surface_id=surface.surface_id,
            verdict=ProofSurfaceVerdict.CONTROL_SURFACE_ONLY,
            proof_surface_valid=False,
            missing_fields=[],
            reason="Non-allow outcome lacks a positive prevention result; proof surface cannot be certified.",
            rule_trace=trace,
        )

    if not surface.prevention_replayable:
        trace.append("control_surface_only.prevention_not_replayable")
        return ProofSurfaceReceipt(
            surface_id=surface.surface_id,
            verdict=ProofSurfaceVerdict.CONTROL_SURFACE_ONLY,
            proof_surface_valid=False,
            missing_fields=[],
            reason="Prevention or admission basis is not replayable.",
            rule_trace=trace,
        )

    trace.append("proof_surface.valid")
    return ProofSurfaceReceipt(
        surface_id=surface.surface_id,
        verdict=ProofSurfaceVerdict.PROOF_SURFACE_VALID,
        proof_surface_valid=True,
        missing_fields=[],
        reason="Required fields, outcome consistency, prevention obligation, and replayability checks passed.",
        rule_trace=trace,
    )
