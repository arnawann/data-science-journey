def say_hello(name):
    print("Hello,", name)
def calculate_age(age):
    print("Next year you will be", age + 1, "years old.")
def monthly_to_yearly(salary):
    return salary * 12

name = input("What is your name? ")
age = int(input("How old are you? "))
salary = int(input("What is your dream monthly salary? "))

say_hello(name)
calculate_age(age)

yearly_salary = monthly_to_yearly (salary)

print("Your yearly salary is Rp", yearly_salary)
