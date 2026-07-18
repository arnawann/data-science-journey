#Materi 2 — Export After Cleaning (Export setelah Cleaning)
import pandas as pd

df = pd.read_csv("07- Real Data Cleaning/sales_data_dirty.csv")

# Handle missing values
df["Price"] = df["Price"].fillna(df["Price"].mean())
df["Quantity"] = df["Quantity"].fillna(df["Quantity"].median())

# Remove duplicates
df = df.drop_duplicates()

# Standardize values
df["Category"] = df["Category"].replace({
    "electronics": "Electronics",
    "Clothng": "Clothing"
})

df.to_csv(
    "07- Real Data Cleaning/cleaned_sales_data.csv",
    index=False
)

print("Clean dataset saved!")