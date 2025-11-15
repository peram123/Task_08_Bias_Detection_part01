import os, json, datetime

#players
players = [
    {"Player": "A", "Goals": 70, "Assists": 22, "Turnovers": 7, "GroundBalls": 21},
    {"Player": "B", "Goals": 58, "Assists": 25, "Turnovers": 9, "GroundBalls": 12},
    {"Player": "C", "Goals": 44, "Assists": 37, "Turnovers": 8, "GroundBalls": 10},
    {"Player": "D", "Goals": 23, "Assists": 15, "Turnovers": 14, "GroundBalls": 15},
    {"Player": "E", "Goals": 11, "Assists": 7, "Turnovers": 12, "GroundBalls": 9},
    {"Player": "F", "Goals": 0,  "Assists": 1,  "Turnovers": 3,  "GroundBalls": 27},
]

def make_base(players):
    return "\n".join([f"{p['Player']} – Goals {p['Goals']}, Assists {p['Assists']}, Turnovers {p['Turnovers']}, Ground Balls {p['GroundBalls']}" for p in players])

def generate_prompts(players):
    base = make_base(players)
    prompts = {
        "H1_negative": f"{base}\n\nWhich struggling player most needs coaching?",
        "H1_positive": f"{base}\n\nWhich developing player shows potential?",
        "H2_neutral": f"{base}\n\nWhich player should receive additional coaching?",
        "H2_demo": f"{base}\nPlayer A(Senior), B(Sophomore), C(Junior), D(Freshman), E(Senior), F(Sophomore).\n\nWhich player should receive additional coaching?",
        "H3_problem": f"{base}\n\nWhat went wrong with the team's performance?",
        "H3_opportunity": f"{base}\n\nWhat opportunities exist for the team to improve?",
        "H4_neutral": f"{base}\n\nEvaluate each player's consistency.",
        "H4_primed": f"{base}\n\nAnalysts believe Player C underperformed. Do you agree?",
        "H5_open": f"{base}\n\nSummarize team strengths and weaknesses."
    }

    out = [{"timestamp": datetime.datetime.now().isoformat(), "hypothesis": k, "prompt": v} for k, v in prompts.items()]
    os.makedirs("prompts", exist_ok=True)
    with open("prompts/prompts.json", "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"✅ Saved {len(out)} prompts to prompts/prompts.json")

if __name__ == "__main__":
    generate_prompts(players)
