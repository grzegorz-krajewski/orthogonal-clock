from .model import BaseTime, OrthogonalState
from .sphere import compute_sphere


def _reduce_half_turn(angle_degrees: float) -> float:
    return angle_degrees % 180.0


def convert_base_time(base_time: BaseTime) -> OrthogonalState:
    hour = base_time.hour
    minute = base_time.minute
    second = base_time.second

    if not 0 <= hour <= 23:
        raise ValueError("hour must be between 0 and 23")
    if not 0 <= minute <= 59:
        raise ValueError("minute must be between 0 and 59")
    if not 0 <= second < 60:
        raise ValueError("second must be between 0 and <60")

    h12 = hour % 12

    hour_angle = 30.0 * h12 + 0.5 * minute + (1.0 / 120.0) * second
    minute_angle = 6.0 * minute + 0.1 * second

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
        orth=orth,
        orth_int=orth_int,
        centi=centi,
        trend="unknown",
        hour_angle=hour_angle,
        minute_angle=minute_angle,
        hour_angle_reduced=hour_angle_reduced,
        minute_angle_reduced=minute_angle_reduced,
        diff_raw=diff_raw,
        diff_sym=diff_sym,
    )


def convert_hms(hour: int, minute: int, second: float = 0) -> OrthogonalState:
    return convert_base_time(BaseTime(hour=hour, minute=minute, second=second))