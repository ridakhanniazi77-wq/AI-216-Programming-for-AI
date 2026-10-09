"""Task 2: Aliasing, shallow copying, and deep copying."""

import copy

print("Part A: Aliasing")
original_scores = [70, 80, 90]
processed_scores = original_scores
processed_scores.append(100)
print("Original:", original_scores)
print("Processed:", processed_scores)
print("Both names refer to the same list.\n")

print("Part B: Shallow copy of a flat list")
original_scores = [70, 80, 90]
processed_scores = original_scores.copy()
processed_scores.append(100)
print("Original:", original_scores)
print("Processed:", processed_scores)

print("\nPart C: Shallow copy of nested dictionaries")
raw_predictions = [
    {"id": 1, "label": "Spam"},
    {"id": 2, "label": "HAM"},
]
shallow_predictions = raw_predictions.copy()
shallow_predictions[0]["label"] = "spam"
print("Raw after shallow copy edit:", raw_predictions)

print("\nPart C: Deep copy")
raw_predictions = [
    {"id": 1, "label": "Spam"},
    {"id": 2, "label": "HAM"},
]
deep_predictions = copy.deepcopy(raw_predictions)
deep_predictions[0]["label"] = "spam"
print("Raw after deep copy edit:", raw_predictions)
print("Deep copy:", deep_predictions)
