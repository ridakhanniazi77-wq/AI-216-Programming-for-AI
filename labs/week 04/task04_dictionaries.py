"""Task 4: Dictionaries for structured model records."""

model = {
    "name": "spam_classifier",
    "version": 2,
    "accuracy": 0.92,
    "threshold": 0.80,
    "status": "evaluated",
}

print("Model name:", model["name"])
model["accuracy"] = 0.94
model["owner"] = "AI-216 Team"
print("Description:", model.get("description", "No description provided"))

model["metrics"] = {
    "accuracy": 0.94,
    "precision": 0.91,
    "recall": 0.89,
}

print("Precision:", model["metrics"]["precision"])
print("Recall:", model["metrics"]["recall"])

print("All model fields:")
for key, value in model.items():
    print(f"{key}: {value}")
