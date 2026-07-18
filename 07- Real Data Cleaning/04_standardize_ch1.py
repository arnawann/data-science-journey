import pandas as pd

df = pd.read_csv("Project-01-Sales-Data-Cleaning/sales_data_dirty.csv")

df["Category"] = df["Category"].replace(
    "electronics",
    "Electronics"
)
print(df["Category"].unique())