import os
import json
import pandas as pd
import numpy as np

from config.settings import Settings

def run_cleaning():
    settings = Settings()
    
    # File paths
    raw_path = settings.RAW_DATA_PATH
    processed_path = settings.CLEANED_DATA_PATH
    
    # Load raw jobs
    with open(raw_path, "r", encoding="utf-8") as f:
        jobs = json.load(f)
    
    df = pd.DataFrame(jobs)
    
    # Drop salary columns (all empty)
    for col in ['salary_avg', 'salary_min', 'salary_max']:
        if col in df.columns:
            df.drop(col, axis=1, inplace=True)
    
    # Convert date_posted to datetime
    df['date_posted'] = pd.to_datetime(df['date_posted'], errors='coerce')
    
    # Drop job_type if mostly N/A
    if 'job_type' in df.columns:
        df.drop('job_type', axis=1, inplace=True)
    
    # Normalize skills
    df['skills_required'] = df['skills_required'].apply(
        lambda skills: list(set(skill.strip().lower() for skill in skills))
    )
    
    # Clean location
    df['location'] = df['location'].apply(lambda x: x.strip().title() if pd.notna(x) else x)
    
    # Split location into city/state
    def split_location(loc):
        if pd.isna(loc):
            return None, None
        parts = [p.strip() for p in loc.split(',')]
        if len(parts) == 1:
            return None, parts[0]  # Only country
        return parts[0], parts[1]  # City, State
    
    df['city'], df['state'] = zip(*df['location'].apply(split_location))
    
    # Replace redundant state values
    df['state'] = df['state'].replace('India', np.nan)
    
    # Clean text columns
    text_cols = ['title', 'company', 'job_desc']
    for col in text_cols:
        df[col] = df[col].apply(lambda x: x.strip() if pd.notna(x) else x)
    
    # Drop original location column
    df.drop('location', axis=1, inplace=True)
    
    # Save cleaned CSV
    os.makedirs(os.path.dirname(processed_path), exist_ok=True)
    df.to_csv(processed_path, index=False)
    
    print(f"Cleaned jobs saved to {processed_path}")