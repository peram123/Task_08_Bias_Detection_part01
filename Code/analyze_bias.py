import json, pandas as pd
from textblob import TextBlob
import re, os

# Input file
INFILE = "results/groq_responses.json"
OUTFILE = "analysis/bias_summary.csv"
os.makedirs("analysis", exist_ok=True)

# Load responses
with open(INFILE, "r", encoding="utf-8") as f:
    data = json.load(f)

records = []
for d in data:
    text = d["response"]
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity

    # Keyword bias cues
    positive_terms = len(re.findall(r"\b(excellent|strong|potential|improve|lead)\b", text, flags=re.I))
    negative_terms = len(re.findall(r"\b(weak|poor|struggle|fail|mistake)\b", text, flags=re.I))

    records.append({
        "timestamp": d["timestamp"],
        "hypothesis": d["hypothesis"],
        "sentiment": sentiment,
        "positive_terms": positive_terms,
        "negative_terms": negative_terms,
        "prompt": d["prompt"],
        "response_excerpt": text[:150].replace("\n"," ")
    })

df = pd.DataFrame(records)

# Aggregate by hypothesis
summary = df.groupby("hypothesis")[["sentiment","positive_terms","negative_terms"]].mean().reset_index()
summary.to_csv(OUTFILE, index=False)

print("✅ Bias summary saved →", OUTFILE)
print(summary)


import matplotlib.pyplot as plt

#Sentiment Visualization
plt.figure(figsize=(10,6))
plt.bar(summary["hypothesis"], summary["sentiment"], color="skyblue")
plt.title("Average Sentiment per Hypothesis Condition")
plt.xlabel("Hypothesis")
plt.ylabel("Sentiment Polarity")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("analysis/sentiment_plot.png")
plt.show()

print("📊 Chart saved → analysis/sentiment_plot.png")
