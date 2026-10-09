"""Task 6: ScoreAnalyzer class."""


class ScoreAnalyzer:
    def __init__(self, scores):
        self.scores = list(scores)

    def clean(self):
        """Keep only numeric scores between 0 and 100 inclusive."""
        self.scores = [
            score for score in self.scores
            if isinstance(score, (int, float)) and 0 <= score <= 100
        ]
        return self.scores

    def average(self):
        if not self.scores:
            return None
        return sum(self.scores) / len(self.scores)

    def count_above(self, threshold):
        return sum(score >= threshold for score in self.scores)

    def summary(self):
        if not self.scores:
            return {
                "count": 0,
                "average": None,
                "highest": None,
                "lowest": None,
            }
        return {
            "count": len(self.scores),
            "average": self.average(),
            "highest": max(self.scores),
            "lowest": min(self.scores),
        }


if __name__ == "__main__":
    raw_scores = [78, -5, 110, 67, 90, 88]
    analyzer = ScoreAnalyzer(raw_scores)
    print("Cleaned:", analyzer.clean())
    print("Average:", analyzer.average())
    print("Count >= 70:", analyzer.count_above(70))
    print("Summary:", analyzer.summary())

    empty_analyzer = ScoreAnalyzer([])
    print("Empty summary:", empty_analyzer.summary())
