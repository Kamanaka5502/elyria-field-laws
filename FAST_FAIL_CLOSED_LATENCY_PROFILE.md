# Fast Fail-Closed Latency Profile

## Purpose

This profile tightens the event-intake-to-gate pipeline for low latency while preserving consequence-bound governance.

The goal is fast admissibility resolution that fails closed under uncertainty.

---

## Core Rule

```text
fast + uncertain = not admissible
fast + replayable + fail-closed = admissible
```

No corridor may choose speed over current standing.

---

## Target Profile

For the optimized proof corridor:

```text
Aggressive target:      <= 75 ms
Preferred ceiling:      <= 100 ms
Warning threshold:      > 100 ms
Escalation threshold:   > 150 ms
Hard ceiling:           200 ms
Reentry trigger:        field changed or freshness cannot be proven
Refusal trigger:        latency destroys standing or replayability
```

The 200 ms ceiling remains the outer fail-safe boundary.

The product-grade target is sub-100 ms.

---

## Optimized Stage Budget

| Stage | Budget | Strategy |
| --- | ---: | --- |
| L1 Event Intake | 2 ms | preallocated event shell |
| L2 Classification | 4 ms | deterministic classifier table |
| L3 Canonical Envelope | 6 ms | schema-normalized envelope builder |
| L4 Completeness Check | 3 ms | required-field bitmap |
| L5 Standing Assembly | 10 ms | cached refs with TTL guard |
| L6 Field-State Binding | 8 ms | current-state hash lookup |
| L7 Lawful Region Evaluation | 5 ms | scalar A/Phi/U evaluation |
| L8 Protected Effect Mapping | 4 ms | corridor-local effect map |
| L9 Gate Input Construction | 2 ms | envelope plus field pointer |
| L10 Gate Resolution | 8 ms | deterministic kernel branch |
| L11 Protected Effect Guard | 4 ms | effect status guard table |
| L12 Receipt Issuance | 6 ms | preformatted receipt plus hash chain |
| L13 Legitimacy Replay | 10 ms | replay-token construction |
| L14 Proof Surface Verdict | 5 ms | proof bitmap plus verdict table |
| L15 Outcome Publication | 3 ms | structured result emit |

Optimized total:

```text
80 ms
```

This fits under the preferred 100 ms ceiling with a 20 ms margin.

---

## Aggressive Sub-75 Profile

To reach sub-75 ms:

```text
Standing Assembly:       10 ms -> 8 ms
Field-State Binding:      8 ms -> 6 ms
Legitimacy Replay:       10 ms -> 8 ms
Proof Surface Verdict:    5 ms -> 4 ms
```

Aggressive total:

```text
73 ms
```

This is acceptable only if replay material is already present and all required legitimacy hashes are available.

Do not reach 73 ms by removing proof fields.

---

## Non-Removable Fields

The following may not be removed for speed:

```text
movement identity
corridor identity
current standing basis
lawful-region state
protected-effect map
kernel decision
failure class for non-allow
receipt binding
legitimacy replay token
proof-surface verdict
```

Removing any of these turns the system into a control surface.

---

## Fast Path / Safe Path

```text
FAST PATH
  deterministic envelope complete
  standing refs current
  protected effect mapped
  field state hash available
  replay material available
  no changed-condition event

SAFE PATH
  missing field
  stale field
  changed condition
  replay uncertainty
  ambiguous effect
  capacity boundary
  route or transfer uncertainty
```

Fast path may resolve quickly.

Safe path must route to reentry, escalation, refusal, or halt.

---

## Outcome Rules

### Clean Fast Allow

```text
<= 75 ms
LATENCY_OK
ALLOW
EFFECT_ALLOWED
LEGITIMACY_REPLAY_VALID
PROOF_SURFACE_VALID
```

### Clean Fast Refuse

```text
<= 75 ms
LATENCY_OK
REFUSE
EFFECT_PREVENTED
LEGITIMACY_REPLAY_VALID
PROOF_SURFACE_VALID
```

### Warning But Current

```text
75-100 ms
LATENCY_WARN
continue only if standing remains current
```

### Slow Corridor

```text
100-150 ms
LATENCY_WARN or ESCALATE_LATENCY
```

### Over Escalation Threshold

```text
> 150 ms
ESCALATE_LATENCY
```

### Over Hard Ceiling

```text
> 200 ms
LATENCY_REENTRY_REQUIRED or LATENCY_REFUSE
```

---

## Guard Rules

```text
uncertain_current_standing -> ESCALATE or REFUSE
```

Never:

```text
uncertain_current_standing -> ALLOW
```

Standing references must have TTLs.

Expired standing triggers reentry.

Replay token must be generated at decision time.

Outcome publication waits for protected-effect guard.

---

## Fast Latency Receipt

A fast latency receipt must preserve:

```text
latency_receipt_id
event_id
envelope_id
movement_id
corridor_id
stage_latency_ms
total_latency_ms
corridor_ceiling_ms
standing_ttl_ms
standing_age_ms
field_changed_during_evaluation
fast_path_used
safe_path_reason
latency_verdict
kernel_decision
proof_surface_verdict
```

---

## Final Doctrine

The fastest safe system is not the one that acts first.

The fastest safe system is the one that reaches a bounded, replayable, fail-closed decision before protected consequence can form.

```text
Low latency is not enough.
Low latency must preserve standing.
Fail-closed is the hard posture.
```