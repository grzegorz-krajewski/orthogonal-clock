"""Mechanical / analog style experiments for Orthogonal Clock.

This module is intentionally non-normative.
Use `core/orthogonal_time` for the reference computational model.
"""

from orthogonal_time.converter import convert_hms
from orthogonal_time.notation import format_standard


def demo():
    state = convert_hms(3, 0, 0)
    print(format_standard(state))


if __name__ == '__main__':
    demo()
