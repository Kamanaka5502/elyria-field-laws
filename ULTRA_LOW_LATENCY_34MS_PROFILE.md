# Ultra Low Latency 34 ms Profile

## Purpose

This profile defines the aggressive 34 ms corridor target.

The goal is not to remove governance work.

The goal is to precompile, cache, inline, and fuse the corridor so the gate resolves from a bounded hot-path object without flattening standing, protected-effect control, receipt binding, or replay legitimacy.

---

## Core Claim

A 34 ms corridor is possible only as a hot-path corridor.

It requires:

```text
precompiled corridor schema
prevalidated envelope shape
cached standing references with TTL
current field-state hash already available
protected-effect map already local
single-pass deterministic kernel
inline effect guard
receipt hash emitted at decision time
tokenized legitimacy replay
proof-surface bitmap verdict
```

It is not achieved by removing proof fields.

It is achieved by removing avoidable recomputation.

---

## 34 ms Target Profile

```text
Aggressive target:      <= 34 ms
Preferred ceiling:      <= 50 ms
Warning threshold:      > 50 ms
Escalation threshold:   > 75 ms
Hard ceiling:           100 ms
Outer fail-safe:         200 ms
```

The 34 ms target is for the fast path only.

Anything uncertain leaves the fast path.

---

## 34 ms Stage Budget

| Stage | Budget | Optimization |
| --- | ---: | --- |
| L1 Event Intake | 1 ms | preallocated event shell |
| L2 Classification | 2 ms | corridor dispatch table |
| L3 Canonical Envelope | 3 ms | precompiled envelope schema |
| L4 Completeness Check | 1 ms | required-field bitset |
| L5 Standing Assembly | 4 ms | cached standing refs with TTL |
| L6 Field-State Binding | 3 ms | current field-state hash pointer |
| L7 Lawful Region Evaluation | 2 ms | inline scalar A/Phi/U check |
| L8 Protected Effect Mapping | 2 ms | corridor-local effect ID table |
| L9 Gate Input Construction | 1 ms | zero-copy gate input pointer |
| L10 Gate Resolution | 4 ms | deterministic branch table |
| L11 Protected Effect Guard | 2 ms | inline non-allow/effect check |
| L12 Receipt Issuance | 3 ms | preformatted receipt hash |
| L13 Legitimacy Replay | 4 ms | replay-token hash bundle |
| L14 Proof Surface Verdict | 1 ms | bitmap verdict table |
| L15 Outcome Publication | 1 ms | structured result emit |

Total:

```text
34 ms
```

---

## What Must Be Precompiled

The 34 ms path requires a corridor-local compiled profile:

```text
corridor schema
required envelope fields
standing TTL rules
failure class table
protected-effect map
law version pointer
kernel branch table
receipt template
replay hash bundle shape
proof-surface bitmap
```

If these are not precompiled, the corridor must use the 73 ms or 80 ms profile instead.

---

## Fast Path Eligibility

The 34 ms path is eligible only when:

```text
envelope shape is known
corridor_id is bound
movement type is known
standing refs are current
field-state hash is available
protected effect is mapped
law version is current
prior receipt hash matches if continuity is claimed
replay material is present
no changed-condition event is pending
no route or transfer ambiguity exists
```

Any failed condition exits the 34 ms path.

---

## Safe Exit Rules

The 34 ms path must exit to a safe path when:

```text
standing TTL expired
field hash changed
authority reference stale
evidence freshness uncertain
lineage mismatch
protected effect ambiguous
route standing uncertain
transfer continuity uncertain
capacity boundary reached
replay material incomplete
receipt chain mismatch
```

Safe exit outcomes:

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

## What Cannot Be Removed

The following are non-removable even under the 34 ms target:

```text
movement identity
corridor identity
standing basis
lawful-region state
protected-effect identity
kernel decision
non-allow failure class
receipt binding
replay token
proof-surface verdict
```

If any are removed, the corridor is not ultra-low-latency governance.

It is control-surface collapse.

---

## 34 ms Runtime Shape

The runtime should operate as a fused hot path:

```text
EventShell
  -> EnvelopeBitset
  -> StandingTTLCheck
  -> FieldHashBind
  -> InlineRegionCheck
  -> KernelBranch
  -> EffectGuard
  -> ReceiptHash
  -> ReplayToken
  -> ProofBitmap
  -> Outcome
```

This is not fifteen separate services.

It is one fused corridor execution surface with stage timing preserved inside the receipt.

---

## Latency Receipt for 34 ms Path

The latency receipt must preserve:

```text
latency_receipt_id
event_id
envelope_id
movement_id
corridor_id
profile = 34ms_hot_path
stage_latency_ms
total_latency_ms
standing_ttl_ms
standing_age_ms
field_hash_before
field_hash_after
fast_path_eligible
safe_exit_reason
kernel_decision
proof_surface_verdict
```

Even when stages are fused, the receipt must preserve stage timings or stage timing estimates.

---

## Outcome Matrix

### Clean 34 ms Allow

```text
<= 34 ms
LATENCY_OK
ALLOW
EFFECT_ALLOWED
LEGITIMACY_REPLAY_VALID
PROOF_SURFACE_VALID
```

### Clean 34 ms Refuse

```text
<= 34 ms
LATENCY_OK
REFUSE
EFFECT_PREVENTED
LEGITIMACY_REPLAY_VALID
PROOF_SURFACE_VALID
```

### Fast Path Exit

```text
34 ms path not eligible
SAFE_PATH_REQUIRED
```

### Uncertain Standing

```text
REENTRY_REQUIRED
```

### Over 50 ms

```text
LATENCY_WARN
```

### Over 75 ms

```text
ESCALATE_LATENCY
```

### Over 100 ms

```text
LATENCY_REENTRY_REQUIRED or LATENCY_REFUSE
```

---

## Doctrine

The 34 ms target is achievable only by making the corridor smaller, hotter, and more deterministic.

Not by weakening proof.

```text
34 ms is a compiled corridor target.
It is not a general-purpose pipeline target.
```

The governing posture remains:

```text
Fast when complete.
Closed when uncertain.
Replayable always.
```