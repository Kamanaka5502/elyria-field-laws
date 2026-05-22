from runtime.effect_guard import (
    EffectVerdict,
    ProtectedEffectAttempt,
    guard_protected_effect,
)


def base_attempt(**overrides):
    data = dict(
        movement_id="M-EFFECT-TEST",
        protected_effect_id="E-PROTECTED-001",
        kernel_decision="REFUSE",
        effect_formed=False,
        receipt_bound_to_effect=True,
        replayable_prevention=True,
    )
    data.update(overrides)
    return ProtectedEffectAttempt(**data)


def test_non_allow_with_no_effect_and_replayable_receipt_proves_prevention():
    receipt = guard_protected_effect(base_attempt(kernel_decision="REFUSE"))

    assert receipt.verdict == EffectVerdict.EFFECT_PREVENTED
    assert receipt.effect_formed is False
    assert receipt.prevention_proven is True


def test_non_allow_with_effect_formed_is_violation():
    receipt = guard_protected_effect(base_attempt(kernel_decision="REFUSE", effect_formed=True))

    assert receipt.verdict == EffectVerdict.EFFECT_VIOLATION
    assert receipt.effect_formed is True
    assert receipt.prevention_proven is False


def test_unmapped_effect_cannot_prove_prevention():
    receipt = guard_protected_effect(base_attempt(protected_effect_id=None))

    assert receipt.verdict == EffectVerdict.EFFECT_UNMAPPED
    assert receipt.prevention_proven is False


def test_effect_absence_without_bound_receipt_is_not_proven_prevention():
    receipt = guard_protected_effect(base_attempt(receipt_bound_to_effect=False))

    assert receipt.verdict == EffectVerdict.EFFECT_PREVENTED
    assert receipt.effect_formed is False
    assert receipt.prevention_proven is False


def test_effect_absence_without_replay_is_not_proven_prevention():
    receipt = guard_protected_effect(base_attempt(replayable_prevention=False))

    assert receipt.verdict == EffectVerdict.EFFECT_PREVENTED
    assert receipt.effect_formed is False
    assert receipt.prevention_proven is False


def test_allow_class_decision_may_form_effect():
    receipt = guard_protected_effect(base_attempt(kernel_decision="ALLOW", effect_formed=True))

    assert receipt.verdict == EffectVerdict.EFFECT_ALLOWED
    assert receipt.effect_formed is True
    assert receipt.prevention_proven is False


def test_allow_partial_is_allow_class_for_effect_guard():
    receipt = guard_protected_effect(base_attempt(kernel_decision="ALLOW_PARTIAL", effect_formed=True))

    assert receipt.verdict == EffectVerdict.EFFECT_ALLOWED
    assert receipt.effect_formed is True
    assert receipt.prevention_proven is False
