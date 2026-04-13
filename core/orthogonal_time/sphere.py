from .model import SphereValue


def compute_sphere(h12: int) -> SphereValue:
    return "-" if 3 <= h12 < 9 else "+"