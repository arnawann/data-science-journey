#Materi 1 — Save to CSV (Simpan ke CSV)
import pandas as pd

df = pd.read_csv("07- Real Data Cleaning/sales_data_dirty.csv")

df.to_csv(
    "07- Real Data Cleaning/cleaned_sales_data.csv",
    index=False
)

print("Dataset exported successfully!")