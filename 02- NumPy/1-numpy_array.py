print("===== Array =====")

import numpy as np
numbers = np.array([10, 20, 30, 40, 50])
print(numbers)

print(type(numbers))

import numpy as np
numbers = np.array([10,20,30])
print(numbers / 5)

import numpy as np
a = np.array([1,2,3])
b = np.array([10,20,30])
print(a+b)

import numpy as np
print(a*b)

print("===== Mini Challenge 1 =====")

import numpy as np
prices = np.array([1000,2500,3000,5000])
print("Prices:", prices)
new_prices = prices * 1.1
print("New Prices:", new_prices)

print("===== Tantangan Bonus =====")

prices = np.array([1000,2500,3000,5000])
print("Prices:", prices)
prices_plus_tax = prices * 1.1
print("Prices + Tax 10%:", prices_plus_tax)
final_prices = prices_plus_tax - 500
print("Final Prices:", final_prices)
