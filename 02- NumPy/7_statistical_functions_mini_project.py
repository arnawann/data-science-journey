import numpy as np

salary = np.array([
    5000,
    7000,
    6500,
    8000,
    10000,
    9000
])

print("Salary:", salary)
print("Average:", np.mean(salary))
print("Highest:", np.max(salary))
print("Lowest:", np.min(salary))
print("Total:", np.sum(salary))
print("Median:", np.median(salary))
print("Std:", np.std(salary))
