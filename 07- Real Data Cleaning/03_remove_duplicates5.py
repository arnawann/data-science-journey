#MATERI 5- Menghapus Langsung pada DataFrame (Deleting Directly from a DataFrame)
import pandas as pd

df = pd.read_csv("Project-01-Sales-Data-Cleaning/sales_data_dirty.csv")

df.drop_duplicates(inplace=True)

print(df)