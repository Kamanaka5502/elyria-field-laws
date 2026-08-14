# Verification Scope

This corpus defines the governing vocabulary and bounded executable proof surfaces for consequence admission.

## Canonical invariants

- protected binding requires `K(M) = ALLOW`;
- uncertain current standing may not become `ALLOW`;
- replay of execution is not, by itself, replay of legitimacy;
- a valid endpoint pair does not prove a valid movement path;
- standing at one time does not imply standing at a later time without continuity/revalidation;
- changed governing state must invalidate inherited admissibility or alter the proof basis.

## Performance claims

Latency values in this repository are corridor-specific targets or measurements. They are not general-purpose system-performance claims unless independently reproduced under the stated environment and method.

## Proof boundary

The repository demonstrates bounded laws and executable proof semantics. It does not establish universal safety, production certification, or third-party validation.