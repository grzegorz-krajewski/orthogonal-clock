import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from core.orthogonal_time.converter import convert_hms


def test_12_00():
    state = convert_hms(12, 0, 0)
    assert state.orth == 90.0


def test_03_00():
    state = convert_hms(3, 0, 0)
    assert state.orth == 0.0


def test_06_00():
    state = convert_hms(6, 0, 0)
    assert state.orth == 90.0


def test_09_00():
    state = convert_hms(9, 0, 0)
    assert state.orth == 0.0


def test_01_00():
    state = convert_hms(1, 0, 0)
    assert state.orth == 60.0


def test_02_00():
    state = convert_hms(2, 0, 0)
    assert state.orth == 30.0


def test_04_00():
    state = convert_hms(4, 0, 0)
    assert state.orth == 30.0


def test_05_00():
    state = convert_hms(5, 0, 0)
    assert state.orth == 60.0


if __name__ == "__main__":
    test_12_00()
    test_03_00()
    test_06_00()
    test_09_00()
    test_01_00()
    test_02_00()
    test_04_00()
    test_05_00()
    print("test_reference_cases.py OK")