#Materi 1 — Mengganti nilai tertentu (replace())
import pandas as pd

df = pd.read_csv("03- Pandas/data/sales_data.csv")

df["Category"] = df["Category"].replace(
    "Electronics",
    "Electronic Devices"
)
print(df)