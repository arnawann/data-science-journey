import pandas as pd

print("=== Tabel Mahasiswa ===")
students = {
    "StudentID": [1, 2, 3, 4],
    "Name": ["Alice", "Bob", "Charlie", "David"]
}

print("=== Tabel Nilai ===")
scores = {
    "StudentID": [1,2,3,4],
    "Score": [90,85,95,88]
}

df_students = pd.DataFrame(students)
print(df_students)
df_scores = pd.DataFrame(scores)
print(df_scores)

merged = pd.merge(df_students, df_scores, on="StudentID")
print(merged)

print("=== Contoh Lain ===") 

employees = {
    "ID": [1,2,3],
    "Name": ["Ali","Sarah","Ahmad"]
}

departments = {
    "ID": [1,2,3],
    "Department": ["IT","HR","Finance"]
}

employee = pd.DataFrame(employees)
department = pd.DataFrame(departments)

print(pd.merge(employee, department, on="ID"))
