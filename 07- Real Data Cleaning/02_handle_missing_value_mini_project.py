import pandas as pd #miniproject

df = pd.read_csv("07- Real Data Cleaning/sales_data_dirty.csv")

print("===== HANDLE MISSING VALUE REPORT =====")

print("\nMissing Value Before:")
print(df.isnull().sum())

print(
    "\nTotal Missing Before:",
    df.isnull().sum().sum()
)

# Fill Price
mean_price = df["Price"].mean()
df["Price"] = df["Price"].fillna(mean_price)

# Fill Quantity
median_quantity = df["Quantity"].median()
df["Quantity"] = df["Quantity"].fillna(median_quantity)

print("\nMissing Value After:")
print(df.isnull().sum())

print(
    "Total Missing After:",
    df.isnull().sum().sum()
)

print("\nCleaned Dataset:")
print(df)