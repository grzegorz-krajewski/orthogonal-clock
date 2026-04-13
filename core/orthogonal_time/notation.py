from __future__ import annotations

from .model import OrthogonalState


TREND_SYMBOLS = {
    "up": "↑",
    "down": "↓",
    "steady": "=",
    "unknown": "?",
}


def format_standard(state: OrthogonalState) -> str:
    trend_symbol = TREND_SYMBOLS[state.trend]
    return f"[{state.sphere}] C{state.cycle} O{state.orth_int}.{state.centi:02d} {trend_symbol}"


def format_short(state: OrthogonalState) -> str:
    trend_symbol = TREND_SYMBOLS[state.trend]
    return f"{state.sphere}{state.cycle}:{state.orth_int}.{state.centi:02d}{trend_symbol}"


def format_full(state: OrthogonalState) -> str:
    trend_symbol = TREND_SYMBOLS[state.trend]
    return (
        "OT["
        f"S={state.sphere}; "
        f"C={state.cycle}; "
        f"Orth={state.orth:.2f}; "
        f"Oi={state.orth_int}; "
        f"Ce={state.centi:02d}; "
        f"Tr={trend_symbol}"
        "]"
    )


def to_machine_dict(state: OrthogonalState) -> dict:
    return {
        "system": "orthogonal-time",
        "version": "0.1",
        "sphere": state.sphere,
        "cycle": state.cycle,
        "orth": state.orth,
        "orth_int": state.orth_int,
        "centi": state.centi,
        "trend": state.trend,
        "base": {
            "hour": state.base_time.hour,
            "minute": state.base_time.minute,
            "second": state.base_time.second,
        },
    }
