import pandas as pd #ch1

df = pd.read_csv("03- Pandas/data/sales_data.csv")

df["Category"] = df["Category"].replace(
    'Furniture',
    'Home Furniture'
)

print(df)