from runtime.hot_path_34ms import (
    STAGE_BUDGET_MS,
    TARGET_TOTAL_MS,
    GateDecision,
    HotPathInput,
    HotPathVerdict,
    budget_total_ms,
    resolve_hot_path,
)


def stage_latency(total="target"):
    if total == "target":
        return {stage: float(ms) for stage, ms in STAGE_BUDGET_MS.items()}
    if total == "warn":
        # 40 ms total: above 34 ms target but under 50 ms preferred ceiling.
        values = {stage: float(ms) for stage, ms in STAGE_BUDGET_MS.items()}
        values["L10_GATE_RESOLUTION"] += 6.0
        return values
    if total == "escalate":
        # 80 ms total: above 75 ms escalation threshold but under 100 ms hard ceiling.
        values = {stage: float(ms) for stage, ms in STAGE_BUDGET_MS.items()}
        values["L13_LEGITIMACY_REPLAY"] += 46.0
        return values
    if total == "reentry":
        # 120 ms total: above hard ceiling but under outer failsafe.
        values = {stage: float(ms) for stage, ms in STAGE_BUDGET_MS.items()}
        values["L13_LEGITIMACY_REPLAY"] += 86.0
        return values
    if total == "refuse":
        # 220 ms total: above outer failsafe.
        values = {stage: float(ms) for stage, ms in STAGE_BUDGET_MS.items()}
        values["L13_LEGITIMACY_REPLAY"] += 186.0
        return values
    raise ValueError(total)


def hot_input(**overrides):
    data = dict(
        event_id="EV-34MS-TEST",
        envelope_id="ENV-34MS-TEST",
        movement_id="M-34MS-TEST",
        corridor_id="C-34MS-TEST",
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
        measured_stage_latency_ms=stage_latency("target"),
    )
    data.update(overrides)
    return HotPathInput(**data)


def test_budget_contract_equals_34_ms():
    assert budget_total_ms() == TARGET_TOTAL_MS == 34


def test_clean_34ms_allow_is_hot_path_ready():
    receipt = resolve_hot_path(hot_input())

    assert receipt.verdict == HotPathVerdict.HOT_PATH_READY
    assert receipt.gate_decision == GateDecision.ALLOW
    assert receipt.budget_total_ms == 34
    assert receipt.measured_total_ms == 34.0
    assert receipt.proof_surface_verdict == "PROOF_SURFACE_VALID"


def test_fast_refuse_with_effect_prevented_is_valid():
    receipt = resolve_hot_path(
        hot_input(
            hard_gates_pass=False,
            protected_effect_formed=False,
            measured_stage_latency_ms=stage_latency("target"),
        )
    )

    assert receipt.verdict == HotPathVerdict.HOT_PATH_READY
    assert receipt.gate_decision == GateDecision.REFUSE
    assert receipt.failure_class == "FAILED_STANDING_OR_REGION"
    assert receipt.proof_surface_verdict == "PROOF_SURFACE_VALID"


def test_non_allow_with_effect_formed_collapses():
    receipt = resolve_hot_path(
        hot_input(
            hard_gates_pass=False,
            protected_effect_formed=True,
        )
    )

    assert receipt.gate_decision == GateDecision.REFUSE
    assert receipt.failure_class == "EFFECT_FORMED_WITHOUT_ALLOW"
    assert receipt.proof_surface_verdict == "CONTROL_SURFACE_ONLY"


def test_missing_protected_effect_map_exits_to_safe_path():
    receipt = resolve_hot_path(hot_input(protected_effect_mapped=False))

    assert receipt.verdict == HotPathVerdict.SAFE_PATH_REQUIRED
    assert receipt.gate_decision == GateDecision.REENTRY_REQUIRED
    assert receipt.safe_path_reason == "PROTECTED_EFFECT_UNMAPPED"
    assert receipt.proof_surface_verdict == "PROOF_SURFACE_INCOMPLETE"


def test_expired_standing_ttl_exits_to_safe_path():
    receipt = resolve_hot_path(hot_input(standing_ttl_ms=10, standing_age_ms=11))

    assert receipt.verdict == HotPathVerdict.SAFE_PATH_REQUIRED
    assert receipt.safe_path_reason == "STANDING_TTL_EXPIRED"
    assert receipt.gate_decision == GateDecision.REENTRY_REQUIRED


def test_field_hash_change_exits_to_safe_path():
    receipt = resolve_hot_path(hot_input(field_hash_after="hash-field-changed"))

    assert receipt.verdict == HotPathVerdict.SAFE_PATH_REQUIRED
    assert receipt.safe_path_reason == "FIELD_HASH_CHANGED"
    assert receipt.gate_decision == GateDecision.REENTRY_REQUIRED


def test_warning_latency_does_not_allow_uncertainty_but_can_allow_complete_path():
    receipt = resolve_hot_path(hot_input(measured_stage_latency_ms=stage_latency("warn")))

    assert receipt.measured_total_ms == 40.0
    assert receipt.verdict == HotPathVerdict.LATENCY_WARN
    assert receipt.gate_decision == GateDecision.ALLOW
    assert receipt.proof_surface_verdict == "PROOF_SURFACE_VALID"


def test_latency_above_75_escalates():
    receipt = resolve_hot_path(hot_input(measured_stage_latency_ms=stage_latency("escalate")))

    assert receipt.measured_total_ms == 80.0
    assert receipt.verdict == HotPathVerdict.ESCALATE_LATENCY
    assert receipt.gate_decision == GateDecision.ESCALATE
    assert receipt.proof_surface_verdict == "CONTROL_SURFACE_ONLY"


def test_latency_above_100_requires_reentry():
    receipt = resolve_hot_path(hot_input(measured_stage_latency_ms=stage_latency("reentry")))

    assert receipt.measured_total_ms == 120.0
    assert receipt.verdict == HotPathVerdict.LATENCY_REENTRY_REQUIRED
    assert receipt.gate_decision == GateDecision.REENTRY_REQUIRED


def test_latency_above_outer_failsafe_refuses():
    receipt = resolve_hot_path(hot_input(measured_stage_latency_ms=stage_latency("refuse")))

    assert receipt.measured_total_ms == 220.0
    assert receipt.verdict == HotPathVerdict.LATENCY_REFUSE
    assert receipt.gate_decision == GateDecision.REFUSE


def test_uncertain_replay_material_never_allows():
    receipt = resolve_hot_path(hot_input(replay_material_present=False))

    assert receipt.verdict == HotPathVerdict.SAFE_PATH_REQUIRED
    assert receipt.safe_path_reason == "REPLAY_MATERIAL_MISSING"
    assert receipt.gate_decision == GateDecision.REENTRY_REQUIRED
