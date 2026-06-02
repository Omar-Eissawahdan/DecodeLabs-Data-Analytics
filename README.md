Data Analytics Internship Portfolio
Intern Name: Omar Eissa Ibrahim Wahdan

Track: Data Analytics Internship @ DecodeLabs

This document serves as the comprehensive portfolio detailing the technical workflows, methodologies, and business insights extracted over the first two weeks. It showcases the transition from structural data sanitization to programmatic exploratory data analysis.

🔴 Week 1: Project 1 - Data Cleaning & Preprocessing
Tech Stack: Microsoft Excel | Data Sanitization | Structural Formatting

The foundational phase focused on transforming raw, unstructured data into a reliable, analytical-ready dataset.

1. Objective & Scope: To audit, clean, and standardize a messy sales dataset, removing inconsistencies and establishing a robust "single source of truth" for downstream analytical processes.

2. Execution Methodology: * Deduplication: Scanned and removed redundant row entries to ensure transaction volumes and revenue metrics remain accurate.

Missing Value Imputation: Addressed null values logically. Categorical gaps were treated, and numerical gaps were filled without skewing the variance.

Type Casting & Formatting: Standardized temporal fields (Dates) and financial fields (Currency) into consistent formats, rectifying alignment issues.

Integrity Validation: Conducted a final cross-reference check to ensure no anomalies persisted across the UnitPrice, Quantity, and TotalPrice columns.

🔴 Week 2: Project 2 - Exploratory Data Analysis (EDA)
Tech Stack: Python | Pandas | Matplotlib | Seaborn

Building upon the sanitized dataset from Week 1, the objective shifted toward algorithmic data discovery. This phase utilized Python's analytical libraries to programmatically uncover underlying patterns, correlations, and outliers.

1. Statistical Summary & Central Tendencies: Utilizing Pandas' describe() framework, numerical matrices were profiled to calculate foundational metrics (Mean, Median, Standard Deviation). This provided an immediate mathematical baseline of the dataset's geometry.

2. Unmasking Outliers (Anomaly Detection): A Boxplot visualization was generated using Seaborn to map the variability of the TotalPrice feature.

Finding: The plot isolated significant points beyond the upper whisker. In a business context, these are "signals" representing high-value VIP customer purchases or bulk B2B transactions, not entry errors.

3. Correlation Analysis: A Pearson Correlation Coefficient was calculated to investigate the relationship between product cost and consumer purchasing volume.

Coefficient Result: r ≈ 0.028

Analytical Insight: The result indicates near-zero linear correlation. Customers purchase the quantities they require irrespective of the unit price variance. Visually confirmed via a Scatter Plot.

4. Categorical Performance & Business Recommendations: Through GroupBy aggregation on the Product axis, a Bar Chart was constructed to rank inventory demand. The visual evidence clearly identified top-performing categories (e.g., Printers and Chairs), providing a direct compass for inventory forecasting.
