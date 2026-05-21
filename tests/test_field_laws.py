from runtime.kernel import Decision, Movement, bind_defined, resolve


def base_movement(**overrides):
    data = dict(
        movement_id="M-TEST",
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


def test_allow_defines_bind_status():
    receipt = resolve(base_movement())

    assert receipt.decision == Decision.ALLOW
    assert receipt.bind_defined is True
    assert bind_defined(receipt) is True


def test_hard_gate_failure_refuses_and_never_binds():
    receipt = resolve(base_movement(authority_standing=False))

    assert receipt.decision == Decision.REFUSE
    assert receipt.bind_defined is False
    assert bind_defined(receipt) is False
    assert receipt.hard_gates["authority"] is False


def test_redirect_requires_distance_reduction():
    receipt = resolve(
        base_movement(
            admissibility_distance=0.5,
            lawful_redirect_available=True,
            redirect_distance=0.2,
        )
    )

    assert receipt.decision == Decision.REDIRECT
    assert receipt.bind_defined is False
    assert bind_defined(receipt) is False


def test_redirect_without_distance_reduction_refuses_when_no_external_resolution():
    receipt = resolve(
        base_movement(
            admissibility_distance=0.5,
            lawful_redirect_available=True,
            redirect_distance=0.8,
        )
    )

    assert receipt.decision == Decision.REFUSE
    assert receipt.bind_defined is False
    assert bind_defined(receipt) is False


def test_external_resolution_escalates_without_binding():
    receipt = resolve(
        base_movement(
            admissibility_distance=0.4,
            external_resolution_available=True,
        )
    )

    assert receipt.decision == Decision.ESCALATE
    assert receipt.bind_defined is False
    assert bind_defined(receipt) is False


def test_consequence_expansion_halts_without_binding():
    receipt = resolve(base_movement(continued_movement_expands_risk=True))

    assert receipt.decision == Decision.HALT
    assert receipt.bind_defined is False
    assert bind_defined(receipt) is False


def test_invalid_trajectory_redirects_only_when_lawful_repair_exists():
    receipt = resolve(
        base_movement(
            trajectory_validity=False,
            admissibility_distance=0.6,
            lawful_redirect_available=True,
            redirect_distance=0.3,
        )
    )

    assert receipt.decision == Decision.REDIRECT
    assert receipt.bind_defined is False
    assert bind_defined(receipt) is False


def test_invalid_trajectory_refuses_without_repair_or_escalation():
    receipt = resolve(base_movement(trajectory_validity=False, admissibility_distance=0.6))

    assert receipt.decision == Decision.REFUSE
    assert receipt.bind_defined is False
    assert bind_defined(receipt) is False
