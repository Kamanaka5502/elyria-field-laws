# Changed-Condition Reentry Theorem

## Core Claim

A changed condition forces reentry.

A movement that was previously admissible cannot continue to consequence status after a material condition changes unless it re-enters the resolving field and survives the current law, capacity, authority, lineage, witness, and trajectory conditions.

---

## Why This Matters

Many systems treat changed conditions as metadata.

That is a reduction.

A changed condition is not a note attached to movement.

It is a field event that can alter standing.

The proof question is not:

```text
Was the movement approved before the change?
```

The proof question is:

```text
Did the movement re-enter the resolving field after the change and still hold?
```

---

## Formal Context

The lawful region of continuation is:

```text
R = { z | A(z) >= 0, Phi(z) >= 0, U(z) = 1 }
```

A material condition change creates a new evaluation state:

```text
z_t0 -> z_t1
```

Prior standing at `t0` does not automatically transfer to `t1`.

```text
z_t0 in R does not imply z_t1 in R
```

---

## Theorem

If a material condition changes before consequence status is admitted, the movement must re-enter the resolving field.

```text
changed_condition(M, t1) = true
```

requires:

```text
reentry(M, t1) -> K(M, t1)
```

Only the post-change kernel decision may determine whether consequence status can be admitted.

---

## Material Change Classes

Changed-condition reentry is required when any of the following changes:

```text
AUTHORITY_CHANGED
EVIDENCE_STALE
SCOPE_NARROWED
LINEAGE_CHANGED
CAPACITY_CHANGED
TRANSFER_PATH_CHANGED
ROUTE_STANDING_CHANGED
WITNESS_CHANGED
LAW_VERSION_CHANGED
CONSEQUENCE_EXPOSURE_CHANGED
BASIN_PRESSURE_CHANGED
```

These are not advisory events.

They alter the resolving field.

---

## Reentry Requirements

A valid reentry must preserve or reconstruct:

1. the prior movement object;
2. the changed condition;
3. the current authority standing;
4. the current evidence state;
5. the current lineage state;
6. the current capacity field;
7. route and transfer standing;
8. witness continuity;
9. law version;
10. post-change kernel decision.

Without these, continuation after change is inherited assumption, not lawful reentry.

---

## Relation to Standing Decay

Standing decay identifies that prior standing may fail.

Changed-condition reentry defines the required response:

```text
re-enter the resolving field
re-evaluate current standing
admit consequence only under current lawful decision
```

---

## Relation to Replay

Legitimacy replay must preserve the changed-condition event and the reentry decision.

A replay that reconstructs only the original approval but not the post-change reentry is execution replay only.

---

## Doctrine

Changed conditions are not annotations.

Changed conditions are reentry triggers.

```text
When the field changes, standing must be earned again.
```
