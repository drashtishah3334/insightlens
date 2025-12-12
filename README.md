# InsightLens – AI-Powered CSV Insights (Phase 1)

InsightLens is a lightweight tool that turns any CSV file into an instant, easy-to-read insights report.  
The goal is to help users quickly understand the structure and quality of a dataset without writing code.

In Phase 1, the focus is on building a simple, reliable pipeline that works for *any* CSV.  
Users can upload a file and immediately see:

- a preview of the data  
- basic validation checks (missing values, duplicates, etc.)  
- descriptive statistics for each column  
- correlations or simple patterns  
- an AI-generated summary explaining the dataset in plain English  
- a chat interface to ask follow-up questions (coming soon)

InsightLens is being built step-by-step by a group of MSc Data Science graduates to refresh practical data engineering, analysis, and LLM integration skills.  

Phase 2 will introduce optional domain-specific intelligence (e.g., retail, finance, healthcare), but the foundation in Phase 1 remains fully domain-agnostic.

---

## Why We Are Building This

Most people receive CSV files without knowing where to start:
- What are the important columns?
- Are there problems in the data?
- How do variables relate to each other?
- What patterns or anomalies exist?

Instead of manually running dozens of EDA steps, InsightLens aims to automate the first 15–20 minutes of exploration and provide a simple explanation backed by an AI model.

---

## Current Phase (Phase 1)

- Basic Streamlit interface with CSV upload  
- Data preview  
- Planned next steps:
  - schema inference  
  - validation checks  
  - profiling and correlations  
  - insight generation  
  - LLM narrative summary  
  - Q&A with the dataset  

This README will grow as each component is implemented.

---

## Tech Stack (Phase 1)

- **Python 3.13**
- **Streamlit** (UI)
- **Pandas / Polars** (data handling)
- **NumPy, SciPy** (statistics)
- **HuggingFace / Ollama** (LLM integration – upcoming)
- **Plotly / Altair** (charts – upcoming)
- **GitHub** (collaboration with branch protection + PR reviews)

---

## Future Scope (Phase 2)

- Data Health Score  
- Smart chart recommendations  
- Dataset similarity & drift analysis  
- Synthetic dataset generator  
- Domain-specific playbooks  
- “Explain this chart” via LLM  
- Anomaly + root-cause detection  

---

## Team

- [@drashti-shah](https://github.com/drashtishah3334)
- [@akarshan-jaiswal](https://github.com/Akarshan-Jaiswal)
- [@jagatheesh-pugazhenthi](https://github.com/Jaga-droid)
- Lahja


