import os, json, datetime
from groq import Groq

# ===== CONFIG. =====
MODEL = "llama-3.1-8b-instant"
NUM_SAMPLES = 2
TEMPERATURE = 0.7
OUTFILE = "results/groq_responses.json"
# ==================

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def load_prompts(path="prompts/prompts.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def query_groq(prompt):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=TEMPERATURE,
    )
    return response.choices[0].message.content.strip()

def run_experiments():
    os.makedirs("results", exist_ok=True)
    prompts = load_prompts()
    results = []

    for p in prompts:
        print(f"\n🚀 Running {p['hypothesis']} ...")
        for i in range(NUM_SAMPLES):
            try:
                result = query_groq(p["prompt"])
                results.append({
                    "timestamp": datetime.datetime.now().isoformat(),
                    "hypothesis": p["hypothesis"],
                    "prompt": p["prompt"],
                    "response": result
                })
                print(f"✅ Saved sample {i+1} for {p['hypothesis']}")
            except Exception as e:
                print(f"❌ Error: {e}")

    with open(OUTFILE, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"\n🎯 Completed! Saved {len(results)} responses → {OUTFILE}")

if __name__ == "__main__":
    run_experiments()
