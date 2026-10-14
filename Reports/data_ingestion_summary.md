# Bluestock Fintech — Mutual Fund Analytics

## Data Ingestion Summary

### 1. Objective

To load the 10 provided CSV datasets using Python and examine their structure and basic data quality.

### 2. Tools Used

* Python
* Pandas
* VS Code

### 3. Dataset Summary

| Dataset               |       Rows | Columns |
| --------------------- | ---------: | ------: |
| Investor Transactions |     32,778 |      13 |
| Portfolio Holdings    |        322 |       8 |
| Benchmark Indices     |      8,050 |       3 |
| Fund Master           |         40 |      15 |
| NAV History           |     46,000 |       3 |
| AUM by Fund House     |         90 |       5 |
| Monthly SIP Inflows   |         48 |       6 |
| Category Inflows      |        144 |       3 |
| Industry Folio Count  |         21 |       6 |
| Scheme Performance    |         40 |      19 |
| **Total**             | **87,533** |  **81** |

### 4. Initial Data Quality Findings

* All 10 CSV files were discovered and read by the ingestion script.
* No duplicate rows were reported in any dataset.
* No missing values were reported in nine datasets.
* The Monthly SIP Inflows dataset contains 12 missing values in `yoy_growth_pct`.
* Further validation of scheme codes, dates, numeric ranges, and dataset relationships is required.

### 5. Conclusion

The initial data ingestion process completed successfully. All 10 datasets were loaded and examined using Pandas. The next stage is to validate the Fund Master dataset and investigate data quality issues.
