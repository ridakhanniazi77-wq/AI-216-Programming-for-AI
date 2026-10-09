# Lab 03 — Functions, Modules, Exceptions, Debugging & OOP

**Course:** AI-216 Programming for Artificial Intelligence  
**Semester:** Fall 2026  
**Week:** 03

## Concepts Practiced
- Functions and return values
- Local and global scope
- Modules and imports
- `if __name__ == "__main__":`
- Exception handling and input validation
- Debugging logic errors
- Classes, objects, attributes, and methods
- Refactoring into separate modules

## Tasks Completed
1. Function Design — `task01_functions.py`
2. Scope — `task02_scope.py`
3. Modules — `task03_modules/`
4. Exception Handling — `task04_exceptions.py`
5. Debugging Challenge — `task05_debugging.py`
6. ScoreAnalyzer Class — `task06_oop.py`
7. Refactoring — `task07_refactor/`
8. Optional Threshold Classifier — `optional_threshold_classifier.py`

## Scope Notes
Inside `show_score()`, `score = 70` is a local variable. The module-level `score = 90` is global. The local assignment does not change the global value. Passing the threshold explicitly to `is_qualified(score, threshold)` makes the dependency visible and makes the function easier to reuse and test.

## Modules and the Main Guard
A module is a Python file that can define reusable functions and classes. `if __name__ == "__main__":` runs the demo only when the file is executed directly; it does not run the demo just because another file imports that module.

## Exception Handling Test Cases
| Case | Input | Expected result |
| --- | --- | --- |
| Valid | obtained=80, total=100 | 80.00% |
| Negative obtained | obtained=-5, total=100 | ValueError |
| Obtained exceeds total | obtained=120, total=100 | ValueError |
| Zero total | obtained=80, total=0 | ValueError |
| Non-numeric input | e.g. `abc` | ValueError caught and displayed |

## Debugging Notes
The original average loop assigned `total = score` each time instead of adding to the running total. For `[60, 70, 80, 90]`, the faulty function returned `90 / 4 = 22.5`; the correct average is `75.0`. The fix is `total += score`. The original classifier checked `average >= 50` before `average >= 85`, making the Excellent branch unreachable. Check the higher threshold first.

The faulty code is kept in `task05_debugging.py` so its behavior can be compared with the corrected version. I used printed outputs and manual tracing to locate the errors.

## Design Decisions
- Functions are useful for small operations that do not need to store persistent state.
- A class is appropriate when scores and operations on those scores belong together.
- `main.py` coordinates the workflow, while preprocessing and analysis modules contain focused logic.
- Empty score collections return `None` for averages and extrema where appropriate.

## What I Found Difficult
Understanding why the original debugging challenge produced incorrect results and how module imports work.

## What I Learned
Functions reduce repetition, modules organize reusable code, exceptions help handle predictable invalid inputs, and classes group state with related behavior.

## AI Engineering Relevance
AI workflows often clean data, calculate metrics, and evaluate predictions. Modular functions, deliberate validation, debugging, and clear class design help these workflows stay testable and maintainable.

## AI Usage Log
### Tool Used
ChatGPT

### What I Asked
Help organize and implement the Week 3 lab tasks.

### What I Used
A structured starting implementation for the exercises and optional classifier.

### What I Verified or Changed Myself
Run every script, check the results against the lab requirements, and revise any part you cannot explain before submission.

## How to Run
Run individual scripts from this folder:

```powershell
python task01_functions.py
python task02_scope.py
python task04_exceptions.py
python task05_debugging.py
python task06_oop.py
python optional_threshold_classifier.py
```

Run the module demo from its folder:

```powershell
cd task03_modules
python score_utils.py
python main.py
```

Run the refactored program from its folder:

```powershell
cd ..\task07_refactor
python main.py
```

## Submission Checklist
- [ ] Run all scripts and review their output.
- [ ] Test valid, empty, boundary, and invalid inputs.
- [ ] Understand each function, module, and class.
- [ ] Confirm the Week 3 README is complete.
- [ ] Commit meaningful progress and push to GitHub.
