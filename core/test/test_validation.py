import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from core.orthogonal_time.converter import convert_hms


def test_invalid_hour_low():
    try:
        convert_hms(-1, 0, 0)
        raise AssertionError("Expected ValueError for hour=-1")
    except ValueError:
        pass


def test_invalid_hour_high():
    try:
        convert_hms(24, 0, 0)
        raise AssertionError("Expected ValueError for hour=24")
    except ValueError:
        pass


def test_invalid_minute_low():
    try:
        convert_hms(0, -1, 0)
        raise AssertionError("Expected ValueError for minute=-1")
    except ValueError:
        pass


def test_invalid_minute_high():
    try:
        convert_hms(0, 60, 0)
        raise AssertionError("Expected ValueError for minute=60")
    except ValueError:
        pass


def test_invalid_second_low():
    try:
        convert_hms(0, 0, -1)
        raise AssertionError("Expected ValueError for second=-1")
    except ValueError:
        pass


def test_invalid_second_high():
    try:
        convert_hms(0, 0, 60)
        raise AssertionError("Expected ValueError for second=60")
    except ValueError:
        pass


if __name__ == "__main__":
    test_invalid_hour_low()
    test_invalid_hour_high()
    test_invalid_minute_low()
    test_invalid_minute_high()
    test_invalid_second_low()
    test_invalid_second_high()
    print("test_validation.py OK")