import pandas as pd

df = pd.read_csv("07- Real Data Cleaning/sales_data_dirty.csv")

df["Category"] = df["Category"].replace(
    "electronics",
    "Electronics"
)
print(df["Category"].unique())