"""Task 4: Percentage calculator with input validation."""


def calculate_percentage(obtained, total):
    """Calculate percentage; reject invalid mark combinations."""
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
        print("Invalid input:", error)
    else:
        print(f"Percentage: {percentage:.2f}%")
    finally:
        print("Percentage calculation finished.")


if __name__ == "__main__":
    main()
