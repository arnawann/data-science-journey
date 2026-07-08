import numpy as np
numbers = np.array([10,20,30,40,50])
print(numbers)

print("===== NumPy Random =====")

print("+++ Random Integer +++")

numberss = np.random.randint(1,10)
print(numberss)

print("+++ Membuat Banyak Angka+++")
numbers = np.random.randint(1,10,size=5)
print(numbers)

print("+++ Matrix Random +++")
numbers = np.random.randint(1,100,size=(3,4))
print(numbers)

print("+++ Random Decimal +++")
numbers = np.random.rand(5)
print(numbers)

print("+++ Random Matrix Deciml +++")
numbers = np.random.rand(2,3)
print(numbers)

print("+++ Random Choice +++")
colors = ["Red","Blue","Green","Black"]
print(np.random.choice(colors))

print("+++ Random Choice Banyak+++")
print(np.random.choice(colors,size=5))
