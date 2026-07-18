# Project 01 — Sales Data Cleaning

## Overview

This project demonstrates a complete **data cleaning workflow** using Python and Pandas.

The dataset intentionally contains common real-world data quality issues such as:

- Missing values
- Duplicate rows
- Inconsistent category names

The goal of this project is to transform raw data into a clean dataset that is ready for analysis.

---

## Dataset

**Input**

```
sales_data_dirty.csv
```

Contains:

- Missing values
- Duplicate records
- Typographical errors
- Inconsistent capitalization

**Output**

```
cleaned_sales_data.csv
```

A cleaned dataset ready for analysis.

---

## Project Structure

```text
Project-01-Sales-Data-Cleaning/
│
├── data/
│   ├── sales_data_dirty.csv
│   └── cleaned_sales_data.csv
│
├── scripts/
│   ├── 01_data_inspection.py
│   ├── 02_handle_missing_values.py
│   ├── 03_remove_duplicates.py
│   ├── 04_standardize_values.py
│   ├── 05_export_clean_dataset.py
│   └── full_clean_pipeline.py
│
└── README.md
```

---

## Workflow

### 1. Data Inspection

- Dataset preview
- Dataset shape
- Column names
- Data types
- Missing values
- Duplicate rows
- Unique categories

---

### 2. Handle Missing Values

- Fill missing Price using Mean
- Fill missing Quantity using Median
- Verify missing values are removed

---

### 3. Remove Duplicate Rows

- Count duplicate rows
- Remove duplicates
- Report rows removed

---

### 4. Standardize Values

Standardized inconsistent category values.

Example:

| Before | After |
|---------|-------|
| electronics | Electronics |
| Clothng | Clothing |

---

### 5. Export Clean Dataset

Export the cleaned dataset as

```
cleaned_sales_data.csv
```

---

## Skills Demonstrated

- Pandas
- Data Inspection
- Missing Value Handling
- Duplicate Removal
- Data Standardization
- CSV Export
- Data Cleaning Workflow

---

## Technologies

- Python 3
- Pandas

---

## Learning Outcomes

After completing this project I learned how to:

- Inspect a raw dataset
- Identify data quality issues
- Handle missing values
- Remove duplicate records
- Standardize inconsistent values
- Export a clean dataset
- Build a complete data cleaning pipeline

---

## Future Improvements

- Handle outliers
- Validate numeric ranges
- Automate cleaning with reusable functions
- Add logging
- Write unit tests

---

## Author

Arnawan Dwi Nugraha

Data Science Journey