"""Task 1: Working with lists."""

MIN_ACCEPTABLE_SCORE = 0.85

accuracies = [0.82, 0.91, 0.87, 0.78, 0.93, 0.85]

print(f"First: {accuracies[0]}")
print(f"Last: {accuracies[-1]}")
print(f"Middle four: {accuracies[1:5]}")

accuracies.append(0.89)
accuracies.extend([0.84, 0.90])

old_score_index = accuracies.index(0.78)
accuracies[old_score_index] = 0.80

print(f"Updated: {accuracies}")
print(f"Scores >= {MIN_ACCEPTABLE_SCORE}: {sum(score >= MIN_ACCEPTABLE_SCORE for score in accuracies)}")
print(f"Highest: {max(accuracies)}")
print(f"Lowest: {min(accuracies)}")
print(f"Sorted (high to low): {sorted(accuracies, reverse=True)}")
print(f"Original order kept: {accuracies}")

# append([0.84, 0.90]) would add one nested list as a single item.
# extend([0.84, 0.90]) adds each score as a separate list element.
