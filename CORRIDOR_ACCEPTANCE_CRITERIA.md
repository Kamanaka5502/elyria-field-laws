# Corridor Acceptance Criteria

## Core Claim

A bounded corridor is accepted only when it proves consequence-bound governance end to end.

A corridor is not accepted because it runs.

A corridor is accepted only when it preserves movement, standing, protected effect, receipt, replay, and proof-surface validity under both positive and negative cases.

---

## Acceptance Rule

A corridor is accepted when it demonstrates:

```text
ALLOW -> protected effect may form -> legitimacy replay valid -> proof surface valid
```

and:

```text
NON_ALLOW -> protected effect prevented -> legitimacy replay valid -> proof surface valid
```

It must also demonstrate collapse when governance proof fails.

---

## Required Positive Case

The positive case must show:

```text
movement object present
lawful region satisfied
hard gates pass
kernel decision = ALLOW
protected effect mapped
protected effect allowed
receipt bound to movement and effect
legitimacy replay valid
proof surface valid
```

This proves consequence admission under valid standing.

---

## Required Negative Case

The negative case must show:

```text
movement object present
standing failure or field failure present
kernel decision != ALLOW
protected effect mapped
protected effect prevented
failure class preserved
receipt bound to movement and effect
legitimacy replay valid
proof surface valid
```

This proves consequence prevention under failed standing.

---

## Required Collapse Cases

The corridor must reject or collapse proof when:

```text
protected effect forms under non-allow
protected effect is unmapped
failure class is missing
receipt is unbound
replay is execution-only
lawful region state is missing
standing basis is missing
kernel decision is missing
```

These cases must resolve to:

```text
CONTROL_SURFACE_ONLY
```

or:

```text
PROOF_SURFACE_INCOMPLETE
```

---

## Non-Acceptance Conditions

A corridor is not accepted if it only proves:

```text
execution completed
log recorded
decision returned
receipt generated
rollback occurred
human approval captured
policy check passed
```

Those may be useful artifacts.

They do not prove consequence-bound governance unless the full proof surface holds.

---

## Acceptance Checklist

A corridor must preserve:

1. movement identity;
2. lawful-region state;
3. current standing basis;
4. kernel decision;
5. protected-effect identity;
6. effect admission or prevention;
7. structured failure class for non-allow;
8. receipt binding;
9. legitimacy replay;
10. final proof-surface verdict.

---

## Doctrine

The corridor is accepted only when it proves both sides of the boundary:

```text
what may bind
and
what cannot bind
```

A corridor that cannot prove both is not product-ready.
