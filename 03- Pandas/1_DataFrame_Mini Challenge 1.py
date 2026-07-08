import pandas as pd

students = {
    
    "Name": ["Arnawan", "Aisyah", "Hasan"],
    "Age": [24,22,21],
    "City": ["Depok", "Jakarta", "Bandung"]
}

df = pd.DataFrame(students)

print(df)
