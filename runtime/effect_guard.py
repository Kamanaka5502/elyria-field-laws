"""Protected effect guard for Elyria Field Laws.

A runtime proves consequence-bound movement governance only when protected
effect formation is prevented for non-admissible movement.

Core rule:
    K(M) != ALLOW -> E_protected does not form
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import List, Optional


class EffectVerdict(str, Enum):
    EFFECT_ALLOWED = "EFFECT_ALLOWED"
    EFFECT_PREVENTED = "EFFECT_PREVENTED"
    EFFECT_VIOLATION = "EFFECT_VIOLATION"
    EFFECT_UNMAPPED = "EFFECT_UNMAPPED"


ALLOW_DECISIONS = {"ALLOW", "ALLOW_FULL", "ALLOW_PARTIAL"}
NON_ALLOW_DECISIONS = {"REDIRECT", "ESCALATE", "REFUSE", "HALT", "RESTART", "TRANSFER"}


@dataclass(frozen=True)
class ProtectedEffectAttempt:
    movement_id: str
    protected_effect_id: Optional[str]
    kernel_decision: str
    effect_formed: bool
    receipt_bound_to_effect: bool
    replayable_prevention: bool


@dataclass(frozen=True)
class EffectGuardReceipt:
    movement_id: str
    protected_effect_id: Optional[str]
    verdict: EffectVerdict
    effect_formed: bool
    prevention_proven: bool
    reason: str
    rule_trace: List[str]


def guard_protected_effect(attempt: ProtectedEffectAttempt) -> EffectGuardReceipt:
    """Resolve whether protected effect formation obeys the field-law rule."""

    trace: List[str] = [
        "effect.attempt.present",
        f"kernel_decision={attempt.kernel_decision}",
        f"effect_formed={attempt.effect_formed}",
    ]

    if not attempt.protected_effect_id:
        trace.append("effect.unmapped")
        return EffectGuardReceipt(
            movement_id=attempt.movement_id,
            protected_effect_id=attempt.protected_effect_id,
            verdict=EffectVerdict.EFFECT_UNMAPPED,
            effect_formed=attempt.effect_formed,
            prevention_proven=False,
            reason="Protected effect is unmapped; prevention cannot be proven.",
            rule_trace=trace,
        )

    trace.append("effect.mapped")

    if attempt.kernel_decision in ALLOW_DECISIONS:
        if attempt.effect_formed:
            trace.append("effect.allowed_and_formed")
            return EffectGuardReceipt(
                movement_id=attempt.movement_id,
                protected_effect_id=attempt.protected_effect_id,
                verdict=EffectVerdict.EFFECT_ALLOWED,
                effect_formed=True,
                prevention_proven=False,
                reason="Protected effect formed under an allow-class decision.",
                rule_trace=trace,
            )
        trace.append("effect.allowed_but_not_formed")
        return EffectGuardReceipt(
            movement_id=attempt.movement_id,
            protected_effect_id=attempt.protected_effect_id,
            verdict=EffectVerdict.EFFECT_ALLOWED,
            effect_formed=False,
            prevention_proven=False,
            reason="Protected effect did not form, but allow-class decision permitted it.",
            rule_trace=trace,
        )

    if attempt.effect_formed:
        trace.append("violation.effect_formed_without_allow")
        return EffectGuardReceipt(
            movement_id=attempt.movement_id,
            protected_effect_id=attempt.protected_effect_id,
            verdict=EffectVerdict.EFFECT_VIOLATION,
            effect_formed=True,
            prevention_proven=False,
            reason="Protected effect formed under non-allow decision.",
            rule_trace=trace,
        )

    if not attempt.receipt_bound_to_effect:
        trace.append("prevention.unproven.receipt_unbound")
        return EffectGuardReceipt(
            movement_id=attempt.movement_id,
            protected_effect_id=attempt.protected_effect_id,
            verdict=EffectVerdict.EFFECT_PREVENTED,
            effect_formed=False,
            prevention_proven=False,
            reason="Effect did not form, but receipt is not bound to protected effect.",
            rule_trace=trace,
        )

    if not attempt.replayable_prevention:
        trace.append("prevention.unproven.not_replayable")
        return EffectGuardReceipt(
            movement_id=attempt.movement_id,
            protected_effect_id=attempt.protected_effect_id,
            verdict=EffectVerdict.EFFECT_PREVENTED,
            effect_formed=False,
            prevention_proven=False,
            reason="Effect did not form, but prevention is not replayable.",
            rule_trace=trace,
        )

    trace.append("effect.prevented.proven")
    return EffectGuardReceipt(
        movement_id=attempt.movement_id,
        protected_effect_id=attempt.protected_effect_id,
        verdict=EffectVerdict.EFFECT_PREVENTED,
        effect_formed=False,
        prevention_proven=True,
        reason="Protected effect did not form under non-allow decision, with bound receipt and replayable prevention.",
        rule_trace=trace,
    )
