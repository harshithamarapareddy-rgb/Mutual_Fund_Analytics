
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Project folder
PROJECT_DIR = Path(__file__).resolve().parent

# Input and output paths
INPUT_FILE = (
    PROJECT_DIR
    / "Data"
    / "Processed"
    / "cleaned_nav_history.csv"
)

OUTPUT_DIR = PROJECT_DIR / "Reports"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Load the cleaned NAV data
df = pd.read_csv(INPUT_FILE, parse_dates=["date"])

# Sort records by scheme and date
df = df.sort_values(["scheme_code", "date"])

# Convert each fund's starting NAV to 100
df["indexed_nav"] = (
    df["nav"]
    / df.groupby("scheme_code")["nav"].transform("first")
) * 100

# Create the line chart
plt.figure(figsize=(12, 6))

for scheme_name, group in df.groupby("scheme_name"):
    plt.plot(
        group["date"],
        group["indexed_nav"],
        label=scheme_name
    )

plt.title("Historical Mutual Fund NAV Performance")
plt.xlabel("Date")
plt.ylabel("Indexed NAV (Starting Value = 100)")
plt.legend(fontsize=8)
plt.grid(True)
plt.tight_layout()

# Save the chart
chart_file = OUTPUT_DIR / "nav_performance_chart.png"
plt.savefig(chart_file, dpi=300)

# Display the chart
plt.show()

print("\nChart saved successfully:")
print(chart_file)

