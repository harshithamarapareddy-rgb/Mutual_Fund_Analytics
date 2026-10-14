import requests
import pandas as pd

scheme_code = 120586

url = f"https://api.mfapi.in/mf/{scheme_code}"

print("=" * 60)
print("TESTING ICICI PRUDENTIAL LARGE CAP FUND")
print("=" * 60)

try:
    response = requests.get(url, timeout=30)
    response.raise_for_status()

    result = response.json()

    print("\nScheme name:")
    print(result.get("meta", {}).get("scheme_name"))

    nav_data = pd.DataFrame(result.get("data", []))

    if nav_data.empty:
        print("\nNo NAV history found.")
    else:
        nav_data["date"] = pd.to_datetime(
            nav_data["date"],
            format="%d-%m-%Y",
            errors="coerce"
        )

        nav_data["nav"] = pd.to_numeric(
            nav_data["nav"],
            errors="coerce"
        )

        nav_data = nav_data.dropna(subset=["date", "nav"])

        print("\nTotal NAV records:", len(nav_data))
        print("Earliest NAV date:", nav_data["date"].min().date())
        print("Latest NAV date:", nav_data["date"].max().date())

        print("\nLatest 5 NAV records:")
        print(
            nav_data.sort_values("date", ascending=False)
            .head(5)
            .to_string(index=False)
        )

except requests.exceptions.RequestException as error:
    print("\nAPI request failed:", error)


print("\nTEST COMPLETED")
