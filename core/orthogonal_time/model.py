from __future__ import annotations

from dataclasses import dataclass
from typing import Literal


TrendValue = Literal["up", "down", "steady", "unknown"]
SphereValue = Literal["+", "-"]


@dataclass(frozen=True)
class BaseTime:
    hour: int
    minute: int
    second: int = 0


@dataclass(frozen=True)
class OrthogonalState:
    base_time: BaseTime
    sphere: SphereValue
    cycle: int
    hour_angle: float
    minute_angle: float
    hour_angle_reduced: float
    minute_angle_reduced: float
    diff_raw: float
    diff_sym: float
    orth: float
    orth_int: int
    centi: int
    trend: TrendValue = "unknown"
