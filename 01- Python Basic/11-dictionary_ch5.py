print("===== DICTIONARY + LOOP PART 2 =====")
    
profile = {
    "name": "Arnawan",
    "age": 24,
    "dream_salary": 20000000
}

print("Name:", profile["name"])
print("Age:", profile["age"])
print("Dream Salary: Rp", profile["dream_salary"])

for key, value in profile.items():
    print(key, ":", value)
