import pandas as pd

df = pd.read_csv("Project-01-Sales-Data-Cleaning/data/sales_data_dirty.csv")

# Handle Missing Values
df["Price"] = df["Price"].fillna(df["Price"].mean())
df["Quantity"] = df["Quantity"].fillna(df["Quantity"].median())

# Remove Duplicates
df = df.drop_duplicates()

# Standardize Categories
df["Category"] = df["Category"].replace({
    "electronics": "Electronics",
    "Clothng": "Clothing"
})

df["Category"] = df["Category"].str.title()

# Export
df.to_csv(
    "Project-01-Sales-Data-Cleaning/data/cleaned_sales_data.csv",
    index=False
)

print("Dataset exported successfully!")