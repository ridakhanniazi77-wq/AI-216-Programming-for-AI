"""Task 4: Percentage calculator with validation and exceptions."""


def calculate_percentage(obtained, total):
    """Calculate percentage, rejecting logically invalid marks."""
    if total <= 0:
        raise ValueError("Total marks must be greater than zero.")
    if obtained < 0:
        raise ValueError("Obtained marks cannot be negative.")
    if obtained > total:
        raise ValueError("Obtained marks cannot exceed total marks.")
    return (obtained / total) * 100


def main():
    try:
        obtained = float(input("Enter obtained marks: "))
        total = float(input("Enter total marks: "))
        percentage = calculate_percentage(obtained, total)
    except ValueError as error:
        print("Input error:", error)
    else:
        print(f"Percentage: {percentage:.2f}%")
    finally:
        print("Percentage calculation finished.")


if __name__ == "__main__":
    main()

# Test cases for README:
# (80, 100) -> 80.0%; (-5, 100) -> ValueError
# (120, 100) -> ValueError; (80, 0) -> ValueError
# non-numeric input -> ValueError from float(...)
