print("===== Personal Information =====")
name = input("What is your name?")
city = input("Where do you live?")
dream_salary = int(input("How many your dream salary?"))
age = int(input("How old are you?"))
print(f"Hello!, {name}!")
print(f"You live in {city} city.")
print(f"Your dream salary is Rp{dream_salary}")
if dream_salary > 20000000:
    print("Great ambition!")
else:
    print("Keep improving your skills!")
if age >= 17:
    print("You are eligible for a driver's license.")
else:
    print("You are too young.")
