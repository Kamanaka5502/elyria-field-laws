# Field Laws

This file is the doctrine index for Elyria Field Laws.

The field laws define what must remain true before proposed movement can acquire binding consequence.

The system is not governed because it can observe, approve, log, attest, or explain.

The system is governed only when inadmissible movement cannot bind.

---

## Law 1 — Non-Binding Movement

A system is not governed because it can refuse an action.

A system is governed only when inadmissible movement cannot acquire binding status.

```text
BIND(M) is defined only when K(M) = ALLOW.
```

If `K(M)` resolves to `REDIRECT`, `ESCALATE`, `REFUSE`, or `HALT`, the proposed movement is non-binding.

---

## Law 2 — Legitimacy Replay Separation

Execution replay and legitimacy replay are not the same proof class.

A system can reproduce the same terminal consequence while losing whether the movement that produced it remained lawful.

Replay must preserve admissibility differentiation, not merely outcome consistency.

---

## Law 3 — Redirect Non-Laundering

A redirect is lawful only when it reduces admissibility distance without bypassing hard gates.

```text
delta(M_redirected) < delta(M_original)
```

If redirect does not reduce admissibility distance, it is not repair.

It is laundering.

---

## Law 4 — Hard Gate Non-Compensation

Operational strength cannot compensate for failed authority, lineage, evidence, consequence, or witness gates.

Soft dimensions may influence readiness.

They may not purchase standing.

---

## Law 5 — Endpoint Is Not Path Validity

A valid origin and valid target do not prove lawful movement.

Movement must remain admissible across the transition path.

```text
M(tau) must preserve harmonic admissibility across the sampled trajectory.
```

Endpoint checking is insufficient when consequence binds through transition.

---

## Law 6 — Observation Is Not Custody

Observation can describe state.

Custody governs whether state may lawfully move into consequence.

A dashboard, report, or log is not custody unless it controls binding.

---

## Law 7 — Attestation Is Not Admissibility

Hardware or cryptographic attestation may prove execution environment integrity.

It does not, by itself, prove lawful consequence binding.

Attestation can support admissibility.

It cannot replace it.

---

## Law 8 — Operational Success Is Not Lawful Continuation

A system can remain operational while legitimacy collapses underneath it.

Operational continuity cannot buy authority.

Policy compliance cannot replace lineage.

Replay cannot replace legitimacy.

---

## Kernel Summary

```text
K(M) = {
  ALLOW    if M is inside the admissible region Omega;
  REDIRECT if a lawful correction path reduces admissibility distance;
  ESCALATE if uncertainty is externally resolvable;
  REFUSE   if a hard gate failure blocks admissibility;
  HALT     if continued movement expands illegitimate consequence.
}
```

```text
BIND(M) is defined only when K(M) = ALLOW.
```

Everything else is non-binding.
