import pandas as pd
students ={
    "Name": ["Ali", "Ahmad","Sarah", "Fatimah","Hasan"],
    "Age": [20,21,19,22,18],
    "Score": [85,90,88,95,80]
}
df = pd.DataFrame(students)
print(df)

print("=== Challenge 1 loc ===")
print(df.loc[2])

print("=== Challenge 2 iloc ===")
print(df.iloc[2])

print("=== Challenge 3 loc ===")
print(df.loc[3, "Name"])

print("=== Challenge 4 iloc ===")
print(df.iloc[1, 2])

print("=== Challenge 5 loc ===")
print(df.loc[:, ["Name", "Score"]])

print("=== Challenge 5 iloc ===")
print(df.iloc[:, [0, 2]])