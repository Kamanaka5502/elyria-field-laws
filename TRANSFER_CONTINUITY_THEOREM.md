# Transfer Continuity Theorem

## Core Claim

Transfer is not deletion.

Transfer is lawful continuation through a receiving basin, route, or successor state that can carry the movement without losing standing, lineage, capacity, or witness continuity.

A movement does not become lawful merely because it exits one surface.

It must enter another lawful holding relation.

---

## Why This Matters

Many systems treat removal from a local surface as resolution.

That is projection error.

A dashboard may show that pressure left one region.

A log may show that an item was moved.

A workflow may show that responsibility transferred.

None of those prove lawful transfer.

The proof question is stricter:

```text
Did the movement preserve lawful continuation across the transfer boundary?
```

---

## Formal Context

A basin holds while the lawful region remains satisfied:

```text
R = { z | A(z) >= 0, Phi(z) >= 0, U(z) = 1 }
```

A transfer from basin `B_1` to basin `B_2` is lawful only if the receiving basin can carry the transferred movement.

```text
Transfer(B_1 -> B_2, M)
```

is valid only when `B_2` preserves:

```text
admissibility
remaining capacity
authority-validity
lineage continuity
witness continuity
consequence boundary
```

---

## Theorem

A transfer is lawful only if:

1. the sending basin is identified;
2. the receiving basin is identified;
3. the transfer path is valid;
4. the receiving basin has sufficient remaining capacity or a bounded partial capacity relation;
5. authority-validity survives the transfer;
6. lineage is not broken;
7. the witness object preserves the transfer relation;
8. the receipt records origin, destination, quantity, capacity, and decision basis.

If these conditions fail, the transfer does not prove continuation.

It proves only displacement from a local surface.

---

## Transfer Failure Classes

Transfer may fail through:

```text
NO_RECEIVING_BASIN
TRANSFER_PATH_INVALID
RECEIVER_CAPACITY_FAILED
AUTHORITY_LOST_ON_TRANSFER
LINEAGE_BREAK_ON_TRANSFER
WITNESS_TRANSFER_INCOMPLETE
CONSEQUENCE_BOUNDARY_UNRESOLVED
```

These are not cosmetic labels.

They are boundary outcomes explaining why transfer could not establish lawful continuation.

---

## Relation to Drain

A drain is a transfer aperture.

It is not deletion.

If content exits a basin through a drain, the proof surface must show where it lawfully went.

Untracked drainage is projection error.

It sees disappearance from one local surface while losing the resolving relation.

---

## Relation to Partial Binding

A transfer may be full or partial.

If the receiving basin can carry only a bounded fraction, the system may resolve:

```text
TRANSFER_PARTIAL(M, q_allowed)
```

where:

```text
q_allowed <= Phi(B_2)
q_refused = q_total - q_allowed
```

The remainder must stay non-binding, reroute, wait, or refuse.

---

## Relation to Replay

Transfer replay must reconstruct more than terminal location.

It must reconstruct:

```text
source basin
destination basin
transfer path
capacity before transfer
capacity after transfer
authority standing
lineage continuity
witness continuity
kernel decision
```

Same destination is not enough.

Same final state is not enough.

The lawful transfer relation must replay.

---

## Doctrine

Transfer is lawful only when continuation survives the movement between basins.

```text
Leaving one basin is not proof.
Entering a lawful receiving relation is proof.
```
