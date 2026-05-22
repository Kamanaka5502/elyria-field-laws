# Route Standing Theorem

## Core Claim

A route is not lawful because it exists.

A route is lawful only when movement can traverse it without losing admissibility, capacity, authority-validity, lineage continuity, witness continuity, and consequence-boundary control.

A path may be available while lacking standing.

---

## Why This Matters

Many systems treat available paths as valid paths.

That is a reduction.

A route can be mechanically open while legally, thermally, operationally, or geometrically inadmissible.

The proof question is not:

```text
Can the movement be routed?
```

The proof question is:

```text
Does the route preserve lawful continuation across traversal?
```

---

## Formal Context

A movement path may be modeled as:

```text
M(tau)
```

where `tau` indexes traversal through the route.

For the route to hold standing, each material sampled point must preserve the lawful-region condition:

```text
R = { z | A(z) >= 0, Phi(z) >= 0, U(z) = 1 }
```

Route standing requires:

```text
M(tau) in R
```

for every material traversal point required by the route proof.

---

## Theorem

A route has standing only if:

1. the route is identified;
2. the source state is identified;
3. the destination state is identified;
4. each material traversal condition remains admissible;
5. capacity remains non-negative through the route;
6. authority-validity survives traversal;
7. lineage continuity is preserved;
8. witness continuity is preserved;
9. consequence status remains controlled until admission;
10. replay can reconstruct the route basis.

If these conditions fail, the route is not lawful movement.

It is only available motion.

---

## Route Failure Classes

Route standing may fail through:

```text
ROUTE_UNIDENTIFIED
SOURCE_STATE_MISSING
DESTINATION_STATE_MISSING
TRAVERSAL_ADMISSIBILITY_FAILED
CAPACITY_FAILED_ON_ROUTE
AUTHORITY_LOST_ON_ROUTE
LINEAGE_BREAK_ON_ROUTE
WITNESS_LOST_ON_ROUTE
CONSEQUENCE_BOUNDARY_UNCONTROLLED
ROUTE_REPLAY_INCOMPLETE
```

These failure classes distinguish path availability from lawful traversal.

---

## Relation to Endpoint Validity

Valid origin and valid destination do not prove lawful route.

A movement can start inside `R` and end inside `R` while violating route standing between them.

```text
valid source + valid destination != valid traversal
```

Endpoint proof is insufficient when consequence forms through movement.

---

## Relation to Transfer Continuity

Transfer requires a lawful route between sending basin and receiving basin.

A receiving basin may have capacity, but the transfer still fails if the route cannot preserve standing.

Transfer continuity therefore requires both:

```text
receiving basin standing
route standing
```

---

## Relation to Partial Binding

If only part of the route can preserve capacity or standing, the system may resolve a bounded partial route only if the partial path is explicitly bounded and receipted.

Unbounded partial routing is projection error.

---

## Doctrine

Route existence is not route standing.

```text
A path may be open and still unlawful.
A route may be available and still unable to carry consequence.
```

Lawful route means traversal preserves the field.
