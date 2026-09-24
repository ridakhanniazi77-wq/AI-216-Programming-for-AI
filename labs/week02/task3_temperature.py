temperatures = [18, 22, 31, 27, 35, 29, 15, 33]

normal_count = 0
high_count = 0

for temperature in temperatures:
    if 15 <= temperature <= 30:
        normal_count += 1
    elif temperature > 30:
        high_count += 1

print("Normal readings:", normal_count)
print("High readings:", high_count)