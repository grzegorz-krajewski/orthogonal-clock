from __future__ import annotations

from .model import OrthogonalState


def compute_observational_trend(previous: OrthogonalState, current: OrthogonalState) -> str:
    """Compute observational trend between two states."""
    if current.orth > previous.orth:
        return "up"
    if current.orth < previous.orth:
        return "down"
    return "steady"
