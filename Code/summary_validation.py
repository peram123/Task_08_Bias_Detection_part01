import pandas as pd

df = pd.read_csv("analysis/validation_report.csv")
summary = df.groupby("hypothesis")["valid_claim"].mean().reset_index()
summary["valid_claim_rate_%"] = (summary["valid_claim"] * 100).round(1)
summary.to_csv("analysis/validation_summary.csv", index=False)

print("✅ Saved summary → analysis/validation_summary.csv")
print(summary)
