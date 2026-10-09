# Lab 03 — Functions, Modules, Exceptions, Debugging & OOP

**Course:** AI-216 Programming for Artificial Intelligence  
**Semester:** Fall 2026  
**Week:** 03

## Concepts Practiced
- Functions and return values
- Local and global scope
- Modules and imports
- `if __name__ == "__main__"`
- Exception handling and validation
- Debugging logic errors
- Classes, objects, attributes, and methods
- Refactoring and separation of concerns

## Tasks Completed
1. Function Design & Reuse — `task01_functions.py`
2. Scope & Hidden State — `task02_scope.py`
3. Own Module — `task03_modules/`
4. Exception Handling — `task04_exceptions.py`
5. Debugging Challenge — `task05_debugging.py`
6. `ScoreAnalyzer` Class — `task06_oop.py`
7. Refactoring into Modules + Class — `task07_refactor/`
8. Optional Threshold Classifier — `task_optional_classifier.py`

## Task 2: Scope Answers
- The values differ because `show_score()` creates a local variable named `score` whose value is 70. It does not overwrite the global `score`, which remains 90.
- The `score` inside `show_score()` is local. The `score` declared at the top level is global.
- Passing `threshold` as an explicit argument makes the dependency visible, so the function can be reused with different thresholds and tested without relying on hidden global state.

## Task 3: Main Guard
`if __name__ == "__main__":` runs the demo only when `score_utils.py` is executed directly. When another file imports the module, the demo does not run automatically.

## Task 4: Exception Handling Test Cases
Run the program and enter each case when prompted.

| Case | Input (obtained, total) | Expected result |
| --- | --- | --- |
| Valid | `80, 100` | `80.00%` |
| Negative obtained | `-5, 100` | Validation error |
| Obtained exceeds total | `120, 100` | Validation error |
| Zero total | `80, 0` | Validation error |
| Non-numeric | `hello, 100` | Input conversion error |

Actual results should be confirmed by running the program in your environment.

## Task 5: Debugging Notes
- **Expected output:** Average `75.0`, result `Pass`.
- **Original average bug:** The loop used `total = score`, replacing the running total on every iteration. It should use `total += score`.
- **Original classification bug:** `average >= 50` appeared before `average >= 85`, so an average of 85 or more would be classified as `Pass`. Check the higher threshold first.
- **How to locate it:** Trace `total` for each score and inspect the order of the `if` conditions.
- **Corrected output:** `Average: 75.0` and `Result: Pass`.

## Task 6: Design Decisions
- Functions are suitable for standalone operations that do not need to preserve state.
- A class is useful when data (`self.scores`) and operations on that data belong together.
- In Task 7, `main.py` coordinates the workflow; cleaning belongs in `preprocessing.py`, and score analysis belongs in `analyzer.py`.

## What I Found Difficult
- Review and replace this note with the part you personally found most difficult.

## What I Learned
- Review and replace this note with your own learning reflection.

## AI Engineering Relevance
Reusable functions, modules, validation, debugging, and classes help keep data-processing and AI workflows understandable, testable, and maintainable.

## AI Usage Log

### Tool Used
ChatGPT

### What I Asked
Help organize and implement the Lab 03 tasks from the provided lab instructions.

### What I Used
Used assistance to draft example implementations, test structure, and README explanations.

### What I Verified or Changed Myself
Run each script, inspect its output, and edit this section to accurately describe the testing and changes you personally completed before submission.

## How to Run
From the repository root:

```powershell
python labs/week03/task01_functions.py
python labs/week03/task02_scope.py
python labs/week03/task03_modules/score_utils.py
python labs/week03/task03_modules/main.py
python labs/week03/task04_exceptions.py
python labs/week03/task05_debugging.py
python labs/week03/task06_oop.py
python labs/week03/task07_refactor/main.py
python labs/week03/task_optional_classifier.py
```
