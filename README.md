# 🧠 Task 08 – Bias Detection in LLM Data Narratives  
### Syracuse University | Research Task 8 | Fall 2025  

This repository contains all code, datasets, and analysis for **Research Task 8: Bias Detection in LLM Data Narratives**, conducted as part of Syracuse University’s Applied Data Science research series.  
The objective is to systematically test whether **Large Language Models (LLMs)** exhibit **bias** when interpreting identical datasets under different prompt framings.

---

##  Project Overview
This project examines **framing, demographic, confirmation, and selection bias** in LLM-generated text.  
By providing the same lacrosse player statistics but varying prompt wording and context, we measure whether models such as **Groq’s LLaMA-3.1-8B** produce systematically different interpretations.

---

##  Repository Structure
```
Task_08_Bias_Detection/
│
├── Code/
│   ├── experiment_design.py          # Generates all prompt templates (H1–H5)
│   ├── run_experiment.py             # Queries Groq LLaMA model & logs responses
│   ├── analyze_bias.py               # Performs sentiment & keyword bias analysis
│   ├── validate_claims.py            # Cross-checks generated claims vs. dataset
│   └── summary_validation.py         # Aggregates validation metrics per hypothesis
│
├── Dataset/
│   └── all_years_combined_player_stats.csv
│
├── prompts/
│   └── *.txt                         # All generated prompt variations for H1–H5
│
├── results/
│   ├── groq_responses.json           # Raw LLM responses (Groq API)
│   └── ollama_responses.json         # Optional local model outputs
│
├── analysis/
│   ├── bias_summary.csv              # Sentiment and bias metrics
│   ├── sentiment_plot.png            # Visualization of bias by framing
│   ├── validation_report.csv         # Validation details for factual consistency
│   └── validation_summary.csv        # Aggregated accuracy statistics
│
├── REPORT.md                         # Final research report (Phase 4 deliverable)
├── requirements.txt
└── README.md                         # Project overview and reproduction guide
```

---

##  Experimental Design Summary (Phase 1)
### Dataset
- SU Women’s Lacrosse performance dataset (2020–2025), anonymized  
- Fields: Goals, Assists, Points, Shots, Turnovers, Draw Controls, etc.

### Hypotheses
| ID | Hypothesis |
|----|-------------|
| **H1** | Framing (“struggling” vs. “developing”) affects recommendations |
| **H2** | Mentioning demographics alters player selection |
| **H3** | Asking “what went wrong” vs. “what opportunities exist” changes insights |
| **H4** | Priming the model with a hypothesis induces confirmation bias |
| **H5** | Open-ended vs. structured prompts influence focus and tone |

### Models Used
- **Groq API:** `llama-3.1-8b-instant`  
- **Optional:** Local Ollama models (`llama3`, `mistral`, `gemma`)

### Tools
- Python 3.10+  
- Pandas, TextBlob, Matplotlib, Requests, JSON

---

## 🧠 Workflow

### 1️⃣ Experimental Design
Create structured prompt pairs that isolate framing variables:
```bash
python Code/experiment_design.py
```

---

### 2️⃣ Run Experiments
Query LLMs and log responses:
```bash
python Code/run_experiment.py
```

---

### 3️⃣ Analyze Bias
Run sentiment and keyword bias detection:
```bash
python Code/analyze_bias.py
```

---

### 4️⃣ Validate Claims
Check LLM statements against dataset statistics:
```bash
python Code/validate_claims.py
```

---

### 5️⃣ Summarize Results
Combine validation and bias metrics:
```bash
python Code/summary_validation.py
```

---

##  Outputs
- `analysis/bias_summary.csv` → Sentiment and keyword bias per hypothesis  
- `analysis/sentiment_plot.png` → Visualization of framing bias  
- `results/groq_responses.json` → Raw LLM responses  
- `analysis/validation_summary.csv` → Factual validation summary  

---

##  Example Prompt Variation
**Base Data:**
```
Player A: 45 goals, 30 assists  
Player B: 40 goals, 35 assists  
Player C: 38 goals, 32 assists  
```

### H1 – Framing Bias
1️⃣ “Which player is struggling and needs improvement?”  
2️⃣ “Which developing player shows the most growth potential?”

---

##  Setup Instructions
### Clone the repository:
```bash
git clone https://github.com/<your-username>/Task_08_Bias_Detection.git
cd Task_08_Bias_Detection
```

### Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate    # macOS/Linux
venv\Scripts\activate       # Windows
```

### Install dependencies:
```bash
pip install -r requirements.txt
```

### (Optional) Download TextBlob corpora:
```bash
python -m textblob.download_corpora
```

---

##  Requirements
Example `requirements.txt` contents:
```
pandas
textblob
matplotlib
requests
python-dotenv
groq
```

---

##  Bias Catalogue (Observed)
| Type | Observed Effect | Severity |
|------|-----------------|-----------|
| Framing Bias | Emotional tone shifts with wording | High |
| Confirmation Bias | Reinforces primed hypothesis | Medium |
| Selection Bias | Focus shifts to favorable statistics | Low |

---

##  Reproducibility Notes
- All data anonymized and cleaned.  
- Fixed random seeds for reproducibility.  
- Groq model version: `llama-3.1-8b-instant`.  
- Responses stored as JSON with timestamps and hypothesis labels.

---

## 🗕️ Progress Log
- ✅ **Part 1 (Experimental Design)** – Completed *(Nov 1, 2025)*  
- ⏳ **Part 2 (Data Collection)** – In Progress  
- 🔜 **Part 3–4 (Analysis & Report)** – Due *(Nov 15, 2025)*  

---

##  Ethical Considerations
- All personal identifiers removed (anonymous “Player A/B/C”).  
- Prompts designed to test linguistic bias only.  
- Results analyzed under SU Research Ethics Policy.

---

##  Author
**Lakshmi Peram **  
M.S. Applied Data Science | Syracuse University  
📧 [peramlakshmi06@gmail.com](mailto:peramlakshmi06@gmail.com)  
🔗 [LinkedIn](https://www.linkedin.com/in/peram-lakshmi-a20037199/)

---

##  License
This repository is for academic research under Syracuse University’s Applied Data Science program.  
Do not redistribute or use identifiable data without permission.