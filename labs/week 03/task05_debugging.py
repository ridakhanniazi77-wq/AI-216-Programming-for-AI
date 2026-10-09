"""Task 5: Debugging challenge, with the faulty and corrected versions."""


def calculate_average_faulty(scores):
    """Intentionally faulty version, retained to demonstrate debugging."""
    total = 0
    for score in scores:
        total = score  # Bug: this replaces total instead of accumulating.
    return total / len(scores)


def classify_faulty(average):
    """Intentionally faulty condition order."""
    if average >= 50:
        return "Pass"
    elif average >= 85:
        return "Excellent"
    return "Fail"


def calculate_average(scores):
    if not scores:
        return None
    total = 0
    for score in scores:
        total += score
    return total / len(scores)


def classify(average):
    if average is None:
        return "No valid data"
    if average >= 85:
        return "Excellent"
    if average >= 50:
        return "Pass"
    return "Fail"


if __name__ == "__main__":
    scores = [60, 70, 80, 90]
    print("Faulty average:", calculate_average_faulty(scores))
    print("Faulty result:", classify_faulty(calculate_average_faulty(scores)))

    average = calculate_average(scores)
    print("Corrected average:", average)
    print("Corrected result:", classify(average))

# Expected debugging notes:
# Expected average: 75.0; faulty average: 22.5 (the final score is divided
# by the number of scores). The loop must add each score to total.
# The >= 85 check must appear before >= 50 or "Excellent" is unreachable.
