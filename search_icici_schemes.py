import pandas as pd
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent

SCHEME_FILE = (
    PROJECT_DIR
    / "Data"
    / "Processed"
    / "live_mutual_fund_schemes.csv"
)

schemes = pd.read_csv(SCHEME_FILE)

schemes["schemeName"] = (
    schemes["schemeName"].fillna("").astype(str)
)

# Search for ICICI Prudential large-cap and bluechip schemes
matches = schemes[
    schemes["schemeName"].str.contains(
        "ICICI Prudential", case=False, regex=False
    )
    &
    (
        schemes["schemeName"].str.contains(
            "Large Cap", case=False, regex=False
        )
        |
        schemes["schemeName"].str.contains(
            "Bluechip", case=False, regex=False
        )
    )
]

print("=" * 80)
print("ICICI PRUDENTIAL SCHEME SEARCH")
print("=" * 80)

if matches.empty:
    print("No matching schemes found.")
else:
    print(
        matches[["schemeCode", "schemeName"]]
        .to_string(index=False)
    )

print("\nTotal matching schemes:", len(matches))