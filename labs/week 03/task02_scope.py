"""Task 2: Scope and explicit dependencies."""

score = 90


def show_score():
    score = 70
    print("Inside function:", score)


def is_qualified(score, threshold):
    """Return whether score meets an explicitly supplied threshold."""
    return score >= threshold


if __name__ == "__main__":
    show_score()
    print("Outside function:", score)

    threshold = 0.85
    for test_score in [0.80, 0.85, 0.95]:
        print(
            f"Score {test_score} qualified:",
            is_qualified(test_score, threshold),
        )

# The function's score variable is local to show_score; the module-level
# score is global. Explicit parameters make dependencies clear and tests
# easier because the function does not rely on hidden global state.
