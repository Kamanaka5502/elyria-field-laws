# Effect Prevention Theorem

## Core Claim

The proof of movement governance is not that a system can describe, log, reverse, or explain an effect.

The proof is that a protected effect did not form when movement lacked standing.

Effect prevention is the observable proof surface of consequence-bound governance.

---

## Why This Matters

Many systems claim governance because they can produce a record after execution.

That is not enough.

A record can show that an effect happened.

A rollback can show that an effect was later reversed.

A log can show that the system observed the event.

None of those prove that inadmissible movement was prevented from acquiring consequence status.

---

## Formal Context

Let `M` be a proposed movement.

Let `E_protected` be the protected effect that would form if movement acquired consequence status.

The kernel rule remains:

```text
BIND(M) is defined only when K(M) = ALLOW.
```

Effect prevention requires:

```text
K(M) != ALLOW -> E_protected does not form
```

---

## Theorem

A runtime proves consequence-bound movement governance only when it can show that protected effect formation was prevented for non-admissible movement.

If:

```text
K(M) in {REDIRECT, ESCALATE, REFUSE, HALT}
```

then:

```text
E_protected must remain unformed
```

If the protected effect forms anyway, the system did not govern movement.

It documented execution.

---

## Prevention Versus Reversal

Prevention is not rollback.

Rollback occurs after effect formation.

Prevention occurs before protected effect formation.

```text
prevented effect != reversed effect
```

A rollback may be useful.

But rollback is not proof that invalid movement never acquired consequence status.

---

## Proof Requirements

An effect-prevention proof must preserve:

1. proposed movement object;
2. protected effect map;
3. kernel decision;
4. standing basis;
5. refusal, halt, redirect, or escalation reason;
6. proof that protected effect did not form;
7. receipt / witness object;
8. replay path reconstructing the same prevention basis.

Without the protected-effect map, the system cannot prove what was prevented.

Without replay, the system cannot prove why prevention occurred.

---

## Failure Classes

Effect-prevention failure may occur through:

```text
PROTECTED_EFFECT_UNMAPPED
EFFECT_FORMED_WITHOUT_ALLOW
RECEIPT_UNBOUND_TO_EFFECT
PREVENTION_NOT_REPLAYABLE
ROLLBACK_MISTAKEN_FOR_PREVENTION
OBSERVATION_MISTAKEN_FOR_GOVERNANCE
```

These are boundary failures, not reporting defects.

---

## Relation to Movement Governance

Movement governance is proven by what cannot happen.

A system does not prove governance because it contains a gate, log, receipt, or workflow.

It proves governance only when failed movement cannot form protected consequence.

---

## Doctrine

The prevented consequence is the proof surface.

```text
If invalid movement can still form protected effect,
the system is not governing consequence.
```
