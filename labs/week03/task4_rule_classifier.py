class RuleBasedClassifier:
    def __init__(self, threshold):
        self.threshold = threshold

    def classify(self, value):
        return value >= self.threshold

    def classify_list(self, values):
        results = []

        for value in values:
            results.append(self.classify(value))

        return results


threshold = 60
values = [45, 72, 88, 30, 65]

classifier = RuleBasedClassifier(threshold)

print("Threshold:", threshold)
print("Values:", values)

for value in values:
    print(value, "->", classifier.classify(value))

print("Classification results:", classifier.classify_list(values))