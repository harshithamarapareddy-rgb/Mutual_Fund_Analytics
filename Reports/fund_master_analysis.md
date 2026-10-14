# Fund Master Analysis Report

## 1. Objective

The objective of this analysis is to explore the mutual fund master dataset, understand the distribution of schemes across categories and risk levels, and check data consistency between the Fund Master and NAV History datasets.

## 2. Dataset Overview

The Fund Master dataset contains 40 mutual fund schemes from 10 different fund houses. The dataset includes scheme information such as fund house, category, subcategory, risk category, expense ratio, benchmark, and AMFI code.

## 3. Key Findings

* Total schemes analyzed: 40
* Unique fund houses: 10
* Main categories: Equity and Debt
* Unique subcategories: 12
* Risk categories: 5
* Duplicate AMFI codes: 0

### Category Distribution

* Equity: 34 schemes
* Debt: 6 schemes

### Risk Distribution

* Moderate: 16 schemes
* High: 8 schemes
* Very High: 6 schemes
* Low: 6 schemes
* Moderately High: 4 schemes

## 4. Data Quality Checks

The analysis found no duplicate AMFI codes in the Fund Master dataset.

All 40 unique AMFI codes in the Fund Master dataset were also present in the NAV History dataset. No codes were missing from either dataset.

These results indicate that the two datasets are consistent with each other in terms of AMFI codes. External validation is still required to confirm the codes against an authoritative source.

## 5. Conclusion

The Fund Master dataset contains 40 schemes across 10 fund houses. Equity schemes form the majority of the dataset. The AMFI code checks did not identify duplicates or mismatches between the Fund Master and NAV History datasets.

This analysis provides a foundation for further work on NAV trends, mutual fund performance, risk analysis, and visualizations.
