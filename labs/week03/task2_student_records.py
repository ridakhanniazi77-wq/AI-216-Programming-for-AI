# Task 2: Student Record Processor

students = {
    "Ali": [65, 70, 80],
    "Sara": [90, 85, 88],
    "Ahmed": [40, 55, 60]
}


def calculate_average(marks):
    """Calculate the average marks."""
    return sum(marks) / len(marks)


def check_pass(average):
    """Check whether a student has passed."""
    return average >= 50


def display_summary(name, marks):
    """Display a summary for one student."""
    average = calculate_average(marks)
    passed = check_pass(average)

    print(f"Student: {name}")
    print(f"Marks: {marks}")
    print(f"Average: {average:.2f}")
    print(f"Status: {'Passed' if passed else 'Failed'}")
    print("--------------------")


for name, marks in students.items():
    display_summary(name, marks)