# Continuity Earning Theorem

## Core Claim

Continuity is not inherited.

Continuity is earned by surviving current field conditions after every material interruption, transfer, breach, route change, capacity boundary, or standing decay event.

A movement does not continue lawfully because it was already in motion.

It continues lawfully only if it can re-establish standing under the present resolving field.

---

## Why This Matters

Many systems treat continuity as persistence.

That is a reduction.

Persistence means motion keeps going.

Continuity means the lawful relation survives.

```text
persistence != continuity
activity != standing
resumption != lawful continuation
```

---

## Formal Context

The lawful region of continuation is:

```text
R = { z | A(z) >= 0, Phi(z) >= 0, U(z) = 1 }
```

A movement may be active at `t0` and still lose lawful continuity at `t1`.

```text
active(M, t1) does not imply continuous(M, t1)
```

Continuity must be reconstructed through the kernel:

```text
CONTINUE(M, t1) is admissible only if K(M, t1) permits continuation.
```

---

## Theorem

If movement `M` crosses any material field event, then continuity must be re-earned.

```text
field_event(M, t1) = true
```

requires:

```text
reconstruct_continuity(M, t1)
```

and:

```text
K(M, t1) in {ALLOW, ALLOW_PARTIAL, TRANSFER, REDIRECT}
```

for movement to lawfully continue.

If the post-event kernel returns:

```text
REFUSE
HALT
ESCALATE without resolution
```

then continuity is not earned.

---

## Continuity Requirements

Continuity requires current preservation of:

```text
movement identity
authority standing
evidence freshness
lineage integrity
capacity support
route standing
transfer standing
witness continuity
law version alignment
consequence-boundary control
```

Any missing dimension breaks continuity unless the kernel resolves a lawful repair path.

---

## Continuity Failure Classes

Continuity may fail through:

```text
AUTHORITY_CONTINUITY_LOST
EVIDENCE_CONTINUITY_LOST
LINEAGE_CONTINUITY_LOST
CAPACITY_CONTINUITY_LOST
ROUTE_CONTINUITY_LOST
TRANSFER_CONTINUITY_LOST
WITNESS_CONTINUITY_LOST
LAW_VERSION_CONTINUITY_LOST
CONSEQUENCE_BOUNDARY_LOST
```

These are not metadata gaps.

They are lawful-continuation failures.

---

## Relation to Reentry

Reentry is the procedure.

Continuity earning is the proof result.

```text
Reentry asks the kernel again.
Continuity is earned only if the kernel preserves lawful continuation.
```

---

## Relation to Replay

Legitimacy replay must reconstruct continuity earning.

A replay that shows continuous activity but cannot reconstruct post-event standing is execution replay only.

Replay must show:

```text
field event
reentry
post-event standing
kernel decision
continuity result
protected effect status
```

---

## Doctrine

Continuity is not motion that never stopped.

Continuity is lawful relation that survived the field.

```text
Movement does not inherit continuity.
Movement earns continuity under current law.
```
