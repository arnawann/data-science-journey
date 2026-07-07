try:
    first_number = int(input("First Number:"))
    second_number = int(input("Second Number:"))
    result = first_number + second_number
    print("Result:", result)

except ValueError:
    print("Please enter valid numbers.")
