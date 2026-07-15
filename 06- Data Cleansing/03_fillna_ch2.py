import pandas as pd #ch2

df = pd.read_csv("03- Pandas/data/sales_data.csv")

mean_quantity = df["Quantity"].mean()

df["Quantity"] = df["Quantity"].fillna(mean_quantity)

print(df)