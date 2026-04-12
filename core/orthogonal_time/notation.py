from __future__ import annotations

from .model import OrthogonalState

TREND_SYMBOLS = {
    "up": "↑",
    "down": "↓",
    "steady": "=",
    "unknown": "?",
}


def format_standard(state: OrthogonalState) -> str:
    sphere = state.sphere if state.sphere is not None else "?"
    trend = TREND_SYMBOLS.get(state.trend, "?")
    return f"[{sphere}] C{state.cycle} O{state.orth_int}.{state.centi:02d} {trend}"


def format_short(state: OrthogonalState) -> str:
    sphere = state.sphere if state.sphere is not None else "?"
    trend = TREND_SYMBOLS.get(state.trend, "?")
    return f"{sphere}{state.cycle}:{state.orth_int}.{state.centi:02d}{trend}"


def format_full(state: OrthogonalState) -> str:
    sphere = state.sphere if state.sphere is not None else "?"
    trend = TREND_SYMBOLS.get(state.trend, "?")
    return (
        f"OT[S={sphere}; C={state.cycle}; Orth={state.orth:.2f}; "
        f"Oi={state.orth_int}; Ce={state.centi:02d}; Tr={trend}]"
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
            "scale": state.base.scale,
            "hour": state.base.hour,
            "minute": state.base.minute,
            "second": state.base.second,
        },
    }
