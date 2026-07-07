print("===== PERSONAL PROFILE =====")

print("===== Syarat 1 — Input =====")
print("===== Syarat 3 — Function =====")

def greeting(name):
    print("Hello,", name)
name = input("What is your name?")
greeting(name)

print("===== Syarat 2 — Exception Handling =====")

try:
    age = int(input("How old are you?"))
except ValueError:
    print("Please enter numbers only.")

country = input("Where do you live?")

try:
    monthly_salary = int(input("What is your dream monthly salary?"))
except ValueError:
    print("Please enter numbers only.")

print("===== Syarat 3 — Function =====")

def yearly_salary(monthly_salary):
    return monthly_salary * 12
yearly = yearly_salary(monthly_salary)

print("Name:", name)
print("Age:", age)
print("Country:", country)
print("Dream Monthly Salary:", monthly_salary)
print("Your yearly salary: Rp", yearly)


print("Excellent goal!")
print(yearly)

print("===== Syarat 4 — Dictionary =====")

profile = {
    "name": name,
    "age": age,
    "country": country,
    "monthly_salary": monthly_salary,
    "yearly_salary": yearly
}  
for key, value in profile.items():
    print(key, ":", value)

print("===== Syarat 5 — File Handling =====")

with open("profile.txt", "w") as file:
    file.write("Name: " + name + "\n")
    file.write("Age: " + str(age) + "\n")
    file.write("Country: " + country + "\n")
    file.write("Monthly Salary: " + str(monthly_salary) + "\n")
    file.write("Yearly Salary: " + str(yearly) + "\n")

print("===== Syarat 6 — Read File =====")

with open("profile.txt", "r") as file:
    content = file.read()
print(content)

print("===== Syarat 7 — If/Elif/Else =====")

if monthly_salary >= 30000000:
    print("Amazing ambition! 🚀")
elif monthly_salary >= 15000000:
    print("Excellent goal! 💪")
else:
    print("Keep learning and growing! 📚")
