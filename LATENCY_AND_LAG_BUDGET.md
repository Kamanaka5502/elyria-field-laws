# Latency and Lag Budget

## Purpose

This document defines where lag can enter the event-intake-to-gate pipeline, what each delay means, which delays are acceptable, which delays force escalation, and what receipts must preserve.

Lag is not just performance delay.

Lag can become standing risk.

If the field changes while the pipeline is evaluating, prior standing may no longer be current.

---

## Core Rule

```text
Latency is admissible only while standing remains current.
```

If latency exceeds the corridor ceiling or field conditions change during evaluation, the movement must re-enter the resolving field.

```text
lag_exceeded or field_changed -> REENTRY_REQUIRED
```

---

## Pipeline Lag Map

```text
Raw Event
  -> Event Intake                 L1 intake lag
  -> Event Classification          L2 classification lag
  -> Canonical Envelope            L3 canonicalization lag
  -> Envelope Completeness Check   L4 envelope validation lag
  -> Standing Assembly             L5 standing reconstruction lag
  -> Field-State Binding           L6 live field binding lag
  -> Lawful Region Evaluation      L7 geometry evaluation lag
  -> Protected Effect Mapping      L8 effect-map lag
  -> Gate Input Construction       L9 gate-input lag
  -> Gate Resolution               L10 kernel lag
  -> Protected Effect Guard        L11 effect-guard lag
  -> Receipt Issuance              L12 receipt lag
  -> Legitimacy Replay             L13 replay lag
  -> Proof Surface Verdict         L14 proof-surface lag
  -> Final Outcome                 L15 outcome publication lag
```

Each lag segment must be measurable and receipted.

---

## Recommended Bounded Corridor Budget

For the first proof corridor, use a strict demonstration ceiling:

```text
Total corridor ceiling: 200 ms
Target corridor runtime: <= 100 ms
Escalation threshold: > 200 ms
Hard stale threshold: corridor-specific
```

The 200 ms ceiling is not universal law.

It is a bounded proof-corridor default.

A corridor may set a different ceiling, but the ceiling must be explicit before movement reaches the gate.

---

## Suggested Stage Budget

| Stage | Budget | Risk if exceeded |
| --- | ---: | --- |
| L1 Event Intake | 5 ms | event capture uncertainty |
| L2 Classification | 10 ms | wrong downstream checks |
| L3 Canonical Envelope | 15 ms | envelope drift / malformed handoff |
| L4 Completeness Check | 10 ms | gate receives incomplete object |
| L5 Standing Assembly | 30 ms | stale authority/evidence/lineage |
| L6 Field-State Binding | 20 ms | live state mismatch |
| L7 Lawful Region Evaluation | 15 ms | capacity/admissibility lag |
| L8 Protected Effect Mapping | 10 ms | prevention proof failure |
| L9 Gate Input Construction | 5 ms | gate input mismatch |
| L10 Gate Resolution | 25 ms | delayed bind decision |
| L11 Protected Effect Guard | 10 ms | effect status uncertainty |
| L12 Receipt Issuance | 15 ms | receipt delay / chain risk |
| L13 Legitimacy Replay | 25 ms | replay uncertainty |
| L14 Proof Surface Verdict | 10 ms | final proof delay |
| L15 Outcome Publication | 5 ms | operator visibility delay |

Default total:

```text
205 ms nominal max
```

For a strict 200 ms corridor, compress L13 or L5 by corridor design.

---

## Lag Classes

### 1. Processing Lag

Normal computation delay inside a stage.

Outcome:

```text
CONTINUE if below budget
ESCALATE if over corridor ceiling
```

### 2. Standing Lag

Delay that risks authority, evidence, lineage, capacity, or witness freshness.

Outcome:

```text
REENTRY_REQUIRED
```

### 3. Envelope Lag

Delay between raw event intake and canonical envelope readiness.

Outcome:

```text
ENVELOPE_STALE
ENVELOPE_RECHECK_REQUIRED
```

### 4. Field-State Lag

Delay between envelope creation and live field-state binding.

