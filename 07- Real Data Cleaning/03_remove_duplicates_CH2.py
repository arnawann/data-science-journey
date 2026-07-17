import pandas as pd #CH2-Tampilkan hanya data yang merupakan duplikat. (Show only the duplicate data.)

df = pd.read_csv("07- Real Data Cleaning/sales_data_dirty.csv")

duplicates  = df[df.duplicated()]

print("Duplicate Rows:")
print(duplicates)