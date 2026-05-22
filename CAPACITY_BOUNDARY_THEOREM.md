# Capacity Boundary Theorem

## Core Claim

A state can remain inside the lawful region while still being unable to admit additional burden.

This is the capacity boundary condition.

It is not refusal.

It is not full allowance.

It is lawful continuation at the edge of remaining capacity.

---

## Formal Spine

The lawful region of continuation is:

```text
R = { z | A(z) >= 0, Phi(z) >= 0, U(z) = 1 }
```

Remaining lawful capacity is:

```text
Phi(x) = C(x) - M(x)
```

The capacity boundary occurs when:

```text
Phi(x) = 0
```

At this boundary, the state may still satisfy lawful continuation:

```text
A(z) >= 0
Phi(z) = 0
U(z) = 1
```

But no additional burden may bind without new capacity, transfer, delay, route, or partial admission.

---

## Theorem

If:

```text
A(z) >= 0
Phi(z) = 0
U(z) = 1
```

then:

```text
z is inside R at capacity boundary
```

but:

```text
BIND(M + additional_burden) is undefined
```

unless a lawful transfer, capacity increase, partial split, or redirect is resolved first.

---

## Why This Matters

Binary systems collapse the boundary into either allow or refuse.

That is wrong.

The capacity boundary is a third geometric condition:

```text
lawful continuation exists
additional burden does not
```

This is not ordinary permission logic.

It is continuation geometry.

---

## Relation to Partial Binding

Partial binding becomes necessary when proposed burden exceeds remaining capacity but a bounded fraction can still be admitted.

If:

```text
q_total > Phi(x)
```

and:

```text
Phi(x) > 0
```

then the field may resolve:

```text
PARTIAL_BIND(M, q_allowed)
```

where:

```text
q_allowed <= Phi(x)
q_refused = q_total - q_allowed
```

If:

```text
Phi(x) = 0
```

then no positive additional quantity can be partially admitted without transfer or new capacity.

---

## Relation to Basin Holding

A basin at capacity boundary still exists as a lawful holding region.

But it cannot receive more pressure.

A basin does not fail merely because it is full.

It fails when additional movement is forced into it without lawful transfer, refusal, route, or partial split.

---

## Runtime Verdict

The executable lawful-region model names this condition:

```text
PARTIAL_CAPACITY
```

Meaning:

```text
inside lawful continuation,
but at the capacity boundary.
```

---

## Doctrine

Capacity boundary is where continuation remains lawful but expansion loses standing.

```text
The field may hold what it already carries.
It may not admit what it has no capacity to carry.
```
