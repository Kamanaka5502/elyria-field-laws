# Event Intake to Gate Pipeline

## Purpose

This document defines the clear event-intake path from raw event material into a governed envelope, through the pipeline, into the consequence gate, and out into receipts, replay, and final outcome.

The event does not go directly to the gate.

The event is admitted into intake, canonicalized into an envelope, checked across standing and field conditions, then resolved by the gate.

---

## Core Pipeline

```text
Raw Event
  -> Event Intake
  -> Event Classification
  -> Canonical Envelope
  -> Envelope Completeness Check
  -> Standing Assembly
  -> Field-State Binding
  -> Lawful Region Evaluation
  -> Protected Effect Mapping
  -> Gate Input Construction
  -> Gate Resolution
  -> Protected Effect Guard
  -> Receipt Issuance
  -> Legitimacy Replay
  -> Proof Surface Verdict
  -> Final Outcome
```

---

## Stage 1 — Raw Event

A raw event is any incoming trigger, claim, request, state change, operator intent, system signal, document update, movement proposal, thermal action, transfer attempt, route change, or changed-condition event.

Examples:

```text
operator requests deployment
certificate arrives
policy changes
sensor reports thermal pressure
authority expires
evidence changes
transfer route closes
protected effect is requested
system attempts commit
```

Raw event status:

```text
NOT_GATE_READY
```

Raw event material must never be treated as a gate decision.

---

## Stage 2 — Event Intake

Event intake captures the event without flattening it.

Minimum intake fields:

```text
event_id
event_type
source
received_at
corridor_hint
actor_or_system
raw_payload_reference
claimed_movement
claimed_effect
prior_receipt_reference
```

Intake result:

```text
EVENT_CAPTURED
EVENT_REJECTED_UNREADABLE
```

---

## Stage 3 — Event Classification

The event must be classified by governance role.

Classification types:

```text
MOVEMENT_PROPOSAL
STANDING_CHANGE
AUTHORITY_CHANGE
EVIDENCE_UPDATE
LINEAGE_EVENT
CAPACITY_EVENT
ROUTE_EVENT
TRANSFER_EVENT
WITNESS_EVENT
LAW_VERSION_EVENT
PROTECTED_EFFECT_REQUEST
REPLAY_REQUEST
```

Classification receipt fields:

```text
event_id
event_type
classification
required_checks
corridor_id
classification_reason
```

---

## Stage 4 — Canonical Envelope

The intake material becomes a gate-carrying object only after canonicalization.

Canonical envelope fields:

```text
envelope_id
event_id
corridor_id
movement_id
movement_type
origin_state_hash
target_state_hash
authority_reference
evidence_reference
lineage_reference
capacity_reference
route_reference
transfer_reference
witness_reference
protected_effect_id
law_version
prior_receipt_hash
requested_outcome
failure_default
replay_material_reference
```

Envelope status:

```text
ENVELOPE_CREATED
```

The envelope is the lawful carrier. It is not the gate decision.

---

## Stage 5 — Envelope Completeness Check

Possible outcomes:

```text
ENVELOPE_READY
ENVELOPE_INCOMPLETE
ENVELOPE_REJECTED
```

Envelope failure classes:

```text
CORRIDOR_UNBOUND
MOVEMENT_UNMAPPED
AUTHORITY_REFERENCE_MISSING
EVIDENCE_REFERENCE_MISSING
LINEAGE_REFERENCE_MISSING
CAPACITY_REFERENCE_MISSING
PROTECTED_EFFECT_UNMAPPED
LAW_VERSION_MISSING
PRIOR_RECEIPT_UNLINKED
REPLAY_MATERIAL_INSUFFICIENT
```

Envelope receipt fields:

```text
envelope_id
event_id
corridor_id
status
missing_fields
failure_class
canonical_hash
```

---

## Stage 6 — Standing Assembly

Standing assembly reconstructs current standing for the event.

Standing dimensions:

```text
authority standing
evidence freshness
lineage integrity
capacity support
route standing
transfer standing
witness continuity
law version alignment
prior receipt continuity
```

Standing outcomes:

```text
STANDING_ASSEMBLED
STANDING_INCOMPLETE
STANDING_FAILED
```

Standing receipt fields:

```text
envelope_id
movement_id
authority_hash
evidence_hash
lineage_hash
capacity_hash
route_hash
transfer_hash
witness_hash
law_version_hash
standing_status
failed_dimension
```

---

## Stage 7 — Field-State Binding

The envelope must bind to current field state.

Gate-ready input is:

```text
GateInput = CanonicalEnvelope + CurrentFieldState
```

Current field state includes:

```text
current authority
current evidence
current lineage
current capacity
current route state
current transfer state
current witness state
current law version
current protected-effect boundary
```

Field-state binding outcome:

```text
FIELD_BOUND
FIELD_BINDING_FAILED
```

---

## Stage 8 — Lawful Region Evaluation

The movement is evaluated against lawful continuation geometry.

Core formula:

```text
R = { z | A(z) >= 0, Phi(z) >= 0, U(z) = 1 }
```

Capacity formula:

```text
Phi(x) = C(x) - M(x)
```

Possible region outcomes:

```text
INSIDE_R
OUTSIDE_R
PARTIAL_CAPACITY
```

Region receipt fields:

```text
state_id
A_z
Phi_z
U_z
inside_R
region_verdict
reason
rule_trace
```

---

## Stage 9 — Protected Effect Mapping

