import requests
import pandas as pd
from pathlib import Path
import time

PROJECT_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = PROJECT_DIR / "Data" / "Processed"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

API_URL = "https://api.mfapi.in/mf"

# Scheme codes identified from your API scheme list
selected_schemes = [
    {
        "scheme_code": 119018,
        "scheme_name": "HDFC Large Cap Fund - Direct Plan - Growth Option"
    },
    {
        "scheme_code": 119598,
        "scheme_name": "SBI Large Cap Fund - Direct Plan - Growth"
    },
    {
        "scheme_code": 120465,
        "scheme_name": "Axis Large Cap Fund - Direct Plan - Growth Option"
    },
    {
        "scheme_code": 120586,
        "scheme_name": "ICICI Prudential Large Cap Fund - Direct Plan - Growth"
    },
    {
        "scheme_code": 118632,
        "scheme_name": "Nippon India Large Cap Fund - Direct Plan - Growth Option"
    }
]

all_nav_data = []

print("=" * 65)
print("FETCHING NAV HISTORY FOR SELECTED MUTUAL FUNDS")
print("=" * 65)

for scheme in selected_schemes:
    code = scheme["scheme_code"]

    try:
        url = f"{API_URL}/{code}"
        response = requests.get(url, timeout=30)
        response.raise_for_status()

        result = response.json()

        actual_name = result.get("meta", {}).get(
            "scheme_name", scheme["scheme_name"]
        )

        records = result.get("data", [])

        print(f"\nScheme: {actual_name}")
        print(f"Scheme Code: {code}")
        print(f"NAV records: {len(records)}")

        for record in records:
            all_nav_data.append({
                "scheme_code": code,
                "scheme_name": actual_name,
                "date": record.get("date"),
                "nav": record.get("nav")
            })

    except (requests.exceptions.RequestException, ValueError) as error:
        print(f"\nCould not fetch scheme {code}: {error}")

    time.sleep(0.5)

if all_nav_data:
    nav_df = pd.DataFrame(all_nav_data)

    nav_df["date"] = pd.to_datetime(
        nav_df["date"],
        format="%d-%m-%Y",
        errors="coerce"
    )

    nav_df["nav"] = pd.to_numeric(
        nav_df["nav"],
        errors="coerce"
    )

    nav_df = nav_df.dropna(subset=["date", "nav"])

    nav_df = nav_df.sort_values(
        ["scheme_code", "date"]
    ).reset_index(drop=True)

    output_file = OUTPUT_DIR / "live_nav_history.csv"
    nav_df.to_csv(output_file, index=False)

    print("\n" + "=" * 65)
    print("NAV DATA SUMMARY")
    print("=" * 65)

    print("Total records:", len(nav_df))
    print("Unique schemes:", nav_df["scheme_code"].nunique())
    print("Earliest NAV date:", nav_df["date"].min().date())
    print("Latest NAV date:", nav_df["date"].max().date())

    print("\nRecords by scheme:")
    print(
        nav_df.groupby("scheme_name")
        .agg(
            records=("nav", "count"),
            earliest_date=("date", "min"),
            latest_date=("date", "max")
        ).to_string()
    )

    print("\nSaved to:", output_file)

    print("\nSample records:")
    print(nav_df.head(10).to_string(index=False))

else:
    print("\nNo NAV data was retrieved.")

print("\nPROCESS COMPLETED")