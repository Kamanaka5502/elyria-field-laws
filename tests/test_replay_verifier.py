from runtime.replay_verifier import (
    REQUIRED_LEGITIMACY_FIELDS,
    ReplayObject,
    ReplayVerdict,
    verify_legitimacy_replay,
)


def full_legitimacy_fields(**overrides):
    fields = {name: f"hash-{name}" for name in REQUIRED_LEGITIMACY_FIELDS}
    fields.update(overrides)
    return fields


def base_replay(**overrides):
    data = dict(
        replay_id="R-TEST",
        terminal_outcome_hash="hash-terminal",
        legitimacy_fields=full_legitimacy_fields(),
        reconstructed_decision="ALLOW",
        original_decision="ALLOW",
        reconstructed_bind_status=True,
        original_bind_status=True,
    )
    data.update(overrides)
    return ReplayObject(**data)


def test_full_legitimacy_replay_is_valid():
    receipt = verify_legitimacy_replay(base_replay())

    assert receipt.verdict == ReplayVerdict.LEGITIMACY_REPLAY_VALID
    assert receipt.legitimacy_replay_valid is True
    assert receipt.missing_fields == []
    assert receipt.mismatched_decision is False
    assert receipt.mismatched_bind_status is False


def test_terminal_outcome_without_legitimacy_fields_is_execution_replay_only():
    fields = full_legitimacy_fields(authority_hash=None, evidence_hash=None)
    receipt = verify_legitimacy_replay(base_replay(legitimacy_fields=fields))

    assert receipt.verdict == ReplayVerdict.EXECUTION_REPLAY_ONLY
    assert receipt.legitimacy_replay_valid is False
    assert "authority_hash" in receipt.missing_fields
    assert "evidence_hash" in receipt.missing_fields


def test_missing_terminal_outcome_is_invalid_replay():
    receipt = verify_legitimacy_replay(base_replay(terminal_outcome_hash=""))

    assert receipt.verdict == ReplayVerdict.REPLAY_INVALID
    assert receipt.legitimacy_replay_valid is False
    assert receipt.terminal_outcome_present is False


def test_decision_mismatch_is_execution_replay_only():
    receipt = verify_legitimacy_replay(
        base_replay(reconstructed_decision="REFUSE", original_decision="ALLOW")
    )

    assert receipt.verdict == ReplayVerdict.EXECUTION_REPLAY_ONLY
    assert receipt.legitimacy_replay_valid is False
    assert receipt.mismatched_decision is True


def test_bind_status_mismatch_is_execution_replay_only():
    receipt = verify_legitimacy_replay(
        base_replay(reconstructed_bind_status=False, original_bind_status=True)
    )

    assert receipt.verdict == ReplayVerdict.EXECUTION_REPLAY_ONLY
    assert receipt.legitimacy_replay_valid is False
    assert receipt.mismatched_bind_status is True


def test_same_terminal_outcome_does_not_imply_legitimacy_replay():
    fields = full_legitimacy_fields(trajectory_hash=None)
    receipt = verify_legitimacy_replay(base_replay(legitimacy_fields=fields))

    assert receipt.terminal_outcome_present is True
    assert receipt.verdict == ReplayVerdict.EXECUTION_REPLAY_ONLY
    assert receipt.legitimacy_replay_valid is False
    assert "trajectory_hash" in receipt.missing_fields
