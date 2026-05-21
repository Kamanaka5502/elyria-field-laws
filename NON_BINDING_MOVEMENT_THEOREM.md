# Non-Binding Movement Theorem

## Core Claim

A system proves movement governance only when a proposed transition that fails the kernel cannot acquire consequence status.

The proof question is not whether a system can stop, flag, reverse, or explain an operation.

The proof question is:

```text
Can a failed movement still become consequence?
```

If yes, the system is documenting execution rather than governing movement.

---

## Definitions

Let `M` be a proposed movement across a consequence-state field.

A movement is not a workflow step. It is a proposed transition from one consequence-state to another.

```text
M_t = (S_o, S_t, A_t, E_t, L_t, R_t, C_t, W_t)
```

Where:

```text
S_o = origin state
S_t = target state
A_t = authority standing
E_t = evidence context
L_t = lineage condition
R_t = recovery posture
C_t = consequence exposure
W_t = witness / replay object
```

Let `K(M)` be the movement-kernel resolution:

```text
K(M) in {ALLOW, REDIRECT, ESCALATE, REFUSE, HALT}
```

Let `BIND(M)` mean the movement is permitted to acquire protected consequence status.

---

## Theorem

```text
BIND(M) is defined only when K(M) = ALLOW.
```

Equivalent form:

```text
K(M) != ALLOW => BIND(M) is undefined.
```

Therefore, if the kernel resolves to `REDIRECT`, `ESCALATE`, `REFUSE`, or `HALT`, the proposed movement remains non-binding.

---

## Consequence

A failed movement is not treated as an already-real event that must be corrected after the fact.

A failed movement remains outside consequence status by construction.

That is the distinction between ordinary control and consequence-bound movement governance.

Ordinary controls may observe, interrupt, flag, log, or reverse execution.

A movement kernel resolves consequence status before protected effect is permitted.

---

## Hard Gate Failure

If a hard gate fails, the movement cannot reach `ALLOW`.

Hard gates include:

```text
authority standing
lineage integrity
evidence freshness
consequence admissibility
witness / replay validity
```

These gates are non-compensable.

Operational continuity cannot compensate for lost authority.

Policy compliance cannot replace lineage.

Replay cannot replace legitimacy.

---

## Resolution Table

```text
ALLOW    -> consequence status may be defined
REDIRECT -> non-binding pending lawful correction
ESCALATE -> non-binding pending external resolution
REFUSE   -> non-binding due to failed admissibility
HALT     -> non-binding because continued movement expands illegitimate consequence
```

Only `ALLOW` permits consequence status.

All other kernel outcomes preserve non-binding status.

---

## Proof Surface

To prove movement governance, the runtime must show:

1. proposed movement object;
2. kernel resolution;
3. hard gate state;
4. admissibility basis;
5. consequence boundary;
6. witness / replay object;
7. proof that protected effect was permitted only when `K(M) = ALLOW`.

Without this proof surface, the system may be useful, but it is not proving consequence-bound movement governance.

---

## Doctrine

The theorem is not that failed action is stopped.

The theorem is that failed movement never acquires lawful consequence status.

```text
Failed movement is non-binding by construction.
```
