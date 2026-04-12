from orthogonal_time.converter import convert_hms
from orthogonal_time.notation import format_standard

samples = [
    (12, 0, 0),
    (1, 0, 0),
    (2, 0, 0),
    (3, 0, 0),
    (4, 0, 0),
    (5, 0, 0),
    (6, 0, 0),
]

for h, m, s in samples:
    state = convert_hms(h, m, s)
    print(f"Classic {h:02d}:{m:02d}:{s:02d} -> {format_standard(state)}")
