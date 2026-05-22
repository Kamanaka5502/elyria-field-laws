"""34 ms hot-path corridor contract.

This module does not claim the host machine will always execute in 34 ms.
It defines the compiled-corridor contract required for a 34 ms target:

    fast when complete
    safe-path when uncertain
    replayable always

The hot path is eligible only when all required proof objects are already
bounded, local, current, and hash-ready.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional


STAGE_BUDGET_MS: Dict[str, int] = {
    "L1_EVENT_INTAKE": 1,
    "L2_CLASSIFICATION": 2,
    "L3_CANONICAL_ENVELOPE": 3,
    "L4_COMPLETENESS_CHECK": 1,
    "L5_STANDING_ASSEMBLY": 4,
    "L6_FIELD_STATE_BINDING": 3,
    "L7_LAWFUL_REGION_EVALUATION": 2,
    "L8_PROTECTED_EFFECT_MAPPING": 2,
    "L9_GATE_INPUT_CONSTRUCTION": 1,
    "L10_GATE_RESOLUTION": 4,
    "L11_PROTECTED_EFFECT_GUARD": 2,
    "L12_RECEIPT_ISSUANCE": 3,
    "L13_LEGITIMACY_REPLAY": 4,
    "L14_PROOF_SURFACE_VERDICT": 1,
    "L15_OUTCOME_PUBLICATION": 1,
}

TARGET_TOTAL_MS = 34
PREFERRED_CEILING_MS = 50
ESCALATION_THRESHOLD_MS = 75
HARD_CEILING_MS = 100
OUTER_FAILSAFE_MS = 200


class HotPathVerdict(str, Enum):
    HOT_PATH_READY = "HOT_PATH_READY"
    SAFE_PATH_REQUIRED = "SAFE_PATH_REQUIRED"
    LATENCY_WARN = "LATENCY_WARN"
    ESCALATE_LATENCY = "ESCALATE_LATENCY"
    LATENCY_REENTRY_REQUIRED = "LATENCY_REENTRY_REQUIRED"
    LATENCY_REFUSE = "LATENCY_REFUSE"


class GateDecision(str, Enum):
    ALLOW = "ALLOW"
    REFUSE = "REFUSE"
    ESCALATE = "ESCALATE"
    HALT = "HALT"
    REENTRY_REQUIRED = "REENTRY_REQUIRED"


@dataclass(frozen=True)
class HotPathInput:
    event_id: str
    envelope_id: str
    movement_id: str
    corridor_id: str
    envelope_shape_known: bool
    movement_type_known: bool
    standing_refs_current: bool
    standing_ttl_ms: int
    standing_age_ms: int
    field_state_hash_available: bool
    field_hash_before: str
    field_hash_after: str
    protected_effect_mapped: bool
    law_version_current: bool
    replay_material_present: bool
    prior_receipt_hash_matches: bool = True
    changed_condition_pending: bool = False
    route_or_transfer_ambiguity: bool = False
    capacity_boundary_reached: bool = False
    hard_gates_pass: bool = True
    inside_lawful_region: bool = True
    protected_effect_formed: bool = False
    measured_stage_latency_ms: Dict[str, float] = field(default_factory=dict)


@dataclass(frozen=True)
class HotPathReceipt:
    event_id: str
    envelope_id: str
    movement_id: str
    corridor_id: str
    profile: str
    verdict: HotPathVerdict
    gate_decision: GateDecision
    target_total_ms: int
    budget_total_ms: int
    measured_total_ms: Optional[float]
    stage_budget_ms: Dict[str, int]
    stage_latency_ms: Dict[str, float]
    safe_path_reason: Optional[str]
    failure_class: Optional[str]
    proof_surface_verdict: str
    rule_trace: List[str]


def budget_total_ms() -> int:
    """Return the compiled 34 ms stage-budget total."""

    return sum(STAGE_BUDGET_MS.values())


def _measured_total(stage_latency: Dict[str, float]) -> Optional[float]:
    if not stage_latency:
        return None
    return sum(stage_latency.values())


def _first_safe_path_reason(hot: HotPathInput) -> Optional[str]:
    if not hot.envelope_shape_known:
        return "ENVELOPE_SHAPE_UNKNOWN"
    if not hot.movement_type_known:
        return "MOVEMENT_TYPE_UNKNOWN"
    if not hot.standing_refs_current:
        return "STANDING_REFS_NOT_CURRENT"
    if hot.standing_age_ms > hot.standing_ttl_ms:
        return "STANDING_TTL_EXPIRED"
    if not hot.field_state_hash_available:
        return "FIELD_STATE_HASH_MISSING"
    if hot.field_hash_before != hot.field_hash_after:
        return "FIELD_HASH_CHANGED"
    if not hot.protected_effect_mapped:
        return "PROTECTED_EFFECT_UNMAPPED"
    if not hot.law_version_current:
        return "LAW_VERSION_STALE"
    if not hot.replay_material_present:
        return "REPLAY_MATERIAL_MISSING"
    if not hot.prior_receipt_hash_matches:
        return "PRIOR_RECEIPT_HASH_MISMATCH"
    if hot.changed_condition_pending:
        return "CHANGED_CONDITION_PENDING"
    if hot.route_or_transfer_ambiguity:
        return "ROUTE_OR_TRANSFER_AMBIGUITY"
    if hot.capacity_boundary_reached:
        return "CAPACITY_BOUNDARY_REACHED"
    return None


def _latency_verdict(total_ms: Optional[float]) -> Optional[HotPathVerdict]:
    if total_ms is None:
        return None
    if total_ms <= TARGET_TOTAL_MS:
        return HotPathVerdict.HOT_PATH_READY
    if total_ms <= PREFERRED_CEILING_MS:
        return HotPathVerdict.LATENCY_WARN
    if total_ms <= ESCALATION_THRESHOLD_MS:
        return HotPathVerdict.LATENCY_WARN
    if total_ms <= HARD_CEILING_MS:
        return HotPathVerdict.ESCALATE_LATENCY
    if total_ms <= OUTER_FAILSAFE_MS:
        return HotPathVerdict.LATENCY_REENTRY_REQUIRED
    return HotPathVerdict.LATENCY_REFUSE


def resolve_hot_path(hot: HotPathInput) -> HotPathReceipt:
    """Resolve the 34 ms hot-path contract.

    The function is deliberately conservative:
    any missing or stale proof input leaves the hot path.
    """

    trace: List[str] = ["hot_path.input.present"]
    compiled_total = budget_total_ms()
    measured_total = _measured_total(hot.measured_stage_latency_ms)

    if compiled_total != TARGET_TOTAL_MS:
        trace.append("budget.contract.mismatch")
        return HotPathReceipt(
            event_id=hot.event_id,
            envelope_id=hot.envelope_id,
            movement_id=hot.movement_id,
            corridor_id=hot.corridor_id,
            profile="34ms_hot_path",
            verdict=HotPathVerdict.SAFE_PATH_REQUIRED,
            gate_decision=GateDecision.REENTRY_REQUIRED,
            target_total_ms=TARGET_TOTAL_MS,
            budget_total_ms=compiled_total,
            measured_total_ms=measured_total,
            stage_budget_ms=dict(STAGE_BUDGET_MS),
            stage_latency_ms=dict(hot.measured_stage_latency_ms),
            safe_path_reason="BUDGET_CONTRACT_MISMATCH",
            failure_class="LATENCY_PROFILE_INVALID",
            proof_surface_verdict="CONTROL_SURFACE_ONLY",
            rule_trace=trace,
        )

    trace.append("budget.contract.valid")

    reason = _first_safe_path_reason(hot)
    if reason:
        trace.append(f"safe_path.required:{reason}")
        return HotPathReceipt(
            event_id=hot.event_id,
            envelope_id=hot.envelope_id,
            movement_id=hot.movement_id,
            corridor_id=hot.corridor_id,
            profile="34ms_hot_path",
            verdict=HotPathVerdict.SAFE_PATH_REQUIRED,
            gate_decision=GateDecision.REENTRY_REQUIRED,
            target_total_ms=TARGET_TOTAL_MS,
            budget_total_ms=compiled_total,
            measured_total_ms=measured_total,
            stage_budget_ms=dict(STAGE_BUDGET_MS),
            stage_latency_ms=dict(hot.measured_stage_latency_ms),
            safe_path_reason=reason,
            failure_class=reason,
            proof_surface_verdict="PROOF_SURFACE_INCOMPLETE",
            rule_trace=trace,
        )

    latency_status = _latency_verdict(measured_total)
    if latency_status in {
        HotPathVerdict.ESCALATE_LATENCY,
        HotPathVerdict.LATENCY_REENTRY_REQUIRED,
        HotPathVerdict.LATENCY_REFUSE,
    }:
        trace.append(f"latency.exit:{latency_status.value}")
        gate_decision = (
            GateDecision.ESCALATE
            if latency_status is HotPathVerdict.ESCALATE_LATENCY
            else GateDecision.REENTRY_REQUIRED
        )
        if latency_status is HotPathVerdict.LATENCY_REFUSE:
            gate_decision = GateDecision.REFUSE
        return HotPathReceipt(
            event_id=hot.event_id,
            envelope_id=hot.envelope_id,
            movement_id=hot.movement_id,
            corridor_id=hot.corridor_id,
            profile="34ms_hot_path",
            verdict=latency_status,
            gate_decision=gate_decision,
            target_total_ms=TARGET_TOTAL_MS,
            budget_total_ms=compiled_total,
            measured_total_ms=measured_total,
            stage_budget_ms=dict(STAGE_BUDGET_MS),
            stage_latency_ms=dict(hot.measured_stage_latency_ms),
            safe_path_reason=latency_status.value,
            failure_class=latency_status.value,
            proof_surface_verdict="CONTROL_SURFACE_ONLY",
            rule_trace=trace,
        )

    if not hot.hard_gates_pass or not hot.inside_lawful_region:
        trace.append("fast_refuse.prevented_effect_required")
        if hot.protected_effect_formed:
            trace.append("effect.violation")
            return HotPathReceipt(
                event_id=hot.event_id,
                envelope_id=hot.envelope_id,
                movement_id=hot.movement_id,
                corridor_id=hot.corridor_id,
                profile="34ms_hot_path",
                verdict=latency_status or HotPathVerdict.HOT_PATH_READY,
                gate_decision=GateDecision.REFUSE,
                target_total_ms=TARGET_TOTAL_MS,
                budget_total_ms=compiled_total,
                measured_total_ms=measured_total,
                stage_budget_ms=dict(STAGE_BUDGET_MS),
                stage_latency_ms=dict(hot.measured_stage_latency_ms),
                safe_path_reason=None,
                failure_class="EFFECT_FORMED_WITHOUT_ALLOW",
                proof_surface_verdict="CONTROL_SURFACE_ONLY",
                rule_trace=trace,
            )
        return HotPathReceipt(
            event_id=hot.event_id,
            envelope_id=hot.envelope_id,
            movement_id=hot.movement_id,
            corridor_id=hot.corridor_id,
            profile="34ms_hot_path",
            verdict=latency_status or HotPathVerdict.HOT_PATH_READY,
            gate_decision=GateDecision.REFUSE,
            target_total_ms=TARGET_TOTAL_MS,
            budget_total_ms=compiled_total,
            measured_total_ms=measured_total,
            stage_budget_ms=dict(STAGE_BUDGET_MS),
            stage_latency_ms=dict(hot.measured_stage_latency_ms),
            safe_path_reason=None,
            failure_class="FAILED_STANDING_OR_REGION",
            proof_surface_verdict="PROOF_SURFACE_VALID",
            rule_trace=trace,
        )

    trace.append("fast_allow")
    return HotPathReceipt(
        event_id=hot.event_id,
        envelope_id=hot.envelope_id,
        movement_id=hot.movement_id,
        corridor_id=hot.corridor_id,
        profile="34ms_hot_path",
        verdict=latency_status or HotPathVerdict.HOT_PATH_READY,
        gate_decision=GateDecision.ALLOW,
        target_total_ms=TARGET_TOTAL_MS,
        budget_total_ms=compiled_total,
        measured_total_ms=measured_total,
        stage_budget_ms=dict(STAGE_BUDGET_MS),
        stage_latency_ms=dict(hot.measured_stage_latency_ms),
        safe_path_reason=None,
        failure_class=None,
        proof_surface_verdict="PROOF_SURFACE_VALID",
        rule_trace=trace,
    )
