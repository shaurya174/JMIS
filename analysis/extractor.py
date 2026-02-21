import os
import sys
import pandas as pd
import ast

# Allow importing Settings
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config.settings import Settings

def run_extractor():
    # Paths
    cleaned_path = os.path.join("data", "processed", "cleaned_jobs.csv")
    output_dir = os.path.join("data", "processed")
    os.makedirs(output_dir, exist_ok=True)

    # Load cleaned jobs
    df = pd.read_csv(cleaned_path)

    # Skill frequency
    skills = Settings().SKILL_KEYWORDS
    df['skills_required_list'] = df['skills_required'].apply(lambda x: [s.lower() for s in ast.literal_eval(x)])
    skill_keywords_lower = [s.lower() for s in skills]
    all_skills = [skill for sublist in df['skills_required_list'] for skill in sublist if skill in skill_keywords_lower]
    skill_counts = pd.Series(all_skills).value_counts().reset_index()
    skill_counts.columns = ['Skill', 'Count']
    skill_counts.to_csv(os.path.join(output_dir, "skill_frequency.csv"), index=False)

    # Location frequency
    df_location = df.dropna(subset=['state'])
    df_location['state'] = df_location['state'].str.lower().str.strip()
    location_counts = df_location['state'].value_counts().reset_index()
    location_counts.columns = ['State', 'Count']
    location_counts.to_csv(os.path.join(output_dir, "location_frequency.csv"), index=False)

    # Company frequency
    df['company_clean'] = df['company'].str.lower().str.strip()
    company_counts = df['company_clean'].value_counts().reset_index()
    company_counts.columns = ['Company', 'Count']
    company_counts.to_csv(os.path.join(output_dir, "company_frequency.csv"), index=False)

    # Jobs per month
    df['date_posted_dt'] = pd.to_datetime(df['date_posted'])
    df['month'] = df['date_posted_dt'].dt.month_name()
    jobs_per_month_counts = df['month'].value_counts().reindex([
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ]).reset_index()
    jobs_per_month_counts.columns = ['Month', 'Count']
    jobs_per_month_counts.to_csv(os.path.join(output_dir, "jobs_per_month.csv"), index=False)

    # Weekly skill trends
    df_sorted = df.sort_values('date_posted_dt')
    df_sorted['skills_required_list'] = df_sorted['skills_required'].apply(lambda x: [s.lower() for s in ast.literal_eval(x)])
    df_exploded = df_sorted.explode('skills_required_list')
    df_exploded = df_exploded[df_exploded['skills_required_list'].isin(skill_keywords_lower)]
    df_exploded.set_index('date_posted_dt', inplace=True)
    weekly_trends = df_exploded.groupby([pd.Grouper(freq='W'), 'skills_required_list']).size().reset_index(name='Count')
    weekly_trends_df = weekly_trends.pivot(index='date_posted_dt', columns='skills_required_list', values='Count').fillna(0)
    weekly_trends_df = weekly_trends_df.sort_index()
    weekly_trends_df.to_csv(os.path.join(output_dir, "weekly_skill_trends.csv"))

    print("All CSVs generated in data/processed/")

if __name__ == "__main__":
    run_extractor()