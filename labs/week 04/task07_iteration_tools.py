"""Task 7: enumerate() and zip()."""

experiments = [0.81, 0.86, 0.79, 0.91]
for number, score in enumerate(experiments, start=1):
    print(f"Experiment {number}: {score}")

predictions = [True, False, True, True]
actual = [True, False, False, True]
correct_count = 0

for predicted, actual_value in zip(predictions, actual):
    is_correct = predicted == actual_value
    correct_count += is_correct
    print(f"Predicted: {predicted} | Actual: {actual_value} | Correct: {is_correct}")

if actual:
    accuracy = correct_count / len(actual)
    print(f"Correct predictions: {correct_count}")
    print(f"Accuracy: {accuracy:.2f}")
else:
    print("Accuracy: None (no actual values)")
