from __future__ import annotations

import math

from .model import BaseTime, OrthogonalState
from .sphere import compute_sphere


def reduce_half_turn(angle: float) -> float:
    """Reduce angle into [0, 180) using modulo 180."""
    return angle % 180.0


def convert_base_time(base: BaseTime, include_sphere: bool = True, trend: str = "unknown") -> OrthogonalState:
    """Convert base time into Orthogonal Time state according to spec v0.1."""
    h12 = base.hour % 12

    hour_angle = 30.0 * h12 + 0.5 * base.minute + (1.0 / 120.0) * base.second
    minute_angle = 6.0 * base.minute + 0.1 * base.second

    reduced_hour_angle = reduce_half_turn(hour_angle)
    reduced_minute_angle = reduce_half_turn(minute_angle)

    diff_raw = abs(reduced_hour_angle - reduced_minute_angle)
    diff_sym = min(diff_raw, 180.0 - diff_raw)

    orth = abs(90.0 - diff_sym)
    orth_int = int(math.floor(orth))
    centi = int(math.floor((orth - orth_int) * 100))

    cycle = base.hour % 12
    sphere = compute_sphere(h12) if include_sphere else None

    return OrthogonalState(
        base=base,
        h12=h12,
        hour_angle=hour_angle,
        minute_angle=minute_angle,
        reduced_hour_angle=reduced_hour_angle,
        reduced_minute_angle=reduced_minute_angle,
        diff_raw=diff_raw,
        diff_sym=diff_sym,
        orth=orth,
        orth_int=orth_int,
        centi=centi,
        cycle=cycle,
        sphere=sphere,
        trend=trend,
    )


def convert_hms(hour: int, minute: int, second: int = 0, scale: str = "local", include_sphere: bool = True) -> OrthogonalState:
    """Convenience wrapper for direct h:m:s conversion."""
    base = BaseTime(hour=hour, minute=minute, second=second, scale=scale)
    return convert_base_time(base=base, include_sphere=include_sphere)
