print("===== Multiple Conditions (AND & OR) =====")

import numpy as np
scores = np.array([60, 75, 80, 90, 55])
print(scores)

print("+++ mencari nilai di atas 70. +++")
print(scores > 70)

print("+++ mencari nilai di bawah 90. +++")
print(scores > 90)

print("+++ mencari nilai lebih dari 70 DAN kurang dari 90. +++")
print((scores > 70) & (scores <90))

print("===== CH 1 =====")
ages = np.array([15,18,22,39,45])
print(ages[(ages <18) | (ages >30)])

print("===== CH 2 =====")
ages = np.array([15,18,22,39,45])
print(ages[(ages <18) & (ages >30)])

print("===== CH 3 =====")
salary = np.array([5,8,10,15,20])
print(salary[(salary >=18) & (salary <20)])
