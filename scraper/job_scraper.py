import sys
import os
import requests
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config.settings import Settings


class JobScraper:

    def __init__(self):
        self.settings = Settings()

    def fetch_jobs(self):
        all_jobs = []
        page = 1

        while len(all_jobs) < self.settings.MAX_JOBS:
            url = (
                f"{self.settings.API_BASE_URL}/"
                f"{self.settings.COUNTRY}/search/{page}"
                f"?app_id={self.settings.APP_ID}"
                f"&app_key={self.settings.APP_KEY}"
                f"&results_per_page={self.settings.RESULTS_PER_PAGE}"
                f"&what={self.settings.SEARCH_QUERY}"
            )

            try:
                response = requests.get(url, headers=self.settings.HEADERS, timeout=20)

                if response.status_code != 200:
                    print(f"Failed on page {page}. Status Code: {response.status_code}")
                    break

                data = response.json()

                jobs = data.get("results", [])
                if not jobs:
                    print("No more jobs found.")
                    break

                all_jobs.extend(jobs)
                print(f"Fetched page {page} | Total jobs so far: {len(all_jobs)}")

                page += 1
                time.sleep(2)  # polite delay

            except requests.exceptions.RequestException as e:
                print("Error while fetching API data:", e)
                break

        return all_jobs[:self.settings.MAX_JOBS]