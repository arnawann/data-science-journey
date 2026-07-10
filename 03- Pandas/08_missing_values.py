import pandas as pd
import numpy as np

students = {
    "Name": ["Ali", "Ahmad","Sarah", "Fatimah","Hasan"],
    "Age": [20,np.nan,19,22,np.nan],
    "Score": [85,90,np.nan,95,85]
}
df = pd.DataFrame(students)
print(df)

print("=== Mengecek Data Kosong ===")
print(df.isnull())

print("=== Menghitung jumlah Data Kosong ===")
print(df.isnull().sum())

print("=== Menghapus Data Kosong ===")
print(df.dropna())

print("=== Mengisi Data Kosong ===")
print(df.fillna(0))

print("=== Mengisi Hanya Satu Kolom ===")
df["Age"] = df["Age"].fillna(18)
print(df)