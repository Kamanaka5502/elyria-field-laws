# Endpoint Is Not Path Validity

## Core Claim

A valid origin and a valid destination do not prove lawful movement.

Movement is not only where it starts and where it ends.

Movement is the traversal relation between states.

---

## Failure Surface

A system may prove:

```text
origin state valid
target state valid
final outcome acceptable
commit completed
receipt produced
```

while failing to prove:

```text
trajectory validity
route standing
capacity continuity
authority continuity
lineage continuity
witness continuity
consequence-boundary control during traversal
```

That is endpoint validation without path validity.

---

## Formal Path Object

Let movement be represented as a traversal path:

```text
M(tau)
```

where `tau` indexes the material traversal of the proposed movement.

The lawful continuation region is:

```text
R = { z | A(z) >= 0, Phi(z) >= 0, U(z) = 1 }
```

Endpoint validity checks only:

```text
M(tau_0) in R
M(tau_1) in R
```

Path validity requires:

```text
M(tau) in R
```

for every material traversal condition required by the proof.

---

## Theorem

```text
M(tau_0) in R and M(tau_1) in R
```

does not imply:

```text
M(tau) in R for all material tau
```

Therefore:

```text
valid endpoint pair != valid movement path
```

---

## Why This Matters

Endpoint-only systems can approve movement that crosses an unlawful region between valid states.

That creates false confidence.

The system appears governed because the start and end states look correct.

But consequence may have formed through an inadmissible traversal.

---

## Path Failure Classes

Path validity may fail through:

```text
TRAJECTORY_ADMISSIBILITY_FAILED
CAPACITY_FAILED_MID_ROUTE
AUTHORITY_LOST_DURING_TRAVERSAL
LINEAGE_BREAK_DURING_TRAVERSAL
WITNESS_LOST_DURING_TRAVERSAL
CONSEQUENCE_BOUNDARY_UNCONTROLLED
ROUTE_STANDING_FAILED
TRANSFER_PATH_INVALID
```

These are not endpoint failures.

They are movement failures.

---

## Relation to Route Standing

Route standing is the local route expression of path validity.

A route may be open while the path lacks standing.

A route may connect two valid endpoints while still failing traversal continuity.

---

## Relation to Replay

Replay must reconstruct the path basis, not merely the endpoint pair.

Same origin and destination are not enough.

Same terminal state is not enough.

Legitimacy replay must preserve the lawful movement path or conservatively refuse reconstruction.

---

## Doctrine

Endpoint validation is a witness projection.

Path validity is consequence-resolution structure.

```text
The question is not whether the movement arrived.
The question is whether the movement lawfully traversed.
```
