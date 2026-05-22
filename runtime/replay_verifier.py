"""Legitimacy replay verifier for Elyria Field Laws.

Execution replay and legitimacy replay are not the same proof class.

This verifier checks whether a replay object preserves the admissibility basis,
not merely the terminal outcome.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Optional


class ReplayVerdict(str, Enum):
    LEGITIMACY_REPLAY_VALID = "LEGITIMACY_REPLAY_VALID"
    EXECUTION_REPLAY_ONLY = "EXECUTION_REPLAY_ONLY"
    REPLAY_INVALID = "REPLAY_INVALID"


REQUIRED_LEGITIMACY_FIELDS = (
    "movement_hash",
    "origin_state_hash",
    "target_state_hash",
    "authority_hash",
    "evidence_hash",
    "lineage_hash",
    "recovery_hash",
    "consequence_hash",
    "witness_hash",
    "trajectory_hash",
    "admissibility_distance_hash",
    "law_version_hash",
    "kernel_resolution_hash",
    "protected_effect_hash",
)


@dataclass(frozen=True)
class ReplayObject:
    replay_id: str
    terminal_outcome_hash: str
    legitimacy_fields: Dict[str, Optional[str]]
    reconstructed_decision: str
    original_decision: str
    reconstructed_bind_status: bool
    original_bind_status: bool


@dataclass(frozen=True)
class ReplayReceipt:
    replay_id: str
    verdict: ReplayVerdict
    legitimacy_replay_valid: bool
    terminal_outcome_present: bool
    missing_fields: List[str]
    mismatched_decision: bool
    mismatched_bind_status: bool
    reason: str
    rule_trace: List[str]


def verify_legitimacy_replay(replay: ReplayObject) -> ReplayReceipt:
    """Verify legitimacy replay, not merely outcome replay."""

    trace: List[str] = ["replay.object.present"]
    terminal_present = bool(replay.terminal_outcome_hash)

    if terminal_present:
        trace.append("terminal_outcome.present")
    else:
        trace.append("terminal_outcome.missing")

    missing = [
        field
        for field in REQUIRED_LEGITIMACY_FIELDS
        if not replay.legitimacy_fields.get(field)
    ]

    if missing:
        trace.append("legitimacy_fields.missing:" + ",".join(missing))

    mismatched_decision = replay.reconstructed_decision != replay.original_decision
    if mismatched_decision:
        trace.append("decision.mismatch")

    mismatched_bind_status = replay.reconstructed_bind_status != replay.original_bind_status
    if mismatched_bind_status:
        trace.append("bind_status.mismatch")

    if not terminal_present:
        return ReplayReceipt(
            replay_id=replay.replay_id,
            verdict=ReplayVerdict.REPLAY_INVALID,
            legitimacy_replay_valid=False,
            terminal_outcome_present=False,
            missing_fields=missing,
            mismatched_decision=mismatched_decision,
            mismatched_bind_status=mismatched_bind_status,
            reason="Replay does not preserve terminal outcome.",
            rule_trace=trace,
        )

    if missing or mismatched_decision or mismatched_bind_status:
        trace.append("execution_replay_only")
        return ReplayReceipt(
            replay_id=replay.replay_id,
            verdict=ReplayVerdict.EXECUTION_REPLAY_ONLY,
            legitimacy_replay_valid=False,
            terminal_outcome_present=True,
            missing_fields=missing,
            mismatched_decision=mismatched_decision,
            mismatched_bind_status=mismatched_bind_status,
            reason="Replay preserves outcome but does not reconstruct full admissibility basis.",
            rule_trace=trace,
        )

    trace.append("legitimacy_replay.valid")
    return ReplayReceipt(
        replay_id=replay.replay_id,
        verdict=ReplayVerdict.LEGITIMACY_REPLAY_VALID,
        legitimacy_replay_valid=True,
        terminal_outcome_present=True,
        missing_fields=[],
        mismatched_decision=False,
        mismatched_bind_status=False,
        reason="Replay reconstructs terminal outcome and admissibility basis.",
        rule_trace=trace,
    )
