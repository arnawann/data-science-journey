#Materi 3 — Reading Export Results (Membaca Hasil Export)
import pandas as pd

clean_df = pd.read_csv(
    "07- Real Data Cleaning/cleaned_sales_data.csv"
)

print(clean_df)