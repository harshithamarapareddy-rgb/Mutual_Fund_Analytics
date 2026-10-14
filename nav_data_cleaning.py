import pandas as pd
from pathlib import Path

# Project folders
PROJECT_DIR = Path(__file__).resolve().parent

INPUT_FILE = (
    PROJECT_DIR
    / "Data"
    / "Processed"
    / "live_nav_history.csv"
)

OUTPUT_DIR = PROJECT_DIR / "Data" / "Processed"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_FILE = OUTPUT_DIR / "cleaned_nav_history.csv"

print("=" * 60)
print("NAV DATA CLEANING AND QUALITY CHECK")
print("=" * 60)

# Load the dataset
df = pd.read_csv(INPUT_FILE)

print("\n1. Original dataset shape:", df.shape)

# Display column names
print("\n2. Columns:")
print(df.columns.tolist())

# Check missing values
print("\n3. Missing values before cleaning:")
print(df.isnull().sum())

# Check duplicate rows
print("\n4. Duplicate rows:", df.duplicated().sum())

# Convert columns to appropriate data types
df["date"] = pd.to_datetime(df["date"], errors="coerce")
df["nav"] = pd.to_numeric(df["nav"], errors="coerce")
df["scheme_code"] = pd.to_numeric(
    df["scheme_code"], errors="coerce"
).astype("Int64")

# Remove rows with missing essential values
df = df.dropna(
    subset=["scheme_code", "scheme_name", "date", "nav"]
).copy()

# Remove invalid NAV values
df = df[df["nav"] > 0].copy()

# Remove duplicate records for the same scheme and date
df = df.drop_duplicates(
    subset=["scheme_code", "date"],
    keep="last"
)

# Sort by scheme and date
df = df.sort_values(
    ["scheme_code", "date"]
).reset_index(drop=True)

# Save cleaned data
df.to_csv(OUTPUT_FILE, index=False)

print("\n5. Cleaned dataset shape:", df.shape)

print("\n6. Missing values after cleaning:")
print(df.isnull().sum())

print("\n7. Duplicate scheme-date records after cleaning:")
print(df.duplicated(subset=["scheme_code", "date"]).sum())

print("\n8. NAV values less than or equal to zero:")
print((df["nav"] <= 0).sum())

print("\n9. Records per scheme:")
print(
    df.groupby("scheme_name")
    .agg(
        total_records=("nav", "count"),
        first_date=("date", "min"),
        latest_date=("date", "max"),
        minimum_nav=("nav", "min"),
        maximum_nav=("nav", "max")
    ).to_string()
)

print("\n10. Cleaned file saved to:")
print(OUTPUT_FILE)

print("\n" + "=" * 60)
print("DATA CLEANING COMPLETED")
print("=" * 60)