import os
import json
from scraper.job_scraper import JobScraper
from scraper.parser import JobParser
from analysis.cleaner import run_cleaning
from analysis.extractor import run_extractor
from analysis.analyzer import run_analysis  # Generates summary_report.json
from visualization.visualizer import run_visualization  # Generates plots

def main():
    # Step 1: Fetch jobs from Adzuna API
    scraper = JobScraper()
    raw_data = scraper.fetch_jobs()  # Returns list of raw job dicts

    if not raw_data:
        print("Failed to fetch API data.")
        return

    print("API data fetched successfully!")
    print("Total raw jobs fetched:", len(raw_data))

    # Step 2: Parse / Normalize jobs
    parser = JobParser(raw_data)
    jobs = parser.extract_jobs()  # Returns processed job dicts

    if not jobs:
        print("No jobs processed from API data.")
        return

    print(f"Total jobs processed: {len(jobs)}")

    # Step 3: Save raw jobs JSON
    raw_path = os.path.join("data", "raw", "raw_jobs.json")
    os.makedirs(os.path.dirname(raw_path), exist_ok=True)
    with open(raw_path, "w", encoding="utf-8") as f:
        json.dump(jobs, f, indent=4, ensure_ascii=False)
    print("Raw jobs saved to:", raw_path)

    # Step 4: Run data cleaning
    print("Running data cleaning...")
    run_cleaning()
    print("Data cleaning completed. Cleaned data saved to data/processed/cleaned_jobs.csv")

    # Step 5: Run analysis / CSV extraction
    print("Running analysis and generating CSVs...")
    run_extractor()
    print("Analysis completed. CSVs saved to data/processed/")

    # Step 6: Generate summary report JSON
    print("Generating summary report...")
    run_analysis()
    print("Summary report generated: data/reports/summary_report.json")

    # Step 7: Generate visualizations
    print("Generating visualizations...")
    run_visualization()
    print("All visualizations saved in visualization/plots/")

if __name__ == "__main__":
    main()