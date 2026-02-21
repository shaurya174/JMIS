import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings("ignore")

# ===== Seaborn Theme =====
sns.set_theme(style="whitegrid")
sns.set_context("notebook", font_scale=1.2)
sns.set_palette("Set2")

# ===== Matplotlib Styling =====
plt.rcParams.update({
    'figure.figsize': (10,6),
    'axes.titlesize': 18,
    'axes.labelsize': 14,
    'xtick.labelsize': 12,
    'ytick.labelsize': 12,
    'axes.titleweight': 'bold',
    'axes.labelweight': 'bold',
    'grid.color': '#dcdcdc',
    'grid.linestyle': '--',
    'grid.linewidth': 0.7,
    'legend.fontsize': 12,
    'legend.frameon': True,
    'legend.framealpha': 0.9,
    'legend.edgecolor': 'black',
    'lines.linewidth': 2,
    'lines.markersize': 8
})

# ===== Paths =====
processed_dir = os.path.join("data", "processed")
plots_dir = os.path.join("visualization", "plots")
os.makedirs(plots_dir, exist_ok=True)

def plot_skills():
    df = pd.read_csv(os.path.join(processed_dir, "skill_frequency.csv"))
    df_sorted = df.sort_values(by='Count', ascending=True)

    plt.figure(figsize=(12,8))
    sns.barplot(x='Count', y='Skill', data=df_sorted, palette='viridis')
    plt.title("Most In-Demand Skills in Job Postings", fontsize=20, fontweight='bold')
    plt.xlabel("Number of Job Postings", fontsize=14, fontweight='bold')
    plt.ylabel("Skills", fontsize=14, fontweight='bold')

    for index, value in enumerate(df_sorted['Count']):
        plt.text(value + 5, index, str(value), va='center', fontsize=12)

    plt.tight_layout()
    plt.savefig(os.path.join(plots_dir, "skill_frequency.png"))
    plt.close()

def plot_locations():
    df = pd.read_csv(os.path.join(processed_dir, "location_frequency.csv"))
    df_sorted = df.sort_values(by='Count', ascending=False)
    df_sorted['cum_pct'] = df_sorted['Count'].cumsum() / df_sorted['Count'].sum() * 100

    plt.figure(figsize=(14,8))
    sns.barplot(x='State', y='Count', data=df_sorted, palette='magma')
    plt.xticks(rotation=45, ha='right')

    ax2 = plt.gca().twinx()
    sns.lineplot(x='State', y='cum_pct', data=df_sorted, sort=False, color='cyan', marker='o', ax=ax2)
    ax2.set_ylabel('Cumulative %', fontsize=14, fontweight='bold')
    ax2.set_ylim(0, 110)

    plt.title("Pareto Analysis: Job Postings by State", fontsize=20, fontweight='bold')
    plt.xlabel("State", fontsize=14, fontweight='bold')
    plt.ylabel("Number of Job Postings", fontsize=14, fontweight='bold')

    plt.tight_layout()
    plt.savefig(os.path.join(plots_dir, "location_pareto.png"))
    plt.close()

def plot_companies():
    df = pd.read_csv(os.path.join(processed_dir, "company_frequency.csv"))
    df_top = df.sort_values(by='Count', ascending=True).tail(15)

    plt.figure(figsize=(14,8))
    sns.barplot(x='Count', y='Company', data=df_top, palette='coolwarm')
    plt.title("Top 15 Companies by Job Postings", fontsize=20, fontweight='bold')
    plt.xlabel("Number of Job Postings", fontsize=14, fontweight='bold')
    plt.ylabel("Company", fontsize=14, fontweight='bold')

    for index, value in enumerate(df_top['Count']):
        plt.text(value + 0.5, index, str(value), va='center', fontsize=12)

    plt.tight_layout()
    plt.savefig(os.path.join(plots_dir, "top_companies.png"))
    plt.close()

def plot_weekly_trends():
    df = pd.read_csv(os.path.join(processed_dir, "weekly_skill_trends.csv"))
    df['date_posted_dt'] = pd.to_datetime(df['date_posted_dt'])

    # Top 5 skills by total postings
    skill_totals = df.drop(columns='date_posted_dt').sum().sort_values(ascending=False)
    top_skills = skill_totals.head(5).index.tolist()

    plt.figure(figsize=(14,7))
    for skill in top_skills:
        sns.lineplot(x='date_posted_dt', y=skill, data=df, marker='o', linewidth=2.5, label=skill)

    plt.title("Weekly Job Demand for Top 5 Skills Over Time", fontsize=20, fontweight='bold')
    plt.xlabel("Week", fontsize=14, fontweight='bold')
    plt.ylabel("Number of Job Postings", fontsize=14, fontweight='bold')
    plt.xticks(rotation=45)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend(title='Skills', fontsize=12, title_fontsize=14)
    plt.tight_layout()
    plt.savefig(os.path.join(plots_dir, "weekly_skill_trends.png"))
    plt.close()

def run_visualization():
    plot_skills()
    plot_locations()
    plot_companies()
    plot_weekly_trends()
    print(f"All plots saved in {plots_dir}")