# Task 4: Rule-Based Classifier


class RuleBasedClassifier:
    """Classify values using a threshold."""

    def __init__(self, threshold):
        self.threshold = threshold

    def classify(self, value):
        """Return True if the value meets the threshold."""
        return value >= self.threshold

    def classify_list(self, values):
        """Classify a list of values."""
        return [self.classify(value) for value in values]


threshold = 60
values = [45, 72, 88, 30, 65]

classifier = RuleBasedClassifier(threshold)

print("Rule-Based Classifier")
print("---------------------")
print(f"Threshold: {threshold}")
print(f"Values: {values}")
print(f"Classifications: {classifier.classify_list(values)}")