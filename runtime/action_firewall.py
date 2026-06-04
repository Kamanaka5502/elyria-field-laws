from __future__ import annotations

import json
from dataclasses import asdict
from pathlib import Path
from typing import Any, Dict

from runtime.kernel import Movement, resolve


def evaluate_request(payload: Dict[str, Any]) -> Dict[str, Any]:
    movement = Movement(
        movement_id=str(payload.get('movement_id', 'M-ACTION')),
        origin_state=str(payload.get('origin_state', 'intent_formed')),
        target_state=str(payload.get('target_state', 'protected_effect')),
        authority_standing=bool(payload.get('authority_standing', False)),
        lineage_integrity=bool(payload.get('lineage_integrity', False)),
        evidence_freshness=bool(payload.get('evidence_freshness', False)),
        recovery_viability=bool(payload.get('recovery_viability', False)),
        consequence_admissibility=bool(payload.get('consequence_admissibility', False)),
        witness_replay_validity=bool(payload.get('witness_replay_validity', False)),
        trajectory_validity=bool(payload.get('trajectory_validity', False)),
        admissibility_distance=float(payload.get('admissibility_distance', 1.0)),
        external_resolution_available=bool(payload.get('external_resolution_available', False)),
        lawful_redirect_available=bool(payload.get('lawful_redirect_available', False)),
        redirect_distance=payload.get('redirect_distance'),
        continued_movement_expands_risk=bool(payload.get('continued_movement_expands_risk', False)),
        notes=list(payload.get('notes', [])),
    )
    receipt = resolve(movement)
    result = asdict(receipt)
    result['decision'] = receipt.decision.value
    return result
