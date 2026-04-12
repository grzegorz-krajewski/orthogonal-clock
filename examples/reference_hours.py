from orthogonal_time.converter import convert_hms

for hour in [12, 1, 2, 3, 4, 5, 6, 9]:
    state = convert_hms(hour, 0, 0)
    print(f"{hour:02d}:00:00 -> Orth={state.orth:.2f}")
