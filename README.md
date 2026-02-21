# 🎯 Job Market Insights System (JMIS)

![JMIS Banner](https://img.shields.io/badge/Job-Market-Insights-blue?style=for-the-badge\&logo=python)

---

## 🚀 Project Overview

**JMIS** is a professional, end-to-end **job data analytics system** designed to:

1. Fetch job postings from the Adzuna API
2. Clean and normalize raw job data
3. Perform detailed analysis across **skills, locations, companies, months, and weekly trends**
4. Generate CSVs, reports, and visualizations for quick insights

This project is structured like a **real-world data analytics pipeline**, ideal for portfolio or professional demos.

---

## 🗂 Project Structure

```
JMIS/
│
├─ analysis/                # Data cleaning, extraction, and analysis scripts
│   ├─ cleaner.py           # Cleans raw job data
│   ├─ extractor.py         # Extracts multiple analytical CSVs
│   ├─ analyzer.py          # Generates summary JSON report
│   └─ __init__.py
│
├─ config/                  # Configuration
│   └─ settings.py          # Skill keywords and other settings
│
├─ data/
│   ├─ raw/                 # Raw JSON from Adzuna API (sample included)
│   │   └─ raw_jobs.json
│   ├─ processed/           # CSV outputs from extraction
│   └─ reports/             # Summary JSON
│
├─ notebooks/               # Jupyter notebooks for exploration
├─ scraper/                 # Web scraping / API fetching logic
│   ├─ job_scraper.py
│   ├─ parser.py
│   └─ __init__.py
├─ tests/                   # Pytest unit tests
├─ main.py                  # Run the full pipeline
├─ requirements.txt         # Python dependencies
└─ README.md
```

---

## ⚡ Features

* **Fetch Jobs**: Pulls up to 1000 job postings from Adzuna API
* **Clean Data**: Standardizes text, parses skills, separates city/state, removes redundant columns
* **Analyze Data**:

  * Skill frequency (`skill_frequency.csv`)
  * Location frequency (`location_frequency.csv`)
  * Company frequency (`company_frequency.csv`)
  * Jobs per month (`jobs_per_month.csv`)
  * Weekly skill trends (`weekly_skill_trends.csv`)
* **Generate Reports**: Consolidated JSON summary (`summary_report.json`)

---

## 📊 Visualizations

Plots are saved in `visualization/plots/`:

1. **Most In-Demand Skills** – Bar chart
   ![Skills Plot](visualization/plots/skills.png)
2. **Pareto Analysis: Job Postings by State** – Bar + cumulative line chart
   ![Location Plot](visualization/plots/locations.png)
3. **Top 15 Companies by Job Postings** – Horizontal bar chart
   ![Companies Plot](visualization/plots/companies.png)
4. **Weekly Job Demand Trends** – Line chart of top 5 skills
   ![Weekly Trends Plot](visualization/plots/weekly_trends.png)

> ✅ Sample data is already included, so you can run the full pipeline immediately.

---

## 🛠 Installation

```bash
git clone https://github.com/yourusername/JMIS.git
cd JMIS

# Create and activate virtual environment
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## 🏃 How to Run

1. **Run tests first**:

```bash
pytest tests/
```

2. **Run the full pipeline**:

```bash
python main.py
```

**Pipeline Steps**:

| Step | Description                     |
| ---- | ------------------------------- |
| 1    | Fetch jobs from Adzuna API      |
| 2    | Parse and normalize raw jobs    |
| 3    | Save raw jobs JSON              |
| 4    | Clean data (`cleaned_jobs.csv`) |
| 5    | Extract analytical CSVs         |
| 6    | Generate `summary_report.json`  |

---

## 📝 CSV Outputs

| File                      | Description                  |
| ------------------------- | ---------------------------- |
| `skill_frequency.csv`     | Skill counts across all jobs |
| `location_frequency.csv`  | Jobs per state               |
| `company_frequency.csv`   | Jobs per company             |
| `jobs_per_month.csv`      | Jobs grouped by month        |
| `weekly_skill_trends.csv` | Weekly trends of top skills  |

---

## 📄 Summary Report JSON

Example structure:

```json
{
  "total_jobs": 1000,
  "top_skills": [{"Skill": "python", "Count": 400}, ...],
  "top_locations": [{"Location": "Delhi", "Count": 120}, ...],
  "top_companies": [{"Company": "TCS", "Count": 75}, ...],
  "jobs_per_month": [{"Month": "January", "Count": 85}, ...],
  "weekly_top_skills": [{"Week": "2026-02-01", "TopSkill": "python"}, ...]
}
```

---

## ⚡ Future Enhancements

* Logging for pipeline steps
* ML models to predict skill demand
* Interactive dashboards
* Support for additional job APIs

---

## 🧩 Tech Stack

* Python 3.11
* Pandas, NumPy
* Matplotlib & Seaborn (visualizations)
* Pytest (unit testing)
* Adzuna Jobs API

---

## 💡 Notes

* Activate your **virtual environment** before running.
* Modular architecture allows swapping API sources or adding new analysis easily.
* All outputs are stored in `data/processed/` (CSVs) and `data/reports/` (summary JSON).

---

## 🎉 Credits

Developed with ❤️ by **Shaurya Mittal**

> “Professional, modular, production-ready — the ultimate real-world data analytics showcase!”
