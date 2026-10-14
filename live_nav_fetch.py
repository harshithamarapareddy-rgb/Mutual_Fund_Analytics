import requests
import pandas as pd
from pathlib import Path

# Project folder
PROJECT_DIR = Path(__file__).resolve().parent

# Output folder
OUTPUT_DIR = PROJECT_DIR / "Data" / "Processed"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Mutual fund API
API_URL = "https://api.mfapi.in/mf"

print("=" * 50)
print("LIVE MUTUAL FUND NAV FETCH")
print("=" * 50)

try:
    response = requests.get(API_URL, timeout=30)
    response.raise_for_status()

    schemes = response.json()

    print("\nAPI connection successful!")
    print("Total schemes available:", len(schemes))

    # Display the first 10 schemes
    print("\nSample mutual fund schemes:")

    for scheme in schemes[:10]:
        print(
            "Scheme Code:", scheme.get("schemeCode"),
            "| Scheme Name:", scheme.get("schemeName")
        )

    # Save the scheme list as a CSV file
    schemes_df = pd.DataFrame(schemes)

    output_file = OUTPUT_DIR / "live_mutual_fund_schemes.csv"
    schemes_df.to_csv(output_file, index=False)

    print("\nScheme list saved successfully!")
    print("File location:", output_file)

except requests.exceptions.RequestException as error:
    print("\nAPI connection failed.")
    print("Error:", error)

print("\n" + "=" * 50)
print("PROCESS COMPLETED")
print("=" * 50)