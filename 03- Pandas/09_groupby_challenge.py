import pandas as pd

print("=== Challenge Company Salary Report ===")
employees = {
    "Name": ["Rudi", "Bentol", "Yayan","Udon", "Kardi","Budi"],
    "Department": ["HR", "Finance", "HR", "IT", "HR", "IT"],
    "Salary": [7000, 4000, 2000, 1000, 3500, 10000]
}
df = pd.DataFrame(employees)


print("=== Challenge 1 Total Salary tiap Department ===")
print(df.groupby("Department")["Salary"].sum())

print("=== Challenge 2 Rata-rata Salary tiap Department ===")
print(df.groupby("Department")["Salary"].mean())

print("=== Challenge 3 Highest Salary tiap Department ===")
print(df.groupby("Department")["Salary"].max())

print("=== Challenge 4 Lowest Salary tiap Department ===")
print(df.groupby("Department")["Salary"].min())

print("=== Challenge 5 Jumlah pegawai tiap Department ===")
print(df.groupby("Department")["Name"].count())