The gate must know what consequence is protected.

Required mapping:

```text
EffectMap(M) -> E_protected
```

Protected-effect outcomes:

```text
EFFECT_MAPPED
PROTECTED_EFFECT_UNMAPPED
EFFECT_SCOPE_AMBIGUOUS
EFFECT_BOUNDARY_UNKNOWN
```

Effect-map receipt fields:

```text
movement_id
protected_effect_id
effect_boundary
effect_scope
effect_hash
mapping_status
```

No protected-effect map means no prevention proof.

---

## Stage 10 — Gate Input Construction

The gate input is built only after the envelope, standing, field state, lawful region, and protected effect are present.

Gate input fields:

```text
gate_input_id
envelope_id
movement_id
corridor_id
current_field_state_hash
standing_receipt_hash
region_receipt_hash
protected_effect_hash
prior_receipt_hash
failure_default
```

Gate input outcome:

```text
GATE_INPUT_READY
GATE_INPUT_REJECTED
```

---

## Stage 11 — Gate Resolution

The gate resolves whether proposed movement may acquire consequence status.

Gate outcomes:

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

Primary binding rule:

```text
BIND(M) is defined only when K(M) = ALLOW.
```

Protected-effect prevention rule:

```text
K(M) != ALLOW -> E_protected does not form
```

Gate receipt fields:

```text
gate_receipt_id
gate_input_id
envelope_id
movement_id
corridor_id
kernel_decision
bind_defined
failure_class
hard_gate_state
admissibility_distance
rule_trace
```

---

## Stage 12 — Protected Effect Guard

After gate resolution, the protected-effect guard verifies effect behavior.

Effect guard outcomes:

```text
EFFECT_ALLOWED
EFFECT_PREVENTED
EFFECT_VIOLATION
EFFECT_UNMAPPED
```

Rules:

```text
ALLOW -> protected effect may form
NON_ALLOW -> protected effect must not form
```

Effect guard receipt fields:

```text
movement_id
protected_effect_id
kernel_decision
effect_formed
effect_verdict
prevention_proven
receipt_bound_to_effect
replayable_prevention
```

---

## Stage 13 — Runtime Receipt Issuance

The runtime receipt binds the full corridor decision.

Required receipt fields:

```text
receipt_id
event_id
envelope_id
movement_id
corridor_id
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
prior_receipt_hash
receipt_hash
replay_token
```

Receipt outcome:

```text
RECEIPT_ISSUED
RECEIPT_INCOMPLETE
RECEIPT_UNBOUND
```

Doctrine:

```text
Receipt without standing is record.
Receipt with standing, effect, decision, and replay is governance proof.
```

---

## Stage 14 — Legitimacy Replay

Replay must reconstruct admissibility, not just outcome.

Replay outcomes:

```text
LEGITIMACY_REPLAY_VALID
EXECUTION_REPLAY_ONLY
REPLAY_INVALID
```

Replay receipt fields:

```text
replay_id
terminal_outcome_hash
movement_hash
authority_hash
evidence_hash
lineage_hash
capacity_hash
trajectory_hash
kernel_resolution_hash
protected_effect_hash
law_version_hash
replay_verdict
missing_fields
```

Rule:

```text
same outcome != same legitimacy
```

---

## Stage 15 — Proof Surface Verdict

The final proof surface verifies whether the event-to-gate pipeline proved governance or collapsed into control.

Final verdicts:

```text
PROOF_SURFACE_VALID
PROOF_SURFACE_INCOMPLETE
CONTROL_SURFACE_ONLY
```

Final proof-surface receipt fields:

```text
surface_id
event_id
envelope_id
movement_id
kernel_decision
protected_effect_id
effect_verdict
receipt_id
replay_verdict
failure_class
proof_surface_verdict
proof_surface_valid
```

---

## Final Outcome Matrix

### Valid Allow

```text
ENVELOPE_READY
STANDING_ASSEMBLED
INSIDE_R
EFFECT_MAPPED
ALLOW
EFFECT_ALLOWED
RECEIPT_ISSUED
LEGITIMACY_REPLAY_VALID
PROOF_SURFACE_VALID
```

Meaning:

```text
Movement had current standing and protected effect may form.
```

### Valid Refuse / Prevented Effect

```text
ENVELOPE_READY
STANDING_FAILED or OUTSIDE_R
EFFECT_MAPPED
REFUSE
EFFECT_PREVENTED
RECEIPT_ISSUED
LEGITIMACY_REPLAY_VALID
PROOF_SURFACE_VALID
```

Meaning:

```text
Movement lacked standing and protected effect did not form.
```

### Envelope Failure

```text
ENVELOPE_INCOMPLETE
```

Meaning:

```text
The event did not become gate-ready input. No gate decision should be claimed.
```

### Control Surface Collapse

```text
NON_ALLOW + EFFECT_VIOLATION
```

or:

```text
EXECUTION_REPLAY_ONLY
```

or:

```text
failure_class missing
```

Final verdict:

```text
CONTROL_SURFACE_ONLY
```

Meaning:

```text
The system may have managed execution, but it did not prove consequence-bound governance.
```

---

## Full Doctrine

```text
Event intake captures.
Envelope canonicalizes.
Standing assembles.
Field state binds.
The gate resolves.
The protected effect guard verifies consequence behavior.
The receipt preserves why.
Replay proves it again.
The proof surface decides whether governance was proven.
```

This is the event-intake-to-gate pipeline.
