"""Task 6: ScoreAnalyzer class."""


class ScoreAnalyzer:
    def __init__(self, scores):
        self.scores = list(scores)

    def clean(self):
        """Keep only numeric scores from 0 through 100, inclusive."""
        self.scores = [
            score for score in self.scores
            if isinstance(score, (int, float))
            and not isinstance(score, bool)
            and 0 <= score <= 100
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


def main():
    raw_scores = [78, -5, 110, 67, 90, 88]
    analyzer = ScoreAnalyzer(raw_scores)
    print("Raw scores:", analyzer.scores)
    print("Cleaned scores:", analyzer.clean())
    print("Average:", analyzer.average())
    print("Scores at least 80:", analyzer.count_above(80))
    print("Summary:", analyzer.summary())


if __name__ == "__main__":
    main()
