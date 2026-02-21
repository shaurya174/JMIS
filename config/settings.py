class Settings:
    """
    Singleton Configuration Class
    Stores all project-level settings.
    """

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Settings, cls).__new__(cls)

            # -------------------------
            # Adzuna API Configuration
            # -------------------------
            cls._instance.API_BASE_URL = "https://api.adzuna.com/v1/api/jobs"
            cls._instance.COUNTRY = "in" 
            cls._instance.APP_ID = "f0b4ed84"
            cls._instance.APP_KEY = "fc8fe20a97548b58a536a590d445ba27"

            cls._instance.SEARCH_QUERY = "developer"
            cls._instance.RESULTS_PER_PAGE = 50
            cls._instance.MAX_JOBS = 1000

            # Request Headers (API usually doesn't need heavy headers)
            cls._instance.HEADERS = {
                "User-Agent": "Mozilla/5.0",
                "Accept": "application/json"
            }

            # -------------------------
            # File Paths
            # -------------------------
            cls._instance.RAW_DATA_PATH = "data/raw/raw_jobs.json"
            cls._instance.CLEANED_DATA_PATH = "data/processed/cleaned_jobs.csv"
            cls._instance.SKILL_FREQ_PATH = "data/processed/skill_frequency.csv"
            cls._instance.LOCATION_FREQ_PATH = "data/processed/location_frequency.csv"
            cls._instance.REPORT_PATH = "data/reports/summary_report.json"

            # -------------------------
            # Skill Keywords
            # -------------------------
            cls._instance.SKILL_KEYWORDS = [
                "Python", "JavaScript", "TypeScript", "React", "Node",
                "Django", "Flask", "FastAPI", "SQL", "PostgreSQL",
                "MongoDB", "AWS", "Azure", "GCP", "Docker",
                "Kubernetes", "Machine Learning", "AI",
                "Data Engineering", "Pandas", "TensorFlow", "Git"
            ]

        return cls._instance