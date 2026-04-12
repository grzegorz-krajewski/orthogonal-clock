from __future__ import annotations


def compute_sphere(h12: int) -> str:
    """Compute temporary sphere value for v0.1.

    Status:
        Transitional / experimental. The v0.1 spec treats sphere
        as useful but not fully mathematically closed.
    """
    if 3 <= h12 < 9:
        return "-"
    return "+"
