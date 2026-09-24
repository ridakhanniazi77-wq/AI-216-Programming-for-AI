class Dataset:
    def __init__(self, values):
        self.values = values

    def count(self):
        return len(self.values)

    def average(self):
        if len(self.values) == 0:
            return 0

        return sum(self.values) / len(self.values)


data_values = [12, 18, 25, 30, 22, 27]

dataset = Dataset(data_values)

print("Dataset:", dataset.values)
print("Number of data points:", dataset.count())
print("Average:", dataset.average())