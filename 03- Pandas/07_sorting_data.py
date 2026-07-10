print("=== Original Data ===")

import pandas as pd
students = {
    "Name": ["Ali", "Ahmad","Sarah", "Fatimah","Hasan"],
    "Age": [20,21,19,22,18],
    "Score": [85,90,88,95,80]
}
df = pd.DataFrame(students)

print(df)

print("=== Sort by Ascending ===")
print(df.sort_values("Score"))

print("=== Sort by Descending ===")
print(df.sort_values("Score", ascending=False))

print("=== Sort by Age ===")
print(df.sort_values("Age"))

print("=== Sort by Name ===")
print(df.sort_values("Name"))