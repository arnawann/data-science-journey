import pandas as pd
students ={
    "Name": ["Ali", "Ahmad","Sarah", "Fatimah","Hasan"],
    "Age": [20,21,19,22,18],
    "Score": [85,90,90,95,85]
}
df = pd.DataFrame(students)
print(df)

print("Urutan siswa yang nilainya sama disesuaikan dengan alfabet.")
print(df.sort_values(by=["Score", "Name"], ascending=[False, True]))