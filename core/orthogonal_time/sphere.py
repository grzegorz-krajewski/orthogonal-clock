from __future__ import annotations

from .model import SphereValue


def compute_sphere(h12: int) -> SphereValue:
    """
    Robocza definicja Sfery zgodna ze spec v0.1.
    Uwaga: ta wersja operuje na modelu 12-godzinnym (h12), nie na pełnej godzinie dobowej.
    Status: przejściowy.
    """
    if not 0 <= h12 <= 11:
        raise ValueError("h12 must be between 0 and 11")
    return "-" if 3 <= h12 < 9 else "+"
