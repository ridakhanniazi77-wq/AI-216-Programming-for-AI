"""Optional challenge: per-label confidence report, two grouping approaches."""

from collections import Counter, defaultdict

cleaned_records = [
    {"id": 1, "label": "spam", "confidence": 0.94},
    {"id": 2, "label": "ham", "confidence": 0.72},
    {"id": 3, "label": "promotion", "confidence": 0.41},
    {"id": 4, "label": "spam", "confidence": 0.89},
    {"id": 5, "label": "ham", "confidence": 0.97},
    {"id": 6, "label": "promotion", "confidence": 0.83},
    {"id": 7, "label": "ham", "confidence": 0.58},
    {"id": 8, "label": "spam", "confidence": 0.91},
    {"id": 10, "label": "unknown", "confidence": 0.86},
    {"id": 11, "label": "ham", "confidence": 0.66},
]


def print_report(grouped_confidences):
    print("label       count  avg_conf  max_conf")
    for label in sorted(grouped_confidences):
        values = grouped_confidences[label]
        average = sum(values) / len(values)
        print(f"{label:<11} {len(values):>5}  {average:>8.3f}  {max(values):>8.2f}")


plain_groups = {}
for record in cleaned_records:
    label = record["label"]
    if label not in plain_groups:
        plain_groups[label] = []
    plain_groups[label].append(record["confidence"])

print("Using a plain dictionary:")
print_report(plain_groups)

default_groups = defaultdict(list)
for record in cleaned_records:
    default_groups[record["label"]].append(record["confidence"])

print("\\nUsing defaultdict(list):")
print_report(default_groups)

most_common_label, count = Counter(
    record["label"] for record in cleaned_records
).most_common(1)[0]
print(f"Most common label: {most_common_label} ({count})")
