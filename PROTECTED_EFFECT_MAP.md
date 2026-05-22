# Protected Effect Map

## Core Claim

A protected effect must be mapped before it can be governed.

A runtime cannot prove prevented consequence unless it identifies the protected effect that would have formed if movement acquired consequence status.

---

## Why This Matters

A system may refuse, halt, redirect, or escalate a movement while still failing to prove what consequence was prevented.

That is not enough.

Without a protected-effect map, refusal is only a decision label.

With a protected-effect map, refusal becomes consequence-bound proof.

---

## Formal Object

Let `M` be a proposed movement.

Let `E_protected` be the effect that must not form unless movement is admitted.

```text
EffectMap(M) -> E_protected
```

The protected effect map binds movement to the consequence surface that would become real if the movement were allowed.

---

## Theorem

A runtime can prove effect prevention only if it preserves:

1. the proposed movement object;
2. the protected effect identity;
3. the consequence boundary where effect would form;
4. the kernel decision;
5. the standing basis;
6. the proof that `E_protected` did not form when `K(M) != ALLOW`;
7. the receipt or witness object;
8. replay reconstruction of the same prevention basis.

If `E_protected` is unmapped, prevention is not proven.

---

## Effect Formation Rule

The field-law rule remains:

```text
BIND(M) is defined only when K(M) = ALLOW.
```

The protected-effect rule is:

```text
K(M) != ALLOW -> E_protected must not form
```

If `E_protected` forms under any non-ALLOW outcome, the system did not govern consequence.

It only recorded execution.

---

## Failure Classes

Protected-effect mapping may fail through:

```text
PROTECTED_EFFECT_UNMAPPED
EFFECT_BOUNDARY_UNKNOWN
EFFECT_FORMED_WITHOUT_ALLOW
EFFECT_RECEIPT_UNBOUND
EFFECT_PREVENTION_NOT_REPLAYABLE
EFFECT_SCOPE_AMBIGUOUS
EFFECT_SUBSTITUTION_DETECTED
```

These are not reporting defects.

They are consequence-boundary failures.

---

## Relation to Receipts

A receipt must bind to the protected effect.

A receipt that records only movement and decision, without identifying the protected consequence, cannot prove prevention.

It preserves event history, not effect governance.

---

## Relation to Replay

Legitimacy replay must reconstruct the protected-effect map.

Same refusal is not enough.

Same outcome is not enough.

Replay must prove that the same protected effect remained unformed under the same non-admissible movement condition.

---

## Doctrine

The system cannot prove what it prevented unless it knows what consequence was protected.

```text
No protected-effect map, no prevention proof.
```
