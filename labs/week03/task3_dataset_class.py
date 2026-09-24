# Task 3: Simple Dataset Class


class Dataset:
    """Represent a small numeric dataset."""

    def __init__(self, values):
        self.values = values

    def count(self):
        """Return the number of data points."""
        return len(self.values)

    def average(self):
        """Calculate and return the average."""
        if self.count() == 0:
            return 0

        return sum(self.values) / self.count()


data_values = [12, 18, 25, 30, 22, 27]

dataset = Dataset(data_values)

print("Simple Dataset")
print("--------------")
print(f"Data: {dataset.values}")
print(f"Number of data points: {dataset.count()}")
print(f"Average: {dataset.average():.2f}")