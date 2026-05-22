# Proof Failure Taxonomy

## Core Claim

A governance runtime must expose why proof failed.

Failure classes are not labels for decoration.

They are boundary outcomes that explain why movement could not lawfully acquire consequence status.

---

## Why This Matters

A system that returns only `DENY`, `FAIL`, or `BLOCKED` flattens the field.

That is insufficient.

The runtime must preserve which dimension failed and whether the failure came from standing, geometry, receipt, replay, route, transfer, capacity, or protected-effect control.

---

## Failure Families

### 1. Standing Failures

```text
AUTHORITY_DECAY
AUTHORITY_INVALID
EVIDENCE_STALE
SCOPE_NARROWED
STANDING_COLLAPSE
LAW_VERSION_CHANGED
```

Standing failures mean movement no longer has current lawful basis.

---

### 2. Continuity Failures

```text
CONTINUITY_BREAK
LINEAGE_BREAK
WITNESS_CONTINUITY_LOST
REENTRY_REQUIRED
REENTRY_INCOMPLETE
CONTINUITY_NOT_EARNED
```

Continuity failures mean persistence continued while lawful relation failed or became unproven.

---

### 3. Geometry Failures

```text
DIMENSION_FLATTENED
PROJECTION_ERROR
ENDPOINT_ONLY_VALIDATION
ROUTE_STANDING_FAILED
TRAJECTORY_BREACH
BOUNDARY_UNRESOLVED
CAPACITY_BOUNDARY_REACHED
```

Geometry failures mean the runtime collapsed lawful movement geometry into a local projection, endpoint pair, or insufficient path representation.

---

### 4. Basin / Capacity Failures

```text
BASIN_CAPACITY_FAILED
RECEIVER_CAPACITY_FAILED
NO_RECEIVING_BASIN
TRANSFER_PATH_INVALID
DRAIN_UNTRACKED
PARTIAL_BOUND_MISSING
```

Basin failures mean the field could not lawfully carry, transfer, receive, or partially admit the proposed movement.

---

### 5. Kernel Failures

```text
KERNEL_DECISION_MISSING
KERNEL_TRACE_INCOMPLETE
ALLOW_WITH_FAILED_GATE
BIND_STATUS_UNRESOLVED
NON_ALLOW_EFFECT_FORMED
```

Kernel failures mean the resolving decision or bind-status rule was not preserved.

---

### 6. Protected-Effect Failures

```text
PROTECTED_EFFECT_UNMAPPED
EFFECT_BOUNDARY_UNKNOWN
EFFECT_FORMED_WITHOUT_ALLOW
EFFECT_RECEIPT_UNBOUND
EFFECT_PREVENTION_NOT_REPLAYABLE
EFFECT_SCOPE_AMBIGUOUS
EFFECT_SUBSTITUTION_DETECTED
```

Protected-effect failures mean the system cannot prove what consequence was protected or whether it was prevented.

---

### 7. Receipt Failures

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

Receipt failures mean the witness object cannot support legitimacy replay.

---

### 8. Replay Failures

```text
REPLAY_INCOMPLETE
EXECUTION_REPLAY_ONLY
LEGITIMACY_REPLAY_FAILED
ADMISSIBILITY_RECONSTRUCTION_MISSING
AUTHORITY_REPLAY_MISSING
TRAJECTORY_REPLAY_MISSING
PROTECTED_EFFECT_REPLAY_MISSING
REPLAY_COLLAPSE
```

Replay failures mean the system reproduced outcome without preserving lawful consequence-state truth.

---

## Non-Flattening Rule

A failure response must not collapse all failures into one generic refusal label.

The runtime must identify the failed family and failed dimension.

```text
REFUSE is an outcome.
The failure class explains why consequence could not bind.
```

---

## Proof Requirement

Every non-ALLOW outcome must preserve at least:

```text
kernel outcome
failure family
specific failure class
failed dimension
protected effect status
receipt / replay status
```

Without this, refusal is a label, not governance proof.

---

## Doctrine

A system proves governance by preserving the shape of failure.

```text
What failed matters.
Why it failed matters.
What consequence did not form matters.
```
