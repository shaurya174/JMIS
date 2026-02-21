import os
import pandas as pd
import json

def run_analysis():
    # Paths
    processed_dir = os.path.join("data", "processed")
    report_path = os.path.join("data", "reports", "summary_report.json")

    # Load CSVs
    skill_df = pd.read_csv(os.path.join(processed_dir, "skill_frequency.csv"))
    location_df = pd.read_csv(os.path.join(processed_dir, "location_frequency.csv"))
    company_df = pd.read_csv(os.path.join(processed_dir, "company_frequency.csv"))
    month_df = pd.read_csv(os.path.join(processed_dir, "jobs_per_month.csv"))
    weekly_trends_df = pd.read_csv(os.path.join(processed_dir, "weekly_skill_trends.csv"), index_col=0)

    # Ensure counts are numeric and fill NaNs with 0
    for df in [skill_df, location_df, company_df, month_df]:
        df['Count'] = pd.to_numeric(df['Count'], errors='coerce').fillna(0).astype(int)

    # Top 5 skills
    top_skills = skill_df.sort_values(by='Count', ascending=False).head(5)
    top_skills_list = [{'Skill': row['Skill'], 'Count': row['Count']} for _, row in top_skills.iterrows()]

    # Top 5 locations
    top_locations = location_df.sort_values(by='Count', ascending=False).head(5)
    top_locations_list = [{'Location': row['State'], 'Count': row['Count']} for _, row in top_locations.iterrows()]

    # Top 5 companies
    top_companies = company_df.sort_values(by='Count', ascending=False).head(5)
    top_companies_list = [{'Company': row['Company'], 'Count': row['Count']} for _, row in top_companies.iterrows()]

    # Jobs per month (fill missing months with 0)
    month_df['Count'] = month_df['Count'].fillna(0).astype(int)
    month_list = [{'Month': row['Month'], 'Count': row['Count']} for _, row in month_df.iterrows()]

    # Weekly skill trends: Top skill per week
    # Weekly skill trends: Top skill per week
    weekly_trends_df.index = pd.to_datetime(weekly_trends_df.index)
    weekly_trends_df.fillna(0, inplace=True)  # fill missing counts with 0
    top_weekly_skills = weekly_trends_df.idxmax(axis=1).reset_index()
    top_weekly_skills.columns = ['Week', 'TopSkill']

    # Convert Week to string for JSON serialization
    top_weekly_skills['Week'] = top_weekly_skills['Week'].dt.strftime('%Y-%m-%d')

    weekly_trends_list = top_weekly_skills.to_dict(orient='records')

    # Consolidated summary
    summary = {
        'total_jobs': int(skill_df['Count'].sum()),  # total jobs counted via skills as proxy
        'top_skills': top_skills_list,
        'top_locations': top_locations_list,
        'top_companies': top_companies_list,
        'jobs_per_month': month_list,
        'weekly_top_skills': weekly_trends_list
    }

    # Save summary JSON
    os.makedirs(os.path.dirname(report_path), exist_ok=True)
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=4, ensure_ascii=False)

    print("Analysis completed. Summary saved to:", report_path)