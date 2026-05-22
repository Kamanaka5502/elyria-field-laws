# Partial Binding Theorem

## Core Claim

Partial binding is not compromise.

Partial binding is capacity-bounded consequence admission.

A movement may partially bind only when the admitted fraction is explicitly bounded, capacity-supported, receipted, and separated from the refused fraction.

---

## Why This Matters

Binary allow/refuse logic is insufficient for fields where consequence can be fractionally admitted.

Thermal movement exposes this clearly.

A device may propose a heat consequence larger than the field can carry.

The correct outcome may not be full `ALLOW` or total `REFUSE`.

The correct outcome may be:

```text
PARTIAL
```

But `PARTIAL` is lawful only if the admitted portion is bounded by the field's remaining capacity.

---

## Formal Object

Let `M` be a proposed movement.

Let `q_total` be the proposed consequence quantity.

Let `q_allowed` be the admissible fraction.

Let `q_refused` be the non-admissible remainder.

```text
q_total = q_allowed + q_refused
```

Partial binding may be defined only when:

```text
0 < q_allowed < q_total
```

and:

```text
q_allowed <= Phi(x)
```

Where:

```text
Phi(x) = C(x) - M(x)
```

`Phi(x)` is remaining lawful capacity.

---

## Theorem

```text
PARTIAL_BIND(M, q_allowed)
```

is defined only if:

1. the full movement cannot lawfully bind;
2. a bounded fraction can lawfully bind;
3. `q_allowed` is explicitly measured or conservatively bounded;
4. `q_allowed <= Phi(x)`;
5. `q_refused = q_total - q_allowed` is explicitly refused;
6. the receipt preserves proposed, allowed, and refused quantities;
7. replay can reconstruct the same capacity relation.

If any of these conditions fail, `PARTIAL_BIND` is undefined.

---

## Non-Laundering Rule

Partial binding cannot be used to smuggle full execution through a reduced label.

A partial outcome is unlawful when:

```text
q_allowed is not bounded
q_refused is not identified
capacity relation is not preserved
receipt omits the refused fraction
replay cannot reconstruct the split
```

Unbounded partial execution is projection error.

---

## Relation to Non-Binding Movement

The original field-law rule remains:

```text
BIND(M) is defined only when K(M) = ALLOW.
```

Partial binding is not an exception to this rule.

It is a bounded variant:

```text
PARTIAL_BIND(M, q_allowed) is defined only when K_partial(M, q_allowed) = ALLOW_PARTIAL.
```

The refused portion remains non-binding.

```text
BIND(M, q_refused) is undefined.
```

---

## Thermal Example

A device proposes:

```text
q_total = 100 heat-units
```

The field has:

```text
Phi(x) = 40 heat-units
```

If authority, lineage, witness, trajectory, and sink assignment hold, the system may admit:

```text
q_allowed = 40
q_refused = 60
```

The decision is not full `ALLOW`.

It is `PARTIAL`.

Only `40` heat-units may acquire consequence status.

The remaining `60` heat-units must remain refused, routed elsewhere, delayed, or halted.

---

## Receipt Requirements

A partial-binding receipt must preserve:

```text
movement_id
q_total
q_allowed
q_refused
capacity_before
capacity_after
basin / sink identity
authority standing
lineage state
evidence state
witness / replay object
decision
rule trace
```

Without these fields, partial binding collapses into ordinary throttling or projection error.

---

## Doctrine

Partial is not weakness.

Partial is lawful fractioning under capacity constraint.

```text
The field may admit only what it can carry.
Everything else remains non-binding.
```
