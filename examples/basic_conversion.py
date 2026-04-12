from orthogonal_time.converter import convert_hms
from orthogonal_time.notation import format_standard, format_full

for hour in [12, 1, 2, 3, 4, 5, 6]:
    state = convert_hms(hour, 0, 0)
    print(format_standard(state), "|", format_full(state))
