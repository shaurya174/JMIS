import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scraper.parser import JobParser

def test_extract_jobs_structure():
    sample_job = [{
        "title": "Developer",
        "company": {"display_name": "TestCorp"},
        "location": {"display_name": "Test City"},
        "description": "Python, AI",
        "created": "2026-02-21T10:00:00Z",
        "contract_type": "Full-time",
        "redirect_url": "http://example.com"
    }]
    parser = JobParser(sample_job)
    jobs = parser.extract_jobs()
    assert isinstance(jobs, list)
    job = jobs[0]
    required_keys = [
        "title","company","location","date_posted",
        "skills_required","job_type","link"
    ]
    for key in required_keys:
        assert key in job