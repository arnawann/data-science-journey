import pandas as pd #ch3

df = pd.read_csv("07- Real Data Cleaning/sales_data_dirty.csv")

print("Before:")
print(df.isnull().sum())

#Fill missing values
mean_price = df["Price"].mean()
df["Price"] = df["Price"].fillna(mean_price)

median_quantity = df["Quantity"].median()
df["Quantity"] = df["Quantity"].fillna(median_quantity)

print("\nAfter:")
print(df.isnull().sum())