import pandas as pd
from pathlib import Path

# Find the project folder

PROJECT_DIR = Path(__file__).resolve().parent
DATA_DIR = PROJECT_DIR / "Data" / "Raw"

# Find CSV files

csv_files = list(DATA_DIR.glob("*.csv"))

print("=" * 60)
print("BLUESTOCK MUTUAL FUND ANALYTICS - DATA INGESTION")
print("=" * 60)

if not csv_files:
    print("ERROR: No CSV files found in data/raw.")
    print("Please check your folder location.")
else:
    print(f"\nFound {len(csv_files)} CSV file(s).\n")

for file_path in sorted(csv_files):
    print("\n" + "=" * 60)
    print(f"DATASET: {file_path.name}")
    print("=" * 60)

    try:
        df = pd.read_csv(file_path)

        print(f"\nNumber of rows: {df.shape[0]}")
        print(f"Number of columns: {df.shape[1]}")

        print("\nColumn names:")
        print(df.columns.tolist())

        print("\nColumn data types:")
        print(df.dtypes)

        print("\nFirst five rows:")
        print(df.head().to_string(index=False))

        print("\nMissing values:")
        print(df.isnull().sum())

        print(f"\nDuplicate rows: {df.duplicated().sum()}")

    except Exception as error:
        print(f"Error reading {file_path.name}: {error}")


print("\n" + "=" * 60)
print("DATA INGESTION CHECK COMPLETED")
print("=" * 60)
