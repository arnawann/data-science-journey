import pandas as pd

students = {
    "Name": ["Ali", "Ahmad", "Sarah", "Fatimah", "Hasan", "Zaid"],
    "Age": [20,21,19,22,18,23],
    "Score": [85,90,88,95,80,91]
}

df = pd.DataFrame(students)

print("=== Head() ===")
print(df.head())

print(df.head(3))

print("=== Tail() ===")
print(df.tail())

print(df.tail(2))
