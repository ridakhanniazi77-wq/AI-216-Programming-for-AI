# Task 1: Data Cleaning Functions

sensor_readings = [45, 78, -12, 90, 105, 66, 88]


def clean_data(readings):
    """Remove readings outside the valid range of 0 to 100."""
    cleaned = []

    for value in readings:
        if 0 <= value <= 100:
            cleaned.append(value)

    return cleaned


def calculate_average(readings):
    """Calculate the average of the given readings."""
    if len(readings) == 0:
        return 0

    return sum(readings) / len(readings)


cleaned_data = clean_data(sensor_readings)
average = calculate_average(cleaned_data)

print("Data Cleaning")
print("-------------")
print(f"Original data: {sensor_readings}")
print(f"Cleaned data: {cleaned_data}")
print(f"Average: {average:.2f}")