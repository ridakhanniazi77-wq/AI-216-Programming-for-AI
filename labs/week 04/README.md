# Lab 04 — Python Data Structures & Clean Code

**Course:** AI-216 Programming for Artificial Intelligence  
**Semester:** Fall 2026  
**Week:** 04

## Concepts Practiced
- Lists, tuples, dictionaries, and sets
- List, dictionary, and set comprehensions
- `enumerate()` and `zip()`
- Sorting and counting records
- Aliasing, shallow copying, and deep copying
- Data structure selection
- Clean-code refactoring and file organization
- Handling incomplete and inconsistent records

## Tasks Completed
1. Lists — `task01_lists.py`
2. Aliasing vs Copying — `task02_copying.py`
3. Tuples — `task03_tuples.py`
4. Dictionaries — `task04_dictionaries.py`
5. Sets — `task05_sets.py`
6. Comprehensions — `task06_comprehensions.py`
7. `enumerate()` and `zip()` — `task07_iteration_tools.py`
8. Data Structure Selection — `task08_data_modeling.py`
9. Prediction Analysis — `task09_clean_code/`
10. Optional per-label confidence report — `optional_label_report.py`

## Data Structure Decisions
- **List:** preserves evaluation order and stores a sequence of prediction records.
- **Tuple:** represents fixed image dimensions and required field names.
- **Dictionary:** maps meaningful field names to values and stores label counts.
- **Set:** stores unique labels and makes union, intersection, and difference explicit.
- **List of dictionaries:** stores multiple prediction records, each with named fields.

## Aliasing vs Copying
In Part A, assigning `processed_scores = original_scores` does not create another list. Both names point to the same object, so an append through either name changes the same list. A shallow `.copy()` fixes this for a flat list because the new list has its own outer container.

For a list containing dictionaries, `.copy()` copies only the outer list. The dictionaries inside are still shared, so changing a nested dictionary also changes what is seen through the original list. `copy.deepcopy()` recursively copies nested objects and protects the original nested data.

Accidental mutation can corrupt preprocessing inputs, make experiment tracking unreliable, or change the data used for model evaluation.

## Hashability
A tuple of hashable values can be used as a dictionary key because it is immutable. A list can change after creation, so it is unhashable and cannot be used as a dictionary key.

## Sets vs Lists for Validation
Set difference directly expresses which received labels are not allowed. Sets also provide typically fast hash-based membership checks, especially for large collections. A list is useful when order or duplicates matter; a set is useful when uniqueness and membership matter.

## Clean-Code Refactoring
The original Task 9 code used unclear names such as `x`, `y`, `z`, and `d`. The refactor uses descriptive names, named constants, and functions with one responsibility. Confidence filtering and label counting both use the complete original list as input, so label counts still include low-confidence records.

Part A can be checked against the original output:
- Selected IDs: `[1, 4, 5, 6]`
- Label counts: `{'spam': 2, 'ham': 3, 'promotion': 2}`
- Unique labels: `['ham', 'promotion', 'spam']`

## Handling Incomplete Records
Task 9 Part B combines both batches, splits complete and incomplete records, and reports the skipped ID(s). A record missing any required field is not analyzed. Labels are stripped and lowercased on copied records, preserving the original input. Unexpected labels are detected with set difference.

The summary dictionary is calculated before printing, keeping computation separate from display.

## Edge Cases Tested
- Empty scores: `summarize_scores([])` returns `None`.
- Empty predictions: `average_confidence([])` returns `None`.
- A confidence exactly equal to the threshold is included because the comparison uses `>=`.
- Duplicate labels are counted, while unique labels are returned as a set.
- A missing confidence field is reported as an incomplete record.
- Label normalization does not change the original `new_batch` data.

## What I Found Difficult
Choosing a data structure for each purpose and understanding how shallow copies behave with nested dictionaries.

## What I Learned
Python data structures communicate the meaning of data. Functions with clear responsibilities make data-processing code easier to test and maintain.

## AI Engineering Relevance
Data structures affect preprocessing, model configuration, prediction storage, label validation, experiment reproducibility, and maintainability. Clear handling of missing or unexpected data helps prevent incorrect analysis.

## AI Usage Log
### Tool Used
ChatGPT

### What I Asked
Help organizing and implementing the Week 4 lab tasks and explaining the required data-structure concepts.

### What I Used
A structured starting implementation for the listed exercises and prediction-analysis workflow.

### What I Verified or Changed Myself
Review each task, run the programs, check the output against the lab instructions, and make any changes needed before submission.

## How to Run
Run individual tasks from this folder, for example:

```powershell
python task01_lists.py
python task02_copying.py
python task03_tuples.py
python task04_dictionaries.py
python task05_sets.py
python task06_comprehensions.py
python task07_iteration_tools.py
python task08_data_modeling.py
python optional_label_report.py
```

Run Task 9 from its own directory so its imports resolve:

```powershell
cd task09_clean_code
python main.py
```

## GitHub Submission Checklist
- [ ] Run all scripts and review their output.
- [ ] Read and understand each function before submitting.
- [ ] Confirm the Task 9 report and raw-label check.
- [ ] Commit meaningful progress.
- [ ] Push the work to GitHub.
