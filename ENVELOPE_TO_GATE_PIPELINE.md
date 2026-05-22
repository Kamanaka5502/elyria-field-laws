# Envelope to Gate Pipeline

## Core Claim

The envelope is the admissible handoff object between layered evidence/intention surfaces and the consequence gate.

The pipeline must carry movement, standing, protected effect, receipt basis, and replay requirements into the gate without flattening the field.

The gate does not receive loose context.

The gate receives a governed envelope.

---

## Why This Matters

A system cannot send raw documents, prompts, logs, dashboards, claims, or workflow notes directly into the gate and call that governance.

Those are upstream materials.

They must be transformed into a bounded envelope that preserves the dimensions required for consequence admission.

```text
raw input != governed envelope
governed envelope != final gate decision
```

The envelope is the carrier.

The gate is the resolver.

---

## Pipeline Shape

```text
Layered Inputs
  -> Canonical Envelope
  -> Standing Check
  -> Lawful Region Check
  -> Protected Effect Map
  -> Gate Resolution
  -> Receipt
  -> Legitimacy Replay
  -> Proof Surface Verdict
```

This is the clean path from layered material to consequence gate.

---

## Layered Inputs

Layered inputs may include:

```text
document evidence
operator intent
state snapshot
authority record
policy / law reference
lineage reference
capacity field
route / transfer condition
witness material
prior receipt
changed-condition event
```

These inputs are not yet gate-ready.

They must be canonicalized into an envelope.

---

## Canonical Envelope

A gate-ready envelope must include:

```text
envelope_id
corridor_id
movement_id
origin_state_hash
target_state_hash
authority_reference
evidence_reference
lineage_reference
capacity_reference
route_reference
transfer_reference
protected_effect_id
law_version
prior_receipt_hash
requested_outcome
failure_default
```

The envelope must be bounded, scoped, and replayable.

---

## Envelope Admission Rules

The envelope may enter the gate only if:

1. the movement object is present;
2. the corridor is identified;
3. authority reference is current;
4. evidence reference is fresh enough for the corridor;
5. lineage reference is intact;
6. protected effect is mapped;
7. law version is identified;
8. prior receipt is linked if continuity is claimed;
9. failure default is explicit;
10. replay material is sufficient.

If any required field is missing, the envelope does not enter the gate as admissible input.

It returns:

```text
ENVELOPE_INCOMPLETE
```

---

## Gate Input Object

The gate receives:

```text
GateInput = CanonicalEnvelope + CurrentFieldState
```

Where:

```text
CanonicalEnvelope = bounded proposed movement package
CurrentFieldState = live admissibility, capacity, authority, lineage, witness, and law conditions
```

The gate must not decide from envelope contents alone if live field state is required.

The envelope carries the claim.

The field resolves standing.

---

## Gate Resolution

The gate resolves:

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

The primary binding rule remains:

```text
BIND(M) is defined only when K(M) = ALLOW.
```

Partial, transfer, redirect, and restart require explicit bounded conditions and receipt/replay support.

---

## Envelope Failure Classes

Envelope failure may occur through:

```text
ENVELOPE_INCOMPLETE
CORRIDOR_UNBOUND
MOVEMENT_UNMAPPED
AUTHORITY_REFERENCE_MISSING
EVIDENCE_REFERENCE_STALE
LINEAGE_REFERENCE_BROKEN
CAPACITY_REFERENCE_MISSING
PROTECTED_EFFECT_UNMAPPED
LAW_VERSION_MISSING
PRIOR_RECEIPT_UNLINKED
REPLAY_MATERIAL_INSUFFICIENT
```

These are pre-gate failures.

They explain why the handoff object was not admissible for gate resolution.

---

## Gate Failure Classes

Once the envelope enters the gate, failures become gate-level outcomes:

```text
AUTHORITY_INVALID
EVIDENCE_STALE
STANDING_COLLAPSE
ROUTE_STANDING_FAILED
TRANSFER_CONTINUITY_FAILED
CAPACITY_FAILED
TRAJECTORY_BREACH
EFFECT_VIOLATION
LEGITIMACY_REPLAY_FAILED
```

Do not mix envelope failure with gate failure.

Envelope failure means the input object was not ready.

Gate failure means the movement was resolved and could not lawfully bind.

---

## Receipt Boundary

The receipt must bind:

```text
envelope_id
movement_id
corridor_id
gate_decision
protected_effect_id
failure_class
field_state_hash
law_version
prior_receipt_hash
replay_token
```

The receipt proves what the gate resolved from the governed envelope under current field conditions.

---

## Doctrine

The envelope is not the gate.

The envelope is the lawful carrier into the gate.

```text
Layers produce the envelope.
The envelope enters the gate.
The gate resolves consequence.
The receipt preserves why.
Replay proves it again.
```
