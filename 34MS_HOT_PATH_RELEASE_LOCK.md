# 34 ms Hot Path Release Lock

## Status

The 34 ms hot path is now defined as a compiled corridor contract.

It is not a general-purpose pipeline claim.

It is a bounded hot-path profile for one corridor where the required proof objects are local, current, hash-ready, and replay-ready before the event reaches the gate.

---

## Locked Target

```text
Target total:        34 ms
Preferred ceiling:   50 ms
Escalation:          > 75 ms
Hard ceiling:        100 ms
Outer failsafe:      200 ms
```

---

## Locked Stage Budget

```text
L1  Event Intake                 1 ms
L2  Classification               2 ms
L3  Canonical Envelope            3 ms
L4  Completeness Check            1 ms
L5  Standing Assembly             4 ms
L6  Field-State Binding           3 ms
L7  Lawful Region Evaluation      2 ms
L8  Protected Effect Mapping      2 ms
L9  Gate Input Construction       1 ms
L10 Gate Resolution               4 ms
L11 Protected Effect Guard        2 ms
L12 Receipt Issuance              3 ms
L13 Legitimacy Replay             4 ms
L14 Proof Surface Verdict         1 ms
L15 Outcome Publication           1 ms
--------------------------------------
Total                            34 ms
```

This budget is encoded in:

```text
runtime/hot_path_34ms.py
```

and tested in:

```text
tests/test_hot_path_34ms.py
```

---

## Locked Runtime Contract

The runtime contract is:

```text
fast when complete
safe-path when uncertain
replayable always
```

The hot path may resolve only when all required proof material is present and current.

---

## Hot Path Eligibility

The 34 ms path is eligible only if:

```text
envelope shape is known
movement type is known
standing references are current
standing TTL has not expired
field-state hash is available
field hash has not changed
protected effect is mapped
law version is current
replay material is present
prior receipt hash matches if continuity is claimed
no changed-condition event is pending
no route or transfer ambiguity exists
no unresolved capacity boundary exists
```

Any failed condition exits to a safe path.

---

## Safe Path Outcomes

Safe path outcomes are:

```text
REENTRY_REQUIRED
ESCALATE
REFUSE
HALT
```

Never:

```text
uncertain -> ALLOW
```

---

## Proof Non-Removal Rule

The following cannot be removed to make the path faster:

```text
movement identity
corridor identity
current standing basis
lawful-region state
protected-effect identity
kernel decision
non-allow failure class
receipt binding
replay token
proof-surface verdict
```

Removing any of these collapses the system into a control surface.

---

## Performance Harness

Local performance sampling is implemented in:

```text
runtime/perf_34ms_harness.py
```

Run:

```bash
python -m runtime.perf_34ms_harness
```

The harness reports:

```text
iterations
target_total_ms
budget_total_ms
min_ms
mean_ms
median_ms
max_ms
p95_ms
pass_target
verdict_counts
```

The harness measures local execution time.

The release lock defines the corridor contract.

Both must be preserved.

---

## Acceptance Conditions

The 34 ms profile is accepted only when:

```text
budget_total_ms == 34
complete hot-path input resolves without safe-path exit
non-allow movement with effect prevented remains proof-surface valid
non-allow movement with effect formed collapses to CONTROL_SURFACE_ONLY
expired standing TTL exits to safe path
field hash change exits to safe path
missing replay material exits to safe path
latency above thresholds escalates, reenters, or refuses
```

---

## Final Lock Statement

The 34 ms path is not fast because it skips governance.

It is fast because the corridor is compiled, bounded, local, deterministic, and fail-closed.

```text
34 ms is the hot-path contract.
Fail-closed is the hard posture.
Replayability is non-negotiable.
```