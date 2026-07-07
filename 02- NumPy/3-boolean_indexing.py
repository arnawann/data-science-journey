print("===== Boolean Indexing =====")

print("+++ Misalnya kita ingin mengambil nilai yang ≥75 +++")

import numpy as np

scores = np.array([75, 80, 60, 95, 88])

print(scores >= 75)

print(scores[scores >= 75])

print("+++ Contoh lain +++")

ages = np.array([15,18,20,13,25,17])
print(ages >=18)

print(ages[ages >=18])

print("===== Challenge 1 =====")
numbers = np.array([10,20,30,40,50])
print(numbers > 25)

print("===== Challenge 2 =====")
numbers = np.array([10,20,30,40,50])
print(numbers[numbers >25])

print("===== Challenge 3 =====")
numbers = np.array([10,20,30,40,50])
print(numbers[numbers <=30])
