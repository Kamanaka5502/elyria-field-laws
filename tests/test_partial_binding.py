from runtime.partial_binding import PartialDecision, PartialMovement, resolve_partial


def base_partial(**overrides):
    data = dict(
        movement_id="PM-TEST",
        q_total=100.0,
        available_capacity=100.0,
        carried_burden=0.0,
        authority_standing=True,
        lineage_integrity=True,
        evidence_freshness=True,
        consequence_admissibility=True,
        witness_replay_validity=True,
        sink_assignment="sink-A",
    )
    data.update(overrides)
    return PartialMovement(**data)


def test_full_capacity_allows_full_quantity():
    receipt = resolve_partial(base_partial(q_total=40.0, available_capacity=100.0))

    assert receipt.decision == PartialDecision.ALLOW_FULL
    assert receipt.partial_bind_defined is True
    assert receipt.q_allowed == 40.0
    assert receipt.q_refused == 0.0
    assert receipt.capacity_after == 60.0


def test_partial_capacity_allows_only_bounded_fraction():
    receipt = resolve_partial(base_partial(q_total=100.0, available_capacity=40.0))

    assert receipt.decision == PartialDecision.ALLOW_PARTIAL
    assert receipt.partial_bind_defined is True
    assert receipt.q_allowed == 40.0
    assert receipt.q_refused == 60.0
    assert receipt.capacity_after == 0.0


def test_zero_capacity_refuses_entire_quantity():
    receipt = resolve_partial(base_partial(q_total=100.0, available_capacity=0.0))

    assert receipt.decision == PartialDecision.REFUSE
    assert receipt.partial_bind_defined is False
    assert receipt.q_allowed == 0.0
    assert receipt.q_refused == 100.0


def test_negative_capacity_refuses_entire_quantity():
    receipt = resolve_partial(base_partial(q_total=100.0, available_capacity=30.0, carried_burden=50.0))

    assert receipt.decision == PartialDecision.REFUSE
    assert receipt.partial_bind_defined is False
    assert receipt.q_allowed == 0.0
    assert receipt.q_refused == 100.0


def test_hard_gate_failure_refuses_partial_binding():
    receipt = resolve_partial(base_partial(authority_standing=False, available_capacity=100.0))

    assert receipt.decision == PartialDecision.REFUSE
    assert receipt.partial_bind_defined is False
    assert receipt.q_allowed == 0.0
    assert receipt.q_refused == 100.0


def test_non_positive_quantity_refuses():
    receipt = resolve_partial(base_partial(q_total=0.0, available_capacity=100.0))

    assert receipt.decision == PartialDecision.REFUSE
    assert receipt.partial_bind_defined is False
    assert receipt.q_allowed == 0.0


def test_carried_burden_reduces_allowed_fraction():
    receipt = resolve_partial(base_partial(q_total=80.0, available_capacity=100.0, carried_burden=45.0))

    assert receipt.decision == PartialDecision.ALLOW_PARTIAL
    assert receipt.partial_bind_defined is True
    assert receipt.q_allowed == 55.0
    assert receipt.q_refused == 25.0
    assert receipt.capacity_after == 0.0
