import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scraper.job_scraper import JobScraper

def test_fetch_jobs_returns_list():
    scraper = JobScraper()
    jobs = scraper.fetch_jobs()
    assert isinstance(jobs, list)
    if jobs:
        assert isinstance(jobs[0], dict)