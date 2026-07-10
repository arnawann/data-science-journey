print("=== Challenge ===")

import pandas as pd
import numpy as np

students = {
    "Name": ["Yayan", "Budi","Sinta", "Bambang","Gunadi"],
    "Age": [np.nan,10,np.nan,22,18],
    "Score": [85,90,95,np.nan,85]
}
df = pd.DataFrame(students)
print(df)

print("=== Challenge 1 - tampilkan jumlah data kosong tiap kolom ===")
print(df.isnull().sum())

print("=== Challenge 2 - Cetak data setelah semua NaN diisi dengan 0 ===")
print(df.fillna(0))

print("=== Challenge 3 - Isi hanya kolom Score yang kosong dengan 75 ===")
df["Score"] = df["Score"].fillna(75)
print(df)

print("=== Challenge 4 - Cetak data setelah dropna() ===")
print(df.dropna())

print("=== Missing Value Report ===")

print("Total Missing Age :", df["Age"].isnull().sum())
print("Total Missing Score :", df["Score"].isnull().sum())
print("=== Data setelah dropna() ===")
print(df.dropna())
print("=== Data setelah fillna(0) ===")
print(df.fillna(0))
