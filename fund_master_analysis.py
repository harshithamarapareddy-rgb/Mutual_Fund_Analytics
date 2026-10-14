import pandas as pd
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent
DATA_DIR = PROJECT_DIR / "Data" / "Raw"

fund_file = next(DATA_DIR.glob("*fund_master.csv"))
nav_file = next(DATA_DIR.glob("*nav_history.csv"))

funds = pd.read_csv(fund_file)
nav = pd.read_csv(nav_file)

print("=" * 60)
print("FUND MASTER ANALYSIS")
print("=" * 60)

print("\n1. Total schemes:", len(funds))

print("\n2. Unique fund houses:")
print(funds["fund_house"].dropna().unique())

print("\n3. Fund categories:")
print(funds["category"].dropna().unique())

print("\n4. Fund subcategories:")
print(funds["sub_category"].dropna().unique())

print("\n5. Available risk categories:")
print(funds["risk_category"].dropna().unique())

print("\n6. Duplicate AMFI codes in Fund Master:")
print(funds["amfi_code"].duplicated().sum())

fund_codes = set(funds["amfi_code"].dropna())
nav_codes = set(nav["amfi_code"].dropna())

print("\n7. Unique AMFI codes in Fund Master:", len(fund_codes))
print("8. Unique AMFI codes in NAV History:", len(nav_codes))

missing_in_nav = fund_codes - nav_codes
missing_in_master = nav_codes - fund_codes

print("\n9. Fund Master codes missing from NAV History:")
print(sorted(missing_in_nav) if missing_in_nav else "None")

print("\n10. NAV History codes missing from Fund Master:")
print(sorted(missing_in_master) if missing_in_master else "None")

print("\n11. Scheme counts by category:")
print(funds["category"].value_counts(dropna=False))

print("\n12. Scheme counts by risk category:")
print(funds["risk_category"].value_counts(dropna=False))

print("\n" + "=" * 60)
print("FUND MASTER ANALYSIS COMPLETED")
print("=" * 60)