print("===== Dictionary + Loop =====")
student = {
    "name": "Arnawan",
    "age": 24,
    "country": "Indonesia",
    "career": "Data Scientist"
}

print("Name:", student["name"])
print("Age:", student["age"])
print("Country:", student["country"])
print("Career:", student["career"])

for key, value in student.items():
    print(key, ":", value)
