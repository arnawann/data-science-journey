import pandas as pd #ch2

df = pd.read_csv("03- Pandas/data/sales_data.csv")

df["Category"] = df["Category"].replace(
    "Clothing",
    "Fashion"
)

print(df)