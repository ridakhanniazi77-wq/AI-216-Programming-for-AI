def clean_data(readings):
    cleaned = []

    for value in readings:
        if 0 <= value <= 100:
            cleaned.append(value)

    return cleaned


def calculate_average(data):
    if len(data) == 0:
        return 0

    return sum(data) / len(data)


sensor_readings = [45, 78, -12, 90, 105, 66, 88]

cleaned_readings = clean_data(sensor_readings)
average = calculate_average(cleaned_readings)

print("Original readings:", sensor_readings)
print("Cleaned readings:", cleaned_readings)
print("Average:", average)