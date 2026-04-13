from dataclasses import dataclass
from typing import Literal


TrendValue = Literal["up", "down", "steady", "unknown"]
SphereValue = Literal["+", "-"]


@dataclass(frozen=True)
class BaseTime:
    hour: int
    minute: int
    second: float = 0


@dataclass(frozen=True)
class OrthogonalState:
    base_time: BaseTime
    sphere: SphereValue
    cycle: int
    orth: float
    orth_int: int
    centi: int
    trend: TrendValue = "unknown"
    hour_angle: float = 0.0
    minute_angle: float = 0.0
    hour_angle_reduced: float = 0.0
    minute_angle_reduced: float = 0.0
    diff_raw: float = 0.0
    diff_sym: float = 0.0