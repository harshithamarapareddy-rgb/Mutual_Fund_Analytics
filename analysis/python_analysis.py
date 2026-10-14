import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Project folder location
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data" / "raw"
REPORT_DIR = PROJECT_DIR / "reports"

# Create reports folder if it does not exist
REPORT_DIR.mkdir(parents=True, exist_ok=True)

# Load mutual fund dataset
file_path = DATA_DIR / "1788499985420-bb134abf-07_scheme_performance.csv"
df = pd.read_csv(file_path)

print("=" * 60)
print("MUTUAL FUND DATA ANALYSIS")
print("=" * 60)

# 1. Dataset overview
print("\n1. DATASET OVERVIEW")
print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])

# 2. Missing values
print("\n2. MISSING VALUES")
print(df.isnull().sum())

# 3. Average returns
print("\n3. AVERAGE MUTUAL FUND RETURNS")
print("Average 1-year return:", round(df["return_1yr_pct"].mean(), 2), "%")
print("Average 3-year return:", round(df["return_3yr_pct"].mean(), 2), "%")
print("Average 5-year return:", round(df["return_5yr_pct"].mean(), 2), "%")

# 4. Top 5 funds by 3-year returns
print("\n4. TOP 5 FUNDS BY 3-YEAR RETURNS")

top_funds = df.nlargest(5, "return_3yr_pct")[
    ["scheme_name", "return_3yr_pct", "risk_grade"]
]

print(top_funds.to_string(index=False))

# Save results
top_funds.to_csv(REPORT_DIR / "top_5_mutual_funds.csv", index=False)

# 5. Category-wise average returns
print("\n5. CATEGORY-WISE AVERAGE 3-YEAR RETURNS")

category_returns = (
    df.groupby("category")["return_3yr_pct"]
    .mean()
    .sort_values(ascending=False)
)

print(category_returns.round(2))

# 6. Create graph
plt.figure(figsize=(10, 6))

category_returns.plot(kind="bar")

plt.title("Average 3-Year Returns by Mutual Fund Category")
plt.xlabel("Fund Category")
plt.ylabel("Average 3-Year Return (%)")
plt.xticks(rotation=45)
plt.tight_layout()

graph_path = REPORT_DIR / "category_returns.png"
plt.savefig(graph_path, dpi=300)
plt.close()

print("\nGraph saved to:", graph_path)
print("Top 5 funds saved to:", REPORT_DIR / "top_5_mutual_funds.csv")
print("\nDATA ANALYSIS COMPLETED SUCCESSFULLY!")