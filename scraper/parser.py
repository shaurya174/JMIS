from config.settings import Settings


class JobParser:

    def __init__(self, raw_jobs):
        self.settings = Settings()
        self.raw_jobs = raw_jobs

    def extract_jobs(self):
        jobs_list = []

        for job in self.raw_jobs:

            try:
                title = job.get("title", "N/A")

                company = job.get("company", {}).get("display_name", "N/A")

                # Salary Information
                salary_min = job.get("salary_min")
                salary_max = job.get("salary_max")

                if salary_min is not None and salary_max is not None:
                    salary_avg = (salary_min + salary_max) / 2
                else:
                    salary_avg = None

                location = job.get("location", {}).get("display_name", "N/A")

                date_posted = job.get("created", "N/A")

                job_desc = job.get("description", "")

                job_link = job.get("redirect_url", "N/A")

                # Extract skills using keyword matching
                skills_required = []
                for skill in self.settings.SKILL_KEYWORDS:
                    if skill.lower() in job_desc.lower():
                        skills_required.append(skill)

                # Contract type
                job_type = job.get("contract_type", "N/A")

                job_data = {
                    "title": title,
                    "company": company,
                    "location": location,
                    "date_posted": date_posted,
                    "skills_required": skills_required,
                    "job_type": job_type,
                    "salary_min": salary_min,
                    "salary_max": salary_max,
                    "salary_avg": salary_avg,
                    "job_desc": job_desc,
                    "link": job_link
                }

                jobs_list.append(job_data)

            except Exception as e:
                print("Parsing error:", e)
                continue

        print(f"Total jobs processed: {len(jobs_list)}")
        return jobs_list