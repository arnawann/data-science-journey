#MATERI 5- Menghapus Langsung pada DataFrame (Deleting Directly from a DataFrame)
import pandas as pd

df = pd.read_csv("07- Real Data Cleaning/sales_data_dirty.csv")

df.drop_duplicates(inplace=True)

print(df)