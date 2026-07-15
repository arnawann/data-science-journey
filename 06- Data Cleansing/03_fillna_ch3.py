import pandas as pd #ch3

df = pd.read_csv("03- Pandas/data/sales_data.csv")

df["Category"] = df["Category"].fillna("Unknown")

print(df)