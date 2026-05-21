# Elyria Field Laws

Elyria Field Laws is a proof-oriented doctrine and runtime skeleton for multidimensional consequence-bound movement governance.

The central question is not whether a system can execute, observe, approve, or log.

The central question is:

> Can inadmissible movement bind consequence?

This repository formalizes the field laws that prevent invalid movement from becoming real.

## Core Frame

Movement is not a workflow step.

Movement is a proposed consequence-state transition.

A proposed movement may only bind when the movement remains admissible across the governing field: authority, lineage, evidence, recovery posture, consequence exposure, witness/replay, harmonic trajectory, and regime-state geometry.

## Field Laws

1. **Non-Binding Movement** — invalid movement cannot acquire binding status.
2. **Legitimacy Replay Separation** — replayed outcome is not replayed legitimacy.
3. **Redirect Non-Laundering** — redirect is lawful only if admissibility distance decreases without bypassing hard gates.
4. **Hard Gate Non-Compensation** — operational strength cannot compensate for failed authority, lineage, evidence, consequence, or witness gates.
5. **Endpoint Is Not Path Validity** — valid origin and target do not prove lawful transition.

## Runtime Principle

```text
BIND(M) is defined only when K(M) = ALLOW.
```

If `K(M)` resolves to `REDIRECT`, `ESCALATE`, `REFUSE`, or `HALT`, the movement is non-binding.

## Repository Shape

```text
FIELD_LAWS.md
NON_BINDING_MOVEMENT_THEOREM.md
LEGITIMACY_REPLAY_SEPARATION.md
REDIRECT_NON_LAUNDERING.md
HARD_GATE_NON_COMPENSATION.md
ENDPOINT_NOT_PATH_VALIDITY.md
runtime/
  field_laws.py
  kernel.py
  admissibility_distance.py
proof_objects/
  valid_movement.json
  hard_gate_failure.json
  redirect_laundering.json
tests/
  test_field_laws.py
```

## Status

Initial proof-pack skeleton. This repo is intended to become a concrete proof surface for consequence-bound movement governance.