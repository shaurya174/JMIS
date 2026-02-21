import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from analysis.extractor import run_extractor
import os

def test_extracted_csvs_exist():
    run_extractor()
    processed_dir = os.path.join("data", "processed")
    for fname in ["skill_frequency.csv", "location_frequency.csv", "company_frequency.csv", "jobs_per_month.csv", "weekly_skill_trends.csv"]:
        assert os.path.exists(os.path.join(processed_dir, fname))