Outcome:

```text
FIELD_REBIND_REQUIRED
```

### 5. Gate Lag

Delay inside kernel decisioning.

Outcome:

```text
ESCALATE_LATENCY
```

if the corridor ceiling is exceeded.

### 6. Receipt Lag

Delay issuing a receipt after decision.

Outcome:

```text
RECEIPT_DELAYED
RECEIPT_CHAIN_RISK
```

### 7. Replay Lag

Delay reconstructing legitimacy replay.

Outcome:

```text
REPLAY_PENDING
EXECUTION_REPLAY_ONLY
LEGITIMACY_REPLAY_FAILED
```

---

## Lag Failure Classes

```text
INTAKE_LAG_EXCEEDED
CLASSIFICATION_LAG_EXCEEDED
ENVELOPE_LAG_EXCEEDED
STANDING_RECONSTRUCTION_LAG
FIELD_BINDING_LAG
REGION_EVALUATION_LAG
EFFECT_MAP_LAG
GATE_RESOLUTION_LAG
EFFECT_GUARD_LAG
RECEIPT_ISSUANCE_LAG
REPLAY_LAG
PROOF_SURFACE_LAG
OUTCOME_PUBLICATION_LAG
TOTAL_CORRIDOR_LAG_EXCEEDED
```

These are not performance-only labels.

They explain where admissibility or replay confidence may have degraded.

---

## Latency Receipts

Every corridor run should produce a latency receipt.

Required fields:

```text
latency_receipt_id
event_id
envelope_id
movement_id
corridor_id
started_at
finished_at
total_latency_ms
stage_latency_ms
corridor_latency_ceiling_ms
stale_threshold_ms
field_changed_during_evaluation
latency_verdict
failure_class
reentry_required
```

---

## Latency Verdicts

```text
LATENCY_OK
LATENCY_WARN
LATENCY_ESCALATE
LATENCY_REENTRY_REQUIRED
LATENCY_REFUSE
```

### LATENCY_OK

All stage and total latency stayed inside the corridor budget.

### LATENCY_WARN

A stage approached budget but standing remained current.

### LATENCY_ESCALATE

Latency exceeded corridor ceiling but external resolution may still preserve standing.

### LATENCY_REENTRY_REQUIRED

Field conditions may have changed or freshness cannot be proven.

### LATENCY_REFUSE

Latency destroyed current standing or replayability.

---

## Outcome Matrix

### Clean Run

```text
LATENCY_OK
FIELD_BOUND
GATE_RESOLVED
RECEIPT_ISSUED
LEGITIMACY_REPLAY_VALID
PROOF_SURFACE_VALID
```

Meaning:

```text
Pipeline delay did not degrade standing or replay.
```

### Slow but Recoverable

```text
LATENCY_ESCALATE
ESCALATE
```

Meaning:

```text
The movement cannot bind yet. External or higher-authority resolution is required.
```

### Field Changed During Lag

```text
LATENCY_REENTRY_REQUIRED
REENTRY_REQUIRED
```

Meaning:

```text
Prior standing cannot be inherited. The movement must re-enter the gate under current field state.
```

### Lag Destroyed Standing

```text
LATENCY_REFUSE
REFUSE
```

Meaning:

```text
Freshness, authority, evidence, witness, or replayability failed before consequence could bind.
```

### Replay Lag Collapse

```text
REPLAY_LAG
EXECUTION_REPLAY_ONLY
CONTROL_SURFACE_ONLY
```

Meaning:

```text
The system may preserve terminal outcome, but legitimacy replay is not proven.
```

---

## Gate Rule Under Lag

The gate must not silently allow movement when latency creates uncertainty.

```text
uncertain_current_standing -> ESCALATE or REFUSE
```

Never:

```text
uncertain_current_standing -> ALLOW
```

---

## Doctrine

Lag is not just delay.

Lag is a standing condition.

```text
If latency outruns current standing, the movement must re-enter the field.
If replay cannot reconstruct what was current, the proof collapses.
If protected effect forms during unresolved lag, governance fails.
```
