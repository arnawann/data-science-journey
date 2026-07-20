# ======================================
# PROJECT 01 - SALES DATA CLEANING
# ======================================

import pandas as pd

df = pd.read_csv("Project-01-Sales-Data-Cleaning/data/sales_data_dirty.csv")

print("\n===== DATA INSPECTION =====\n")

print("\nDataset Preview:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nUnique Categories:")
print(df["Category"].unique())

print("\n===== HANDLE MISSING VALUE REPORT =====")

# Report before
print("\nMissing Value Before:")
print(df.isnull().sum())

print(
    "\nTotal Missing Before:",
    df.isnull().sum().sum()
)

# Fill missing values using mean
mean_price = df["Price"].mean()
df["Price"] = df["Price"].fillna(mean_price)

# Fill missing values using median
median_quantity = df["Quantity"].median()
df["Quantity"] = df["Quantity"].fillna(median_quantity)

# Report after
print("\nMissing Value After:")
print(df.isnull().sum())

print(
    "Total Missing After:",
    df.isnull().sum().sum()
)

print("\nCleaned Dataset Preview:")
print(df.head())

print("\n===== DUPLICATE REPORT =====")

duplicates = df.duplicated().sum()

print("Duplicate Rows:", duplicates)

print("Rows Before:", len(df))

clean_df = df.drop_duplicates()

print("Rows After:", len(clean_df))

print("Rows Removed:", len(df) - len(clean_df))

df = clean_df

print("\nRemaining Products:")

print("Total Products:", df["Product"].nunique())

for product in df["Product"].unique():
    print("-", product)

print("\n===== VALUE STANDARDIZATION REPORT =====")

print("\nCategories Before:")

print(df["Category"].unique())

df["Category"] = df["Category"].replace({
    "electronics": "Electronics",
    "Clothng": "Clothing"
})

df["Category"] = df["Category"].str.title()

print("\nCategories After:")

print(df["Category"].unique())

print("\nTotal Categories:", df["Category"].nunique())

print("\n===== FINAL DATASET =====")

print("\nDataset Shape:")
print(df.shape)

print("\nFinal Columns:")
print(df.columns.tolist())

print("\nTotal Columns:", len(df.columns))

print("\nTotal Missing Values:")
print(df.isnull().sum().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nFinal Categories:")
print(df["Category"].unique())
print("Total Categories:", df["Category"].nunique())

print("\nDataset Preview:")
print(df.head())

print("\n===== EXPORT REPORT =====")

print("\nExporting Cleaned Dataset...")
df.to_csv(
    "Project-01-Sales-Data-Cleaning/data/cleaned_sales_data.csv",
    index=False
)
print("\n✓ Export completed successfully!")
print("Saved to:") 
print("Project-01-Sales-Data-Cleaning/data/cleaned_sales_data.csv")