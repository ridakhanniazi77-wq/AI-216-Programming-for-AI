"""Optional challenge: a simple threshold-based classifier."""


class ThresholdClassifier:
    def __init__(self, threshold=60):
        self.threshold = threshold

    def predict_one(self, value):
        return value >= self.threshold

    def predict(self, values):
        return [self.predict_one(value) for value in values]

    def accuracy(self, values, true_labels):
        if len(values) != len(true_labels):
            raise ValueError("values and true_labels must have the same length.")
        if not values:
            return None
        predictions = self.predict(values)
        correct = sum(
            prediction == label
            for prediction, label in zip(predictions, true_labels)
        )
        return correct / len(true_labels)


def main():
    model = ThresholdClassifier(threshold=60)
    values = [45, 70, 80, 30]
    labels = [False, True, True, False]
    print("Predictions:", model.predict(values))
    print("Accuracy:", model.accuracy(values, labels))


if __name__ == "__main__":
    main()
