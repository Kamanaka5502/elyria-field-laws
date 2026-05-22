# Field Law Corpus Index

## Purpose

This index maps the Elyria Field Laws corpus into a coherent consequence-governance architecture.

The repo is not a collection of essays.

It is a layered proof corpus for lawful movement, protected-effect prevention, receipt constitution, and legitimacy replay.

---

## Core Invariant

```text
BIND(M) is defined only when K(M) = ALLOW.
```

Everything else is non-binding unless a bounded partial or transfer relation is explicitly resolved, receipted, and replayable.

---

## Layer 1 — Foundational Field Laws

```text
FIELD_LAWS.md
NON_BINDING_MOVEMENT_THEOREM.md
HARD_GATE_NON_COMPENSATION.md
REDIRECT_NON_LAUNDERING.md
```

This layer defines the base law: failed movement cannot acquire consequence status.

---

## Layer 2 — Lawful Movement Geometry

```text
LAWFUL_MOVEMENT_GEOMETRY.md
PROJECTION_ERROR.md
ENDPOINT_NOT_PATH_VALIDITY.md
ROUTE_STANDING_THEOREM.md
TRAJECTORY_BREACH_THEOREM.md
```

This layer prevents flattening into diagrams, timelines, dashboards, endpoint validation, or local witness artifacts.

Movement is traversal through lawful geometry, not a workflow step.

---

## Layer 3 — Basin, Capacity, Boundary

```text
BASIN_HOLDING.md
CAPACITY_BOUNDARY_THEOREM.md
BOUNDARY_HOLDING_THEOREM.md
TRANSFER_CONTINUITY_THEOREM.md
THERMAL_MOVEMENT_GOVERNANCE.md
PARTIAL_BINDING_THEOREM.md
```

This layer defines holding, capacity, transfer, thermal consequence, and bounded partial consequence admission.

Core capacity law:

```text
Phi(x) = C(x) - M(x)
```

Core lawful region:

```text
R = { z | A(z) >= 0, Phi(z) >= 0, U(z) = 1 }
```

---

## Layer 4 — Standing and Continuity

```text
STANDING_DECAY_THEOREM.md
CHANGED_CONDITION_REENTRY_THEOREM.md
REENTRY_KERNEL_THEOREM.md
CONTINUITY_EARNING_THEOREM.md
```

This layer defines standing as live, not historical.

```text
Standing is live.
Approval is historical.
```

Changed conditions force reentry; continuity must be earned under current field conditions.

---

## Layer 5 — Protected Effect Governance

```text
PROTECTED_EFFECT_MAP.md
EFFECT_PREVENTION_THEOREM.md
CONTROL_SURFACE_COLLAPSE_THEOREM.md
```

This layer defines protected effect identity and prevention proof.

Core effect law:

```text
K(M) != ALLOW -> E_protected does not form
```

No protected-effect map means no prevention proof.

---

## Layer 6 — Receipts and Replay

```text
RUNTIME_RECEIPT_CONSTITUTION.md
LEGITIMACY_REPLAY_SEPARATION.md
REPLAY_COLLAPSE_THEOREM.md
```

This layer separates execution replay from legitimacy replay.

```text
same outcome != same admissibility
same receipt != same legitimacy
same terminal state != same lawful movement path
```

A receipt without standing is a record.

A receipt with standing, effect, decision, and replay is governance proof.

---

## Layer 7 — Proof Surface and Failure Taxonomy

```text
PROOF_SURFACE_MINIMUM.md
PROOF_FAILURE_TAXONOMY.md
```

This layer defines the minimum admissible proof surface and the shape of failure.

```text
REFUSE is an outcome.
The failure class explains why consequence could not bind.
```

---

## Runtime Modules

```text
runtime/kernel.py
runtime/admissibility_region.py
runtime/partial_binding.py
runtime/replay_verifier.py
runtime/effect_guard.py
runtime/proof_surface.py
```

These modules operationalize the corpus:

```text
movement resolution
lawful-region evaluation
partial consequence admission
legitimacy replay verification
protected-effect guarding
proof-surface verification
```

---

## Tests

```text
tests/test_field_laws.py
tests/test_admissibility_region.py
tests/test_partial_binding.py
tests/test_replay_verifier.py
tests/test_effect_guard.py
tests/test_proof_surface.py
```

Tests convert doctrine into replayable proof behavior.

---

## Proof Objects

```text
proof_objects/valid_movement.json
proof_objects/hard_gate_failure.json
proof_objects/redirect_laundering.json
proof_objects/legitimacy_replay_valid.json
proof_objects/execution_replay_only.json
proof_objects/valid_proof_surface.json
```

Proof objects serialize the difference between valid governance proof and collapsed control surfaces.

---

## Corpus Claim

This repo defines a consequence-bound movement governance corpus.

It does not prove governance by naming gates.

It proves governance by preserving the relation between movement, standing, consequence, prevention, receipt, and replay.

```text
The proof is not the layer.
The proof is what cannot happen.
```
