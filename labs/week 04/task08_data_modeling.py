"""Task 8: Choose data structures that match the data."""

# A: List preserves the order in which model names were evaluated.
evaluated_models = ["baseline_cnn", "resnet50", "vit_base"]

# B: Tuple represents fixed image dimensions.
image_size = (224, 224)

# C: Dictionary gives meaningful names to model configuration fields.
model_config = {
    "name": "spam_classifier",
    "threshold": 0.80,
    "version": 2,
    "debug": False,
}

# D: Set stores unique labels.
unique_labels = {"spam", "ham", "promotion"}

# E: A list of dictionaries stores multiple structured prediction records.
prediction_records = [
    {"id": 1, "label": "spam", "confidence": 0.94},
    {"id": 2, "label": "ham", "confidence": 0.72},
]

# F: Set difference finds labels received from an external source that
# are not part of the allowed label collection.
allowed_labels = {"spam", "ham", "promotion"}
received_labels = {"spam", "unknown", "ham"}
unexpected_labels = received_labels - allowed_labels

print("Evaluated models:", evaluated_models)
print("Image size:", image_size)
print("Model config:", model_config)
print("Unique labels:", sorted(unique_labels))
print("Prediction records:", prediction_records)
print("Unexpected labels:", sorted(unexpected_labels))
