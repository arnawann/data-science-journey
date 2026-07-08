import pandas as pd

print("Dictionary (key -> value) dirubah menjadi tabel")

students = {
    "Name": ["Alii", "Ahmad", "Sarah", "Fatimah"],
    "Age": [20,21,19,22],
    "Score": [85,90,88,95]
}

df = pd.DataFrame(students)

print(df)
