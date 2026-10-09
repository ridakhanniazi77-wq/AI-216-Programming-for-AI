"""Task 2: Local scope, global scope, and explicit parameters."""

score = 90


def show_score():
    score = 70  # Local variable; it does not change the global score.
    print("Inside function:", score)


def is_qualified(score, threshold):
    """Return whether score meets the supplied threshold."""
    return score >= threshold


def main():
    show_score()
    print("Outside function:", score)

    threshold = 0.85
    test_values = [0.70, 0.85, 0.92]
    for value in test_values:
        print(f"Score {value:.2f} qualified? {is_qualified(value, threshold)}")


if __name__ == "__main__":
    main()
