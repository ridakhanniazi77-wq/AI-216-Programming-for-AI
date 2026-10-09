"""Task 1: Function design and reuse."""


def calculate_average(scores):
    """Return the average score, or None when scores is empty."""
    if not scores:
        return None
    return sum(scores) / len(scores)


def find_highest(scores):
    """Return the highest score, or None when scores is empty."""
    if not scores:
        return None
    return max(scores)


def count_above_threshold(scores, threshold):
    """Count scores greater than or equal to threshold."""
    return sum(score >= threshold for score in scores)


def classify_average(average):
    """Classify an average using the lab's grade bands."""
    if average is None:
        return "No valid data"
    if average >= 85:
        return "Excellent"
    if average >= 70:
        return "Good"
    if average >= 50:
        return "Satisfactory"
    return "Needs Improvement"


if __name__ == "__main__":
    scores = [78, 85, 92, 67, 88]
    average = calculate_average(scores)
    print("Scores:", scores)
    print("Average:", average)
    print("Highest:", find_highest(scores))
    print("Scores >= 80:", count_above_threshold(scores, 80))
    print("Classification:", classify_average(average))
    print("Empty average:", calculate_average([]))
