# Dashboard Proof Surface Specification

## Purpose

This file defines the operator-facing dashboard surface for Elyria Field Laws.

The dashboard is not the governance layer.

The dashboard is a witness projection of the consequence-governance proof surface.

It must show the corridor state without flattening the runtime into a policy panel, audit log, or decorative visualization.

---

## Core Rule

```text
Dashboard = witness projection
Gate = consequence resolver
Receipt = proof object
Replay = legitimacy reconstruction
```

The dashboard may display governance.

It does not create governance.

---

## Required Dashboard Zones

### 1. Corridor Identity

The dashboard must show:

```text
corridor_id
movement_id
event_id
envelope_id
profile
runtime mode
```

Example profile:

```text
34ms_hot_path
```

Example runtime mode:

```text
FAST_PATH
SAFE_PATH_REQUIRED
REENTRY_REQUIRED
ESCALATE_LATENCY
```

---

### 2. Movement Object

The dashboard must display the proposed movement:

```text
origin_state
target_state
movement_type
requested_outcome
protected_effect_id
```

The movement object must remain visible because consequence governance begins with proposed movement, not with dashboard status.

---

### 3. Envelope Status

The dashboard must show whether the event became a gate-ready envelope.

Possible states:

```text
EVENT_CAPTURED
ENVELOPE_CREATED
ENVELOPE_READY
ENVELOPE_INCOMPLETE
ENVELOPE_REJECTED
```

Required fields:

```text
envelope_hash
missing_fields
failure_class
prior_receipt_hash
```

---

### 4. Standing Status

The dashboard must show current standing, not historical approval.

Standing dimensions:

```text
authority_standing
evidence_freshness
lineage_integrity
capacity_support
route_standing
transfer_standing
witness_continuity
law_version_alignment
standing_ttl_ms
standing_age_ms
```

Visual rule:

```text
green = current
amber = warning / nearing expiry
red = failed or stale
```

---

### 5. Lawful Region Geometry

The dashboard must show the lawful-region state:

```text
R = { z | A(z) >= 0, Phi(z) >= 0, U(z) = 1 }
```

Display values:

```text
A(z)
Phi(z)
U(z)
inside_R
region_verdict
```

Possible region verdicts:

```text
INSIDE_R
OUTSIDE_R
PARTIAL_CAPACITY
```

The dashboard may visualize geometry, but it must not treat the visualization as proof.

---

### 6. Gate Resolution

The dashboard must show the kernel decision:

```text
ALLOW
ALLOW_PARTIAL
TRANSFER
REDIRECT
ESCALATE
REFUSE
HALT
RESTART
REENTRY_REQUIRED
```

Core binding rule must be visible:

```text
BIND(M) is defined only when K(M) = ALLOW.
```

Non-allow outcomes must show a failure class.

---

### 7. Protected Effect Guard

The dashboard must show protected-effect status:

```text
protected_effect_id
effect_formed
effect_verdict
prevention_proven
receipt_bound_to_effect
replayable_prevention
```

Possible effect verdicts:

```text
EFFECT_ALLOWED
EFFECT_PREVENTED
EFFECT_VIOLATION
EFFECT_UNMAPPED
```

Core rule:

```text
K(M) != ALLOW -> E_protected does not form.
```

---

### 8. Receipt Chain

The dashboard must show receipt state:

```text
receipt_id
receipt_hash
receipt_parent_hash
movement_hash
standing_hash
protected_effect_hash
kernel_resolution_hash
replay_token
receipt_status
```

Possible receipt states:

```text
RECEIPT_ISSUED
RECEIPT_INCOMPLETE
RECEIPT_UNBOUND
RECEIPT_CHAIN_RISK
```

A receipt without standing is a record.

A receipt with standing, effect, decision, and replay is governance proof.

---

### 9. Legitimacy Replay

The dashboard must show replay status:

```text
LEGITIMACY_REPLAY_VALID
EXECUTION_REPLAY_ONLY
REPLAY_INVALID
```

It must display missing replay dimensions when replay fails:

```text
movement_hash
authority_hash
evidence_hash
lineage_hash
capacity_hash
trajectory_hash
kernel_resolution_hash
protected_effect_hash
law_version_hash
```

Core rule:

```text
same outcome != same legitimacy
```

---

### 10. Latency / Lag Panel

The dashboard must show the current latency profile:

```text
34ms_hot_path
80ms_optimized_path
200ms_outer_failsafe
```

For the 34 ms profile, show:

```text
target_total_ms = 34
preferred_ceiling_ms = 50
escalation_threshold_ms = 75
hard_ceiling_ms = 100
outer_failsafe_ms = 200
```

Stage latency map:

```text
L1 Event Intake
L2 Classification
L3 Canonical Envelope
L4 Completeness Check
L5 Standing Assembly
L6 Field-State Binding
L7 Lawful Region Evaluation
L8 Protected Effect Mapping
L9 Gate Input Construction
L10 Gate Resolution
L11 Protected Effect Guard
L12 Receipt Issuance
L13 Legitimacy Replay
L14 Proof Surface Verdict
L15 Outcome Publication
```

Latency verdicts:

```text
LATENCY_OK
LATENCY_WARN
ESCALATE_LATENCY
LATENCY_REENTRY_REQUIRED
LATENCY_REFUSE
```

---

### 11. Proof Surface Verdict

The dashboard must show the final proof surface verdict:

```text
PROOF_SURFACE_VALID
PROOF_SURFACE_INCOMPLETE
CONTROL_SURFACE_ONLY
```

This is the final operator-visible proof state.

The dashboard must distinguish:

```text
valid governed corridor
```

from:

```text
control surface collapse
```

---

## Dashboard Failure Rules

The dashboard must not hide these failures:

```text
PROTECTED_EFFECT_UNMAPPED
EFFECT_FORMED_WITHOUT_ALLOW
EXECUTION_REPLAY_ONLY
RECEIPT_UNBOUND_TO_EFFECT
FAILURE_CLASS_MISSING
STANDING_TTL_EXPIRED
FIELD_HASH_CHANGED
REPLAY_MATERIAL_MISSING
```

If any of these occur, the dashboard must show the corridor as incomplete, collapsed, reentry-required, escalated, refused, or halted.

Never show green for uncertainty.

---

## Visual Hierarchy

Recommended dashboard order:

```text
1. Final proof surface verdict
2. Gate decision
3. Protected effect status
4. Standing status
5. Lawful-region geometry
6. Receipt/replay status
7. Latency profile
8. Failure class / safe-path reason
```

The operator should see consequence status before decorative geometry.

---

## Anti-Flattening Rule

The dashboard must never reduce the system to:

```text
approved / denied
pass / fail
safe / unsafe
red / green only
```

Every non-allow outcome must preserve:

```text
failure family
failure class
failed dimension
protected effect status
receipt status
replay status
```

---

## Closing Doctrine

The dashboard is a surface.

The proof is the prevented consequence and replayable admissibility basis.

```text
A dashboard may witness the field.
It may not replace the field.
```
