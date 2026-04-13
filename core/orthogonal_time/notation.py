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

def format_presentational(
    state: OrthogonalState,
    *,
    base_hour: int | None = None,
    base_minute: int | None = None,
    base_second: int | None = None,
    show_seconds: bool = False,
) -> str:
    trend_symbol = TREND_SYMBOLS[state.trend]
    left = f"OT[{state.sphere}|C{state.cycle}|O{state.orth_int}.{state.centi:02d}|{trend_symbol}]"

    if base_hour is None or base_minute is None:
        return left

    if show_seconds:
        if base_second is None:
            base_second = 0
        right = f"{base_hour:02d}:{base_minute:02d}:{base_second:02d}"
    else:
        right = f"{base_hour:02d}:{base_minute:02d}"

    return f"{left} @ {right}"

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
    }