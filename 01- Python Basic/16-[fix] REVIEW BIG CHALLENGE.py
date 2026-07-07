print("===== PERSONAL PROFILE =====")

def greeting(name):
    print("Hello,", name)
name = input("What is your name?")
greeting(name)

try:
    age = int(input("How old are you?"))
except ValueError:
    print("Please enter numbers only.")

country = input("Where do you live?")

try:
    monthly_salary = int(input("What is your dream monthly salary?"))
except ValueError:
    print("Please enter numbers only.")

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

profile = {
    "name": name,
    "age": age,
    "country": country,
    "monthly_salary": monthly_salary,
    "yearly_salary": yearly
}  
for key, value in profile.items():
    print(key, ":", value)

with open("profile.txt", "w") as file:
    file.write("Name: " + name + "\n")
    file.write("Age: " + str(age) + "\n")
    file.write("Country: " + country + "\n")
    file.write("Monthly Salary: " + str(monthly_salary) + "\n")
    file.write("Yearly Salary: " + str(yearly) + "\n")

if monthly_salary >= 30000000:
    print("Amazing ambition! 🚀")
elif monthly_salary >= 15000000:
    print("Excellent goal! 💪")
else:
    print("Keep learning and growing! 📚")
