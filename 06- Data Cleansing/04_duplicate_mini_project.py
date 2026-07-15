import pandas as pd #Materi 4 — Menghapus duplikat berdasarkan kolom tertentu
df = pd.read_csv("03- Pandas/data/sales_data.csv")

clean_df = df.drop_duplicates()

rows_removed = len(df) - len(clean_df)

print("===== DUPLICATE DATA REPORT =====\n")

print("Rows Before:", len(df))
print("Rows After:", len(clean_df))
print("Duplicates Removed:", rows_removed)
print("Duplicates Removed:", df.duplicated().sum())

print("\nRemaining Columns:")

for col in clean_df.columns:
    print(col)