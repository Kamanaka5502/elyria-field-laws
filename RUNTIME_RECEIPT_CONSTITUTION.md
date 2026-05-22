# Runtime Receipt Constitution

## Core Claim

A receipt is not a record.

A receipt is a bounded witness object that must preserve the lawful basis of movement, consequence prevention, protected-effect status, and replay legitimacy.

If a receipt cannot reconstruct standing, it is event history, not governance proof.

---

## Why This Matters

Many systems generate receipts after decisions.

That is insufficient.

A receipt that records only a terminal outcome may prove that something was labeled, logged, or decided.

It does not prove that consequence was lawfully admitted or prevented.

---

## Minimum Receipt Object

A valid runtime receipt must bind:

```text
receipt_id
movement_id
movement_hash
origin_state_hash
target_state_hash
authority_hash
evidence_hash
lineage_hash
capacity_hash
route_hash
transfer_hash
witness_hash
law_version_hash
kernel_decision
protected_effect_id
protected_effect_hash
effect_status
failure_class
replay_token
receipt_parent_hash
receipt_hash
```

These fields are not decorative metadata.

They preserve the admissibility structure required for legitimacy replay.

---

## Receipt Binding Rule

A receipt must bind to the protected effect.

```text
Receipt(M) must include EffectMap(M) -> E_protected
```

If the receipt does not identify the protected effect, it cannot prove effect prevention.

If the receipt does not identify the kernel decision, it cannot prove bind status.

If the receipt does not identify standing basis, it cannot prove admissibility.

---

## Replay Requirement

A receipt must support legitimacy replay.

It must allow reconstruction of:

```text
movement object
standing basis
lawful-region state
kernel decision
protected-effect map
effect-prevention result
failure class
continuity state
```

A receipt that can reproduce only the terminal decision is execution replay only.

---

## Parent Hash Continuity

A receipt may chain to a prior receipt through:

```text
receipt_parent_hash
```

This preserves continuity across standing change, reentry, transfer, partial admission, halt, restart, or effect prevention.

A broken chain must be treated as a continuity event, not ignored.

---

## Failure Classes

Receipt failure may occur through:

```text
RECEIPT_UNBOUND_TO_MOVEMENT
RECEIPT_UNBOUND_TO_EFFECT
RECEIPT_MISSING_STANDING_BASIS
RECEIPT_MISSING_KERNEL_DECISION
RECEIPT_MISSING_REPLAY_TOKEN
RECEIPT_CHAIN_BREAK
RECEIPT_TERMINAL_ONLY
RECEIPT_DIMENSION_FLATTENED
```

These are governance proof failures.

---

## Relation to Field Laws

The kernel rule remains:

```text
BIND(M) is defined only when K(M) = ALLOW.
```

The receipt must preserve why `K(M)` was reached and whether protected effect formation was admitted or prevented.

---

## Doctrine

A receipt is sufficient only when it can replay legitimacy.

```text
Receipt without standing is record.
Receipt with standing, effect, decision, and replay is governance proof.
```
