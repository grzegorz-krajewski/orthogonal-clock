from __future__ import annotations

from .model import OrthogonalState, TrendValue


def compute_observational_trend(
    previous: OrthogonalState | None,
    current: OrthogonalState,
    *,
    epsilon: float = 1e-9,
) -> TrendValue:
    if previous is None:
        return "unknown"

    if current.orth > previous.orth + epsilon:
        return "up"

    if current.orth < previous.orth - epsilon:
        return "down"

    return "steady"
