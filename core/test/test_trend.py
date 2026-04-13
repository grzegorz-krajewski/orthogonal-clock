import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from core.orthogonal_time.converter import convert_hms
from core.orthogonal_time.trend import compute_observational_trend


def test_unknown_when_previous_missing():
    current = convert_hms(1, 0, 0)
    assert compute_observational_trend(None, current) == "unknown"


def test_up_trend():
    previous = convert_hms(3, 0, 0)   # 0
    current = convert_hms(4, 0, 0)    # 30
    assert compute_observational_trend(previous, current) == "up"


def test_down_trend():
    previous = convert_hms(5, 0, 0)   # 60
    current = convert_hms(4, 0, 0)    # 30
    assert compute_observational_trend(previous, current) == "down"


def test_steady_trend():
    previous = convert_hms(3, 0, 0)   # 0
    current = convert_hms(9, 0, 0)    # 0
    assert compute_observational_trend(previous, current) == "steady"


if __name__ == "__main__":
    test_unknown_when_previous_missing()
    test_up_trend()
    test_down_trend()
    test_steady_trend()
    print("test_trend.py OK")