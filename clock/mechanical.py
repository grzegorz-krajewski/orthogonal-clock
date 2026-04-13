from datetime import datetime
import time

from core.orthogonal_time.converter import convert_hms
from core.orthogonal_time.notation import format_standard


def current_display() -> str:
    now = datetime.now()
    state = convert_hms(now.hour, now.minute, now.second)
    return format_standard(state)


def demo():
    last_display = None

    try:
        while True:
            display = current_display()

            if display != last_display:
                print("\r" + display, end="", flush=True)
                last_display = display

            time.sleep(0.05)
    except KeyboardInterrupt:
        print()


if __name__ == "__main__":
    demo()