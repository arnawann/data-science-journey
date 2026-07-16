#Materi 4 — Mengganti seluruh DataFrame

import pandas as pd

df = pd.read_csv("03- Pandas/data/sales_data.csv")

new_df = df.replace(
    "Electronics",
    "Electronic Devices"
)

print(new_df)