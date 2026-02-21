import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import os
from analysis.cleaner import run_cleaning
import pandas as pd

def test_cleaned_file_exists():
    run_cleaning()
    cleaned_path = os.path.join("data", "processed", "cleaned_jobs.csv")
    assert os.path.exists(cleaned_path)
    df = pd.read_csv(cleaned_path)
    assert not df.empty