"""Task 5: Debugging challenge, with corrected code and notes."""


def calculate_average(scores):
    if not scores:
        return None
    total = 0
    for score in scores:
        total += score  # Fix: accumulate instead of replacing total.
    return total / len(scores)


def classify(average):
    # Check the more specific/higher band before the general passing band.
    if average >= 85:
        return "Excellent"
    elif average >= 50:
        return "Pass"
    return "Fail"


def main():
    scores = [60, 70, 80, 90]
    average = calculate_average(scores)
    print("Average:", average)
    print("Result:", classify(average))


if __name__ == "__main__":
    main()
