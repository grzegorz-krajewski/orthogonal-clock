import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from core.orthogonal_time.converter import convert_hms
from core.orthogonal_time.notation import (
    format_full,
    format_short,
    format_standard,
    to_machine_dict,
)


def test_standard_notation_03_00():
    state = convert_hms(3, 0, 0)
    assert format_standard(state) == "[-] C3 O0.00 ?"


def test_standard_notation_01_00():
    state = convert_hms(1, 0, 0)
    assert format_standard(state) == "[+] C1 O60.00 ?"


def test_short_notation():
    state = convert_hms(5, 0, 0)
    assert format_short(state) == "-5:60.00?"


def test_full_notation_contains_fields():
    state = convert_hms(1, 0, 0)
    output = format_full(state)
    assert "S=" in output
    assert "C=" in output
    assert "Orth=" in output
    assert "Oi=" in output
    assert "Ce=" in output
    assert "Tr=" in output


def test_machine_dict():
    state = convert_hms(9, 0, 0)
    data = to_machine_dict(state)

    assert data["system"] == "orthogonal-time"
    assert data["sphere"] == "+"
    assert data["cycle"] == 9
    assert data["orth"] == 0.0
    assert data["orth_int"] == 0
    assert data["centi"] == 0
    assert data["trend"] == "unknown"


if __name__ == "__main__":
    test_standard_notation_03_00()
    test_standard_notation_01_00()
    test_short_notation()
    test_full_notation_contains_fields()
    test_machine_dict()
    print("test_notation.py OK")