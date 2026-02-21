import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from analysis.analyzer import run_analysis
import os
import json

def test_summary_json():
    run_analysis()
    report_path = os.path.join("data", "reports", "summary_report.json")
    assert os.path.exists(report_path)
    with open(report_path) as f:
        data = json.load(f)
    assert "total_jobs" in data
    assert "top_skills" in data
    assert "top_locations" in data
    