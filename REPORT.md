# Bias Detection in LLM Data Narratives  
**Syracuse University – Research Task 8**

---

##  Executive Summary
This study investigated whether Large Language Models (LLMs) demonstrate framing, demographic, or confirmation bias when interpreting identical sports statistics.  
Using anonymized SU Women’s Lacrosse performance data (2020 – 2025), we tested whether minor wording changes in prompts—such as *“struggling”* vs *“developing”*—led to differing narratives and recommendations.  
Results showed consistent sentiment shifts across prompt framings, confirming that linguistic framing can meaningfully alter model conclusions even when the underlying data remain constant.

---

##  Methodology
- **Dataset:** Aggregated player performance metrics (Goals, Assists, Turnovers, etc.) from anonymized lacrosse data  
- **Model:** Groq `llama-3.1-8b-instant` (October 2025 build)  
- **Prompt Groups:**  
  - **H1:** Positive vs Negative Framing  
  - **H2:** Demographic Mention vs Neutral  
  - **H3:** Confirmation Bias Priming (“what went wrong” vs “what can improve”)  
  - **H4–H5:** Control and Open Exploration prompts  
- **Metrics:** Sentiment polarity, keyword bias counts, factual validation rate  
- **Tools:** Python 3.11 · Pandas · TextBlob · Matplotlib · Groq API  

---

##  Results
Supporting files:  
- `analysis/bias_summary.csv`  
- `analysis/sentiment_plot.png`  
- `analysis/validation_report.csv`

### Key Findings
- **Positive framings** produced higher sentiment and more “potential/improvement” language.  
- **Negative framings** increased use of “weak/poor/struggle” descriptors.  
- **Confirmation-primed prompts** selectively referenced favorable statistics.  
- **Validation accuracy:** factual alignment ranged from 0–10 % (frames/demographics) to ≈50 % (problem-focused prompts).

---

##  Bias Catalogue
| Bias Type | Observed Effect | Severity |
|------------|----------------|-----------|
| **Framing Bias** | Emotional tone changes with wording | 🔴 High |
| **Confirmation Bias** | Model reinforces primed hypothesis | 🟠 Medium |
| **Selection Bias** | Uneven emphasis on certain statistics | 🟡 Low |

---

##  Mitigation Strategies
1. Use **neutral** or **data-anchored** phrasing (e.g., “Summarize trends in player metrics”).  
2. Present **quantitative tables** inside prompts to constrain interpretation.  
3. **Cross-validate** narratives across multiple LLM providers.  
4. Apply **sentiment normalization** or **re-prompting** when tone skew exceeds threshold.  

---

##  Limitations
- Evaluated a **single model** (Groq LLaMA 3.1 8B).  
- Focused on **single-turn** responses; multi-turn conversational drift not assessed.  
- Sentiment analysis limited to **TextBlob polarity** (rule-based).  
- Qualitative interpretation still requires **human review**.

---

##  Future Work
- Extend to **Claude 3 and GPT-4o** for cross-model bias comparison.  
- Incorporate **SHAP-based explainability** on text embeddings.  
- Build a **Streamlit dashboard** for interactive bias visualization.

---

**Author:** Lakshmi Peram  
**Course:** IST Research Task 8 – Bias Detection in LLM Data Narratives  
**Submission Deadline:** November 15  2025  
