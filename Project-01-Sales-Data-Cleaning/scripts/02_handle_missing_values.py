import pandas as pd #miniproject

df = pd.read_csv("Project-01-Sales-Data-Cleaning/data/sales_data_dirty.csv")

print("===== HANDLE MISSING VALUE REPORT =====")

# Report before
print("\nMissing Value Before:")
print(df.isnull().sum())

print(
    "\nTotal Missing Before:",
    df.isnull().sum().sum()
)

# Fill mean
mean_price = df["Price"].mean()
df["Price"] = df["Price"].fillna(mean_price)

# Fill median
median_quantity = df["Quantity"].median()
df["Quantity"] = df["Quantity"].fillna(median_quantity)

# Report after
print("\nMissing Value After:")
print(df.isnull().sum())

print(
    "Total Missing After:",
    df.isnull().sum().sum()
)

print("\nCleaned Dataset:")
print(df)