"""Digital display experiments for Orthogonal Clock."""

from orthogonal_time.converter import convert_hms
from orthogonal_time.notation import format_short


def demo():
    state = convert_hms(5, 0, 0)
    print(format_short(state))


if __name__ == '__main__':
    demo()
