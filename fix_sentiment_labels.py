import json

with open("data/sentiment_results.json", "r") as f:
    data = json.load(f)

for post in data:
    label = post["sentiment"]["label"]
    if label not in {"POSITIVE", "NEUTRAL", "NEGATIVE"}:
        print(f"Fixing label: {label} -> NEUTRAL")
        post["sentiment"]["label"] = "NEUTRAL"

with open("data/sentiment_results.json", "w") as f:
    json.dump(data, f, indent=2)

print("✅ Replaced unknown or invalid sentiment labels with NEUTRAL.")