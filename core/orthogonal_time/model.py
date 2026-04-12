from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class BaseTime:
    hour: int
    minute: int
    second: int = 0
    scale: str = "local"


@dataclass(frozen=True)
class OrthogonalState:
    base: BaseTime
    h12: int
    hour_angle: float
    minute_angle: float
    reduced_hour_angle: float
    reduced_minute_angle: float
    diff_raw: float
    diff_sym: float
    orth: float
    orth_int: int
    centi: int
    cycle: int
    sphere: Optional[str] = None
    trend: str = "unknown"
