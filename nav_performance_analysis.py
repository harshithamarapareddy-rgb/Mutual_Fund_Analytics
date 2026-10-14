import pandas as pd
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent

INPUT_FILE = (
    PROJECT_DIR
    / "Data"
    / "Processed"
    / "cleaned_nav_history.csv"
)

OUTPUT_DIR = PROJECT_DIR / "Data" / "Processed"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(INPUT_FILE, parse_dates=["date"])

print("=" * 70)
print("MUTUAL FUND NAV PERFORMANCE ANALYSIS")
print("=" * 70)

# Sort each fund's NAV records by date
df = df.sort_values(["scheme_code", "date"]).copy()

# Calculate daily percentage return for each scheme
df["daily_return_pct"] = (
    df.groupby("scheme_code")["nav"]
    .pct_change() * 100
)

# Calculate performance summary for each scheme
summary = (
    df.groupby(["scheme_code", "scheme_name"])
    .agg(
        first_date=("date", "min"),
        latest_date=("date", "max"),
        first_nav=("nav", "first"),
        latest_nav=("nav", "last"),
        minimum_nav=("nav", "min"),
        maximum_nav=("nav", "max"),
        average_nav=("nav", "mean"),
        average_daily_return_pct=("daily_return_pct", "mean"),
        daily_return_volatility_pct=("daily_return_pct", "std"),
        total_records=("nav", "count")
    )
    .reset_index()
)

# Calculate total NAV change over the available period
summary["total_return_pct"] = (
    (summary["latest_nav"] - summary["first_nav"])
    / summary["first_nav"]
) * 100

# Save the performance summary
summary_file = OUTPUT_DIR / "nav_performance_summary.csv"
summary.to_csv(summary_file, index=False)

# Save daily returns separately
daily_returns_file = OUTPUT_DIR / "nav_daily_returns.csv"
df.to_csv(daily_returns_file, index=False)

print("\n1. Number of schemes:", summary["scheme_code"].nunique())

print("\n2. Performance summary:")
print(
    summary[
        [
            "scheme_name",
            "first_nav",
            "latest_nav",
            "total_return_pct",
            "daily_return_volatility_pct",
            "total_records"
        ]
    ].round(2).to_string(index=False)
)

print("\n3. Files saved:")
print(summary_file)
print(daily_returns_file)

print("\n" + "=" * 70)
print("PERFORMANCE ANALYSIS COMPLETED")
print("=" * 70)