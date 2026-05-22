from runtime.admissibility_region import ContinuationState
from runtime.corridor_runner import CorridorInput, run_corridor
from runtime.kernel import Movement
from runtime.replay_verifier import REQUIRED_LEGITIMACY_FIELDS, ReplayObject


def legitimacy_fields(**overrides):
    fields = {name: f"hash-{name}" for name in REQUIRED_LEGITIMACY_FIELDS}
    fields.update(overrides)
    return fields


def replay(decision="ALLOW", bind_status=True, fields=None):
    return ReplayObject(
        replay_id="R-CORRIDOR-TEST",
        terminal_outcome_hash="hash-terminal",
        legitimacy_fields=fields or legitimacy_fields(),
        reconstructed_decision=decision,
        original_decision=decision,
        reconstructed_bind_status=bind_status,
        original_bind_status=bind_status,
    )


def movement(**overrides):
    data = dict(
        movement_id="M-CORRIDOR-TEST",
        origin_state="S0",
        target_state="S1",
        authority_standing=True,
        lineage_integrity=True,
        evidence_freshness=True,
        recovery_viability=True,
        consequence_admissibility=True,
        witness_replay_validity=True,
        trajectory_validity=True,
        admissibility_distance=0.0,
    )
    data.update(overrides)
    return Movement(**data)


def region(**overrides):
    data = dict(
        state_id="Z-CORRIDOR-TEST",
        admissibility=1.0,
        available_capacity=1.0,
        carried_burden=0.0,
        authority_valid=True,
    )
    data.update(overrides)
    return ContinuationState(**data)


def test_valid_allow_corridor_produces_valid_proof_surface():
    receipt = run_corridor(
        CorridorInput(
            corridor_id="C-ALLOW-001",
            movement=movement(),
            continuation_state=region(),
            protected_effect_id="E-PROTECTED-001",
            effect_formed=True,
            receipt_bound_to_effect=True,
            replay=replay(decision="ALLOW", bind_status=True),
        )
    )

    assert receipt.region_verdict == "INSIDE_R"
    assert receipt.kernel_decision == "ALLOW"
    assert receipt.effect_verdict == "EFFECT_ALLOWED"
    assert receipt.replay_verdict == "LEGITIMACY_REPLAY_VALID"
    assert receipt.proof_surface_verdict == "PROOF_SURFACE_VALID"
    assert receipt.proof_surface_valid is True


def test_non_allow_prevented_effect_with_legitimacy_replay_is_valid():
    receipt = run_corridor(
        CorridorInput(
            corridor_id="C-REFUSE-001",
            movement=movement(authority_standing=False),
            continuation_state=region(),
            protected_effect_id="E-PROTECTED-001",
            effect_formed=False,
            receipt_bound_to_effect=True,
            replay=replay(decision="REFUSE", bind_status=False),
            failure_class="AUTHORITY_INVALID",
        )
    )

    assert receipt.kernel_decision == "REFUSE"
    assert receipt.effect_verdict == "EFFECT_PREVENTED"
    assert receipt.replay_verdict == "LEGITIMACY_REPLAY_VALID"
    assert receipt.proof_surface_verdict == "PROOF_SURFACE_VALID"
    assert receipt.proof_surface_valid is True


def test_non_allow_with_effect_formed_collapses_to_control_surface():
    receipt = run_corridor(
        CorridorInput(
            corridor_id="C-VIOLATION-001",
            movement=movement(authority_standing=False),
            continuation_state=region(),
            protected_effect_id="E-PROTECTED-001",
            effect_formed=True,
            receipt_bound_to_effect=True,
            replay=replay(decision="REFUSE", bind_status=False),
            failure_class="AUTHORITY_INVALID",
        )
    )

    assert receipt.kernel_decision == "REFUSE"
    assert receipt.effect_verdict == "EFFECT_VIOLATION"
    assert receipt.proof_surface_verdict == "CONTROL_SURFACE_ONLY"
    assert receipt.proof_surface_valid is False


def test_missing_protected_effect_map_is_incomplete_surface():
    receipt = run_corridor(
        CorridorInput(
            corridor_id="C-UNMAPPED-001",
            movement=movement(authority_standing=False),
            continuation_state=region(),
            protected_effect_id=None,
            effect_formed=False,
            receipt_bound_to_effect=True,
            replay=replay(decision="REFUSE", bind_status=False),
            failure_class="AUTHORITY_INVALID",
        )
    )

    assert receipt.effect_verdict == "EFFECT_UNMAPPED"
    assert receipt.proof_surface_verdict == "PROOF_SURFACE_INCOMPLETE"
    assert receipt.proof_surface_valid is False


def test_execution_replay_only_collapses_proof_surface():
    fields = legitimacy_fields(authority_hash=None)
    receipt = run_corridor(
        CorridorInput(
            corridor_id="C-REPLAY-COLLAPSE-001",
            movement=movement(authority_standing=False),
            continuation_state=region(),
            protected_effect_id="E-PROTECTED-001",
            effect_formed=False,
            receipt_bound_to_effect=True,
            replay=replay(decision="REFUSE", bind_status=False, fields=fields),
            failure_class="AUTHORITY_INVALID",
        )
    )

    assert receipt.replay_verdict == "EXECUTION_REPLAY_ONLY"
    assert receipt.proof_surface_verdict == "CONTROL_SURFACE_ONLY"
    assert receipt.proof_surface_valid is False


def test_non_allow_without_failure_class_collapses_proof_surface():
    receipt = run_corridor(
        CorridorInput(
            corridor_id="C-NO-FAILURE-CLASS-001",
            movement=movement(authority_standing=False),
            continuation_state=region(),
            protected_effect_id="E-PROTECTED-001",
            effect_formed=False,
            receipt_bound_to_effect=True,
            replay=replay(decision="REFUSE", bind_status=False),
            failure_class=None,
        )
    )

    assert receipt.kernel_decision == "REFUSE"
    assert receipt.proof_surface_verdict == "CONTROL_SURFACE_ONLY"
    assert receipt.proof_surface_valid is False
