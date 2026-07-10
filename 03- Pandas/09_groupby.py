import pandas as pd
employees = {
    "Name": ["Jarjit", "Ali", "Ahmad","Sarah", "Fatimah","Hasan"],
    "Department": ["IT", "HR", "IT", "Finance", "HR", "Finance"],
    "Salary": [6000, 5000, 7000, 8000, 5500, 9000]
}
df = pd.DataFrame(employees)

print(df)

print("=== Rata-rata gaji tiap departemen (Average Salary) ===")
print(df.groupby("Department")["Salary"].mean())

print("=== Total gaji tiap departemen (Total Salary) ===")
print(df.groupby("Department")["Salary"].sum())

print("=== Gaji tertinggi tiap departemen (Max Salary) ===")
print(df.groupby("Department")["Salary"].max())

print("=== Gaji terendah tiap departemen (Min Salary) ===")
print(df.groupby("Department")["Salary"].min())

print("=== Jumlah karyawan tiap departemen (Count of Employees) ===")
print(df.groupby("Department")["Name"].count())

print("=== Bonus (Materi yang sering dipakai di dunia kerja) ===")
print(df.groupby("Department")["Salary"].agg(["mean", "max", "min", "sum", "count"]))
