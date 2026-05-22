# Proof Surface Minimum

## Core Claim

A governance claim is not admissible unless the proof surface shows what could not happen.

The minimum proof surface must preserve the movement, the standing basis, the protected effect, the kernel decision, the receipt, and the legitimacy replay path.

Without these, the system may be useful, but it is not proving consequence-bound movement governance.

---

## Minimum Required Objects

A valid field-law proof surface must contain:

```text
movement object
lawful-region state
current standing basis
changed-condition state if any
kernel decision
protected-effect map
effect-prevention result
receipt / witness object
legitimacy replay object
failure class if not allowed
```

These are not documentation fields.

They are admissibility-preservation requirements.

---

## Movement Object

The proof surface must identify the proposed movement.

A movement is not a workflow step.

It is a proposed consequence-state transition.

If the movement object is missing, no consequence-bound proof exists.

---

## Standing Basis

The proof surface must show current standing at the boundary where consequence would form.

Required standing fields include:

```text
authority standing
evidence freshness
lineage integrity
capacity support
route standing
transfer standing
witness continuity
law version alignment
```

Historical approval is insufficient.

Current standing must be reconstructed.

---

## Protected Effect Map

The proof surface must identify the protected consequence that would form if movement acquired consequence status.

```text
EffectMap(M) -> E_protected
```

No protected-effect map means no prevention proof.

---

## Kernel Decision

The proof surface must preserve the kernel decision:

```text
ALLOW
ALLOW_PARTIAL
TRANSFER
REDIRECT
ESCALATE
REFUSE
HALT
RESTART
```

The binding rule remains:

```text
BIND(M) is defined only when K(M) = ALLOW.
```

Partial binding must explicitly identify the allowed and refused fractions.

---

## Effect Prevention

If the kernel decision is not allow-class, the protected effect must remain unformed.

```text
K(M) != ALLOW -> E_protected does not form
```

If the protected effect forms anyway, the runtime has produced an effect violation.

---

## Receipt Requirements

A receipt must bind to:

```text
movement object
standing basis
kernel decision
protected effect
failure class
receipt time / law version
witness basis
replay token
```

A receipt that records only a decision preserves event history.

It does not prove consequence-bound governance.

---

## Legitimacy Replay Requirement

Replay must reconstruct admissibility state, not merely terminal outcome.

```text
same outcome != same legitimacy
```

The replay object must preserve:

```text
movement hash
authority hash
evidence hash
lineage hash
capacity / admissibility hash
trajectory hash
kernel resolution hash
protected-effect hash
law version hash
```

---

## Failure Classes

A minimum proof surface must expose failure classes directly.

Examples:

```text
AUTHORITY_DECAY
EVIDENCE_STALE
SCOPE_NARROWED
CONTINUITY_BREAK
STANDING_COLLAPSE
REPLAY_INCOMPLETE
RECEIPT_UNBOUND
DIMENSION_FLATTENED
EFFECT_PREVENTED
EFFECT_VIOLATION
PROTECTED_EFFECT_UNMAPPED
```

Failure classes are not labels for decoration.

They explain why consequence could not lawfully bind.

---

## Doctrine

A proof surface is sufficient only when it shows:

```text
what movement was proposed
what standing existed
what effect was protected
what decision was made
what consequence was prevented
what replay reconstructs
```

Anything less is a control surface, not consequence-bound movement governance.
