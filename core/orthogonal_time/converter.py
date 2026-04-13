from __future__ import annotations

from datetime import datetime

from .model import BaseTime, OrthogonalState
from .sphere import compute_sphere


def _reduce_half_turn(angle_degrees: float) -> float:
    return angle_degrees % 180.0


def _validate_time(hour: int, minute: int, second: int) -> None:
    if not 0 <= hour <= 23:
        raise ValueError("hour must be between 0 and 23")
    if not 0 <= minute <= 59:
        raise ValueError("minute must be between 0 and 59")
    if not 0 <= second <= 59:
        raise ValueError("second must be between 0 and 59")


def convert_hms(hour: int, minute: int, second: int = 0) -> OrthogonalState:
    _validate_time(hour, minute, second)
    base_time = BaseTime(hour=hour, minute=minute, second=second)
    return convert_base_time(base_time)


def convert_datetime(dt: datetime) -> OrthogonalState:
    return convert_hms(dt.hour, dt.minute, dt.second)


def convert_base_time(base_time: BaseTime) -> OrthogonalState:
    _validate_time(base_time.hour, base_time.minute, base_time.second)

    h12 = base_time.hour % 12

    hour_angle = 30.0 * h12 + 0.5 * base_time.minute + (1.0 / 120.0) * base_time.second
    minute_angle = 6.0 * base_time.minute + 0.1 * base_time.second

    hour_angle_reduced = _reduce_half_turn(hour_angle)
    minute_angle_reduced = _reduce_half_turn(minute_angle)

    diff_raw = abs(hour_angle_reduced - minute_angle_reduced)
    diff_sym = min(diff_raw, 180.0 - diff_raw)

    orth = abs(90.0 - diff_sym)
    orth_int = int(orth)
    centi = int((orth - orth_int) * 100)

    return OrthogonalState(
        base_time=base_time,
        sphere=compute_sphere(h12),
        cycle=h12,
        hour_angle=hour_angle,
        minute_angle=minute_angle,
        hour_angle_reduced=hour_angle_reduced,
        minute_angle_reduced=minute_angle_reduced,
        diff_raw=diff_raw,
        diff_sym=diff_sym,
        orth=orth,
        orth_int=orth_int,
        centi=centi,
        trend="unknown",
    )
