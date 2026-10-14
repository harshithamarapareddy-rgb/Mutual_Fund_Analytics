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

search_terms = [
    "HDFC Top 100 Fund",
    "HDFC Large Cap Fund",
    "SBI Bluechip Fund",
    "SBI Large Cap Fund",
    "Axis Bluechip Fund",
    "Axis Large Cap Fund",
    "ICICI Prudential Bluechip Fund",
    "Nippon India Large Cap Fund"
]

print("=" * 80)
print("MUTUAL FUND SCHEME SEARCH")
print("=" * 80)

for term in search_terms:
    matches = schemes[
        schemes["schemeName"].str.contains(
            term, case=False, regex=False, na=False
        )
    ]

    print(f"\nSearch: {term}")
    print("-" * 80)

    if matches.empty:
        print("No matching scheme found.")
    else:
        print(
            matches[["schemeCode", "schemeName"]]
            .head(5)
            .to_string(index=False)
        )

print("\n" + "=" * 80)
print("SEARCH COMPLETED")
print("=" * 80)