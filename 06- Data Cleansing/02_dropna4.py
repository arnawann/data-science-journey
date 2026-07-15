import pandas as pd

df = pd.read_csv("03- Pandas/data/sales_data.csv")

clean_df = df.dropna()

#Materi 4 - Menghapus langsung pada DataFrame asli
# biasanya membuat DataFrame Baru
# Membuat DataFrame baru
