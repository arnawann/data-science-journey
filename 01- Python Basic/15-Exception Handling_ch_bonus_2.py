try:
    first_number = int(input("First Number:"))
    second_number = int(input("Second Number:"))
    addition = first_number + second_number
    division = first_number / second_number
    print("Addition:", addition)
    print("Division:", division)

except ValueError:
    print("Please enter valid numbers.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
