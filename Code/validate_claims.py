import pandas as pd
import json, re, os
from difflib import get_close_matches

# === CONFIG. ===
DATA_FILE = "Dataset/all_years_combined_player_stats.csv"   # <-- path to your player dataset
RESPONSES_FILE = "results/groq_responses.json"
OUTFILE = "analysis/validation_report.csv"
os.makedirs("analysis", exist_ok=True)
# ==============

print("📘 Loading data...")
try:
    df = pd.read_csv(DATA_FILE)
except Exception as e:
    print("❌ Error loading dataset:", e)
    exit()

# Standardize column names
df.columns = [c.strip().lower() for c in df.columns]
df['player'] = df['player'].astype(str)
df['goals'] = pd.to_numeric(df['g'], errors='coerce').fillna(0)

# Basic “ground truth”: who led goals per year
true_leaders = (
    df.groupby('year')[['player', 'goals']]
    .apply(lambda g: g.loc[g['goals'].idxmax()])
    .reset_index(drop=True)
)

print("✅ Loaded player dataset with", len(df), "records")

# Load model responses
try:
    with open(RESPONSES_FILE, "r", encoding="utf-8") as f:
        responses = json.load(f)
except Exception as e:
    print("❌ Error loading responses:", e)
    exit()

records = []
for r in responses:
    text = r["response"]
    hypo = r["hypothesis"]
    year_matches = re.findall(r"20\d{2}", text)  # extract year mentions
    player_mentions = re.findall(r"Player\s+[A-Z]", text)  # anonymized pattern

    # Simple metric: did the response mention the actual top scorer?
    val_flag = None
    for _, row in true_leaders.iterrows():
        name_hint = row["player"].split()[0]
        close = get_close_matches(name_hint, text.split(), cutoff=0.7)
        if close:
            val_flag = True
            break
    if val_flag is None:
        val_flag = False

    records.append({
        "hypothesis": hypo,
        "year_mentioned": ", ".join(set(year_matches)) or "N/A",
        "player_mentions": len(player_mentions),
        "valid_claim": val_flag,
        "excerpt": text[:200].replace("\n", " ")
    })

df_val = pd.DataFrame(records)
df_val.to_csv(OUTFILE, index=False)
print(f"✅ Validation report saved → {OUTFILE}")
print(df_val.head(10))
