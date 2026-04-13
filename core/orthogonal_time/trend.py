from .converter import convert_hms
from .model import BaseTime, OrthogonalState, TrendValue


def compute_observational_trend(
    previous: OrthogonalState | None,
    current: OrthogonalState | None,
    *,
    epsilon: float = 1e-9,
) -> TrendValue:
    if previous is None or current is None:
        return "unknown"

    if current.orth > previous.orth + epsilon:
        return "up"

    if current.orth < previous.orth - epsilon:
        return "down"

    return "steady"


def compute_local_trend(
    base_time: BaseTime,
    *,
    epsilon_seconds: float = 0.25,
    tolerance: float = 1e-9,
) -> TrendValue:
    current = convert_hms(base_time.hour, base_time.minute, base_time.second)

    future_hour = base_time.hour
    future_minute = base_time.minute
    future_second = base_time.second + epsilon_seconds

    while future_second >= 60:
        future_second -= 60
        future_minute += 1

    while future_minute >= 60:
        future_minute -= 60
        future_hour += 1

    future_hour %= 24

    future = convert_hms(future_hour, future_minute, future_second)

    if future.orth > current.orth + tolerance:
        return "up"
    if future.orth < current.orth - tolerance:
        return "down"

    return "steady"