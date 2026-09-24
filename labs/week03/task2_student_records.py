def calculate_average(marks):
    return sum(marks) / len(marks)


def check_pass(average):
    return average >= 50


def display_summary(name, marks):
    average = calculate_average(marks)
    passed = check_pass(average)

    print("Student:", name)
    print("Marks:", marks)
    print("Average:", average)

    if passed:
        print("Status: Passed")
    else:
        print("Status: Failed")

    print()


students = {
    "Ali": [65, 70, 80],
    "Sara": [90, 85, 88],
    "Ahmed": [40, 55, 60]
}

for name, marks in students.items():
    display_summary(name, marks)