import time
from datetime import datetime

from core.orthogonal_time.converter import convert_hms
from core.orthogonal_time.model import BaseTime, OrthogonalState
from core.orthogonal_time.notation import format_presentational
from core.orthogonal_time.trend import compute_local_trend


def with_local_trend(state: OrthogonalState) -> OrthogonalState:
    trend = compute_local_trend(state.base_time)
    return OrthogonalState(
        base_time=state.base_time,
        sphere=state.sphere,
        cycle=state.cycle,
        orth=state.orth,
        orth_int=state.orth_int,
        centi=state.centi,
        trend=trend,
        hour_angle=state.hour_angle,
        minute_angle=state.minute_angle,
        hour_angle_reduced=state.hour_angle_reduced,
        minute_angle_reduced=state.minute_angle_reduced,
        diff_raw=state.diff_raw,
        diff_sym=state.diff_sym,
    )


def demo():
    last_display = None

    try:
        while True:
            now = datetime.now()
            state = convert_hms(now.hour, now.minute, now.second)
            state = with_local_trend(state)

            display = format_presentational(
                state,
                base_hour=now.hour,
                base_minute=now.minute,
                base_second=now.second,
                show_seconds=False,
            )

            if display != last_display:
                print("\r" + display, end="", flush=True)
                last_display = display

            time.sleep(0.05)
    except KeyboardInterrupt:
        print()


if __name__ == "__main__":
    demo()