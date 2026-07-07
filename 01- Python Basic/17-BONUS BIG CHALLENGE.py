employees = []

def add_employee():
    name = input("Employee Name:")
    age = int(input("Age:"))
    country = input("Country:")
    position = input("Position:")
    monthly_salary = int(input("Monthly Salary:"))

    employee = {
        "name": name,
        "age": age,
        "country": country,
        "position": position,
        "monthly_salary": monthly_salary,
    }
    employees.append(employee)        
    print("Employee added successfully!")
    
def show_employees():
    for employee in employees:
        print("Name:", employee["name"])
        print("Age:", employee["age"])
        print("Country:", employee["country"])
        print("Position:", employee["position"])
        print("Monthly Salary:", employee["monthly_salary"])
        print("-" * 30)

def search_employee():
    search_name = input("Search Employee:")
    found = False
    for employee in employees:
        if employee["name"].lower() == search_name.lower():
            print("Employee Name:", employee["name"])
            print("Age:", employee["age"])
            print("Country:", employee["country"])
            print("Position:", employee["position"])
            print("Monthly Salary:", employee["monthly_salary"])
            print("-" * 30)
            found = True
    if not found:
            print("Employee not found.")

def calculate_average():
    total = 0
    for employee in employees:
        total += employee["monthly_salary"]
    average_salary = total / len(employees)
    print("===== Statistics =====")
    print("Total Employees:", len(employees))
    print("Total Salary:", total, "$")
    print("Average Salary:", int(average_salary), "$")
    print("-" * 30)

def save_file():
    with open("employees.txt", "w") as file:
        for employee in employees:
            file.write("Name:" + employee["name"] + "\n")
            file.write("Age:" + str(employee["age"]) + "\n")
            file.write("Country:" + employee["country"] + "\n")
            file.write("Position:" + employee["position"] + "\n")
            file.write("Monthly Salary:" + str(employee["monthly_salary"]) + "\n")

while True:
    print("===== Salary Management =====")

    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Statistics")
    print("5. Save to File")
    print("0. Exit")

    choice = input("Choose menu:")

    if choice == "1":
        add_employee()
    elif choice == "2":
        show_employees()
    elif choice == "3":
        search_employee()
    elif choice == "4":
        calculate_average()
    elif choice == "5":
        save_file()
        print("Employees saved succesfully!")
    elif choice == "0":
        print("Thank you!")
        break
    else:
        print("Invalid menu.")

