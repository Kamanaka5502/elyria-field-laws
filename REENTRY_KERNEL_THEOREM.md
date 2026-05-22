# Reentry Kernel Theorem

## Core Claim

Reentry is not restart.

Reentry is the required return of proposed movement into the resolving kernel after a material field change, standing decay, breach, transfer shift, route change, or capacity boundary event.

A movement may continue only if the post-reentry kernel resolves current standing.

---

## Why This Matters

Conventional systems often treat restart as operational recovery.

That is incomplete.

A restart may resume process state without proving lawful continuation.

Reentry is stricter.

It requires the movement to be evaluated again under the current field.

```text
restart != reentry
recovery != standing
resumption != lawful continuation
```

---

## Formal Context

The lawful region of continuation is:

```text
R = { z | A(z) >= 0, Phi(z) >= 0, U(z) = 1 }
```

A material field event creates a new evaluation state:

```text
z_t0 -> z_t1
```

Prior kernel resolution cannot be blindly inherited:

```text
K(M, t0) = ALLOW
```

does not imply:

```text
K(M, t1) = ALLOW
```

---

## Theorem

If a material field event occurs before consequence status is admitted, then movement must re-enter the kernel.

```text
field_event(M, t1) = true
```

requires:

```text
REENTER(M, t1) -> K(M, t1)
```

Only `K(M, t1)` may determine whether movement may continue toward consequence status.

---

## Reentry Triggers

Reentry is required when any of the following occur:

```text
STANDING_DECAY
CHANGED_CONDITION
TRAJECTORY_BREACH
CAPACITY_BOUNDARY
BOUNDARY_PRESSURE_SHIFT
TRANSFER_PATH_CHANGE
ROUTE_STANDING_CHANGE
WITNESS_CONTINUITY_CHANGE
LAW_VERSION_CHANGE
BASIN_CAPACITY_CHANGE
CONSEQUENCE_EXPOSURE_CHANGE
```

These are not passive metadata changes.

They are resolving-field events.

---

## Reentry Requirements

A valid reentry must reconstruct:

1. original movement object;
2. triggering field event;
3. current admissibility state;
4. current capacity state;
5. current authority-validity;
6. lineage continuity;
7. evidence state;
8. route and transfer standing;
9. witness continuity;
10. current law version;
11. post-reentry kernel decision;
12. protected effect status.

Without these, the system has resumed motion without proving standing.

---

## Reentry Outcomes

Post-reentry kernel resolution may return:

```text
ALLOW
PARTIAL
TRANSFER
REDIRECT
ESCALATE
REFUSE
HALT
RESTART
```

Only an admissible post-reentry outcome may permit continuation.

---

## Relation to Breach

Breach requires halt and judgement before restart.

Reentry is the kernel-level evaluation that determines whether restart may lawfully occur.

```text
Breach -> Halt -> Judgement -> Reentry -> K(M, t1) -> Restart only if lawful
```

Restart without reentry inherits violation.

---

## Relation to Replay

Legitimacy replay must preserve the reentry event and post-reentry kernel decision.

A replay that reconstructs only the pre-change approval or final state is execution replay only.

---

## Doctrine

Reentry is how the field prevents stale standing from becoming consequence.

```text
When standing is interrupted, movement must earn continuity again.
```
