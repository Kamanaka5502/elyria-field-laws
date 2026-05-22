# Corridor Demo Script

## Purpose

This demo script explains the first end-to-end Elyria Field Laws corridor.

The demo proves one bounded consequence-governance corridor:

```text
one movement
one protected effect
one kernel decision
one receipt
one legitimacy replay
one proof-surface verdict
```

The goal is not to show that the system runs.

The goal is to show what cannot happen.

---

## Demo Claim

A corridor is governed only when inadmissible movement cannot form protected consequence.

The demo must prove both sides:

```text
ALLOW -> protected effect may form -> legitimacy replay valid -> proof surface valid
```

and:

```text
NON_ALLOW -> protected effect prevented -> legitimacy replay valid -> proof surface valid
```

It must also show collapse cases where the system becomes control-surface-only.

---

## Demo Path

The demo follows this runtime chain:

```text
Movement
  -> Lawful Region Evaluation
  -> Kernel Resolution
  -> Protected Effect Guard
  -> Legitimacy Replay Verifier
  -> Proof Surface Verifier
  -> Corridor Receipt
```

Implemented by:

```text
runtime/corridor_runner.py
```

Tested by:

```text
tests/test_corridor_runner.py
```

---

## Case 1 — Valid Allow Corridor

Expected chain:

```text
region_verdict = INSIDE_R
kernel_decision = ALLOW
effect_verdict = EFFECT_ALLOWED
replay_verdict = LEGITIMACY_REPLAY_VALID
proof_surface_verdict = PROOF_SURFACE_VALID
proof_surface_valid = true
```

Meaning:

```text
The movement had standing.
The protected effect was mapped.
The effect formed only under allow-class decision.
The receipt/replay path preserved legitimacy.
```

---

## Case 2 — Valid Refuse Corridor With Effect Prevention

Expected chain:

```text
kernel_decision = REFUSE
effect_verdict = EFFECT_PREVENTED
replay_verdict = LEGITIMACY_REPLAY_VALID
proof_surface_verdict = PROOF_SURFACE_VALID
proof_surface_valid = true
```

Meaning:

```text
The movement failed standing.
The protected effect did not form.
The failure class was preserved.
Legitimacy replay reconstructed the refusal basis.
```

This is the decisive governance proof.

---

## Case 3 — Effect Violation Collapse

Expected chain:

```text
kernel_decision = REFUSE
effect_verdict = EFFECT_VIOLATION
proof_surface_verdict = CONTROL_SURFACE_ONLY
proof_surface_valid = false
```

Meaning:

```text
The runtime refused the movement, but protected effect formed anyway.
The system did not govern consequence.
It collapsed into a control surface.
```

---

## Case 4 — Missing Protected Effect Map

Expected chain:

```text
effect_verdict = EFFECT_UNMAPPED
proof_surface_verdict = PROOF_SURFACE_INCOMPLETE
proof_surface_valid = false
```

Meaning:

```text
The system cannot prove what consequence was protected.
No protected-effect map means no prevention proof.
```

---

## Case 5 — Execution Replay Only

Expected chain:

```text
replay_verdict = EXECUTION_REPLAY_ONLY
proof_surface_verdict = CONTROL_SURFACE_ONLY
proof_surface_valid = false
```

Meaning:

```text
The terminal outcome may replay.
The admissibility basis does not.
Same outcome is not same legitimacy.
```

---

## Case 6 — Missing Failure Class

Expected chain:

```text
kernel_decision = REFUSE
proof_surface_verdict = CONTROL_SURFACE_ONLY
proof_surface_valid = false
```

Meaning:

```text
REFUSE is only an outcome.
The failure class explains why consequence could not bind.
Without the failure class, the refusal surface is flattened.
```

---

## Demo Sentence

Use this sentence when explaining the repo:

```text
This proof pack does not prove governance by showing a gate.
It proves governance by showing when protected consequence may form, when it cannot form, and whether that distinction can replay.
```

---

## Closing Demo Rule

```text
If protected effect can form under non-allow movement, the corridor is not governed.
If replay cannot reconstruct admissibility, the corridor is not proven.
If failure class is missing, refusal is flattened.
```

The corridor is accepted only when it proves both:

```text
what may bind
and
what cannot bind
```
