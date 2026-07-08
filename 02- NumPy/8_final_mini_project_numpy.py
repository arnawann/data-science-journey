import numpy as np
salary = np.array([

    4500,
    6000,
    7000,
    5500,
    8000,
    9000,
    10000,
    6500,
])

print("==== Salary Analysis ====")

print("Total Salary: ", np.sum(salary), "$")

average_salary = np.mean(salary)
print("Average Salary: ", np.mean(salary), "$")

print("Highest Salary: ", np.max(salary), "$")

print("Lowest Salary: ", np.min(salary), "$")

print("Median Salary: ", np.median(salary), "$")

print("Standard Deviation: ", np.std(salary), "$")

print("Employees Above Average: ", salary[salary > average_salary], "$")

