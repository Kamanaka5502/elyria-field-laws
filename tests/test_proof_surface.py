from runtime.proof_surface import (
    ProofSurface,
    ProofSurfaceVerdict,
    verify_proof_surface,
)


def complete_fields(**overrides):
    fields = dict(
        movement_object={"movement_id": "M-001"},
        lawful_region_state={"inside_R": True},
        standing_basis={"authority": True, "lineage": True},
        kernel_decision="REFUSE",
        protected_effect_map={"protected_effect_id": "E-001"},
        effect_prevention_result={"effect_formed": False},
        receipt_object={"receipt_id": "REC-001"},
        legitimacy_replay_object={"verdict": "LEGITIMACY_REPLAY_VALID"},
    )
    fields.update(overrides)
    return fields


def base_surface(**overrides):
    data = dict(
        surface_id="PS-TEST",
        fields=complete_fields(),
        non_allow_outcome=True,
        protected_effect_formed=False,
        prevention_replayable=True,
        failure_class="AUTHORITY_DECAY",
    )
    data.update(overrides)
    return ProofSurface(**data)


def test_complete_non_allow_surface_with_prevention_is_valid():
    receipt = verify_proof_surface(base_surface())

    assert receipt.verdict == ProofSurfaceVerdict.PROOF_SURFACE_VALID
    assert receipt.proof_surface_valid is True
    assert receipt.missing_fields == []


def test_missing_required_field_is_incomplete():
    fields = complete_fields(protected_effect_map=None)
    receipt = verify_proof_surface(base_surface(fields=fields))

    assert receipt.verdict == ProofSurfaceVerdict.PROOF_SURFACE_INCOMPLETE
    assert receipt.proof_surface_valid is False
    assert "protected_effect_map" in receipt.missing_fields


def test_effect_formed_under_non_allow_is_control_surface_only():
    receipt = verify_proof_surface(base_surface(protected_effect_formed=True))

    assert receipt.verdict == ProofSurfaceVerdict.CONTROL_SURFACE_ONLY
    assert receipt.proof_surface_valid is False


def test_non_allow_without_failure_class_is_control_surface_only():
    receipt = verify_proof_surface(base_surface(failure_class=None))

    assert receipt.verdict == ProofSurfaceVerdict.CONTROL_SURFACE_ONLY
    assert receipt.proof_surface_valid is False


def test_non_replayable_prevention_is_control_surface_only():
    receipt = verify_proof_surface(base_surface(prevention_replayable=False))

    assert receipt.verdict == ProofSurfaceVerdict.CONTROL_SURFACE_ONLY
    assert receipt.proof_surface_valid is False


def test_allow_class_surface_can_be_valid_when_replayable():
    receipt = verify_proof_surface(
        base_surface(
            fields=complete_fields(kernel_decision="ALLOW"),
            non_allow_outcome=False,
            protected_effect_formed=True,
            failure_class=None,
            prevention_replayable=True,
        )
    )

    assert receipt.verdict == ProofSurfaceVerdict.PROOF_SURFACE_VALID
    assert receipt.proof_surface_valid is True
