
import numpy as np
numbers = np.array([10,20,30,40,50])
print(numbers)

numberss = np.array([
    [1,2,3],
    [4,5,6]
])
print(numberss)

matrix = np.array([
    [1,2],
    [3,4],
    [5,6]
])
print(matrix)

print("===== Tuple =====")

print(numbers.shape)

print("===== Shape =====")

print(numberss.shape)


print("===== Dimension =====")

print(numbers.ndim)
print(numberss.ndim)

print("===== Size =====")

print(numbers.size)
print(numberss.size)
print(matrix.size)

print("===== Reshape =====")

angka = np.array([1,2,3,4,5,6])
print(angka.reshape(2,3))
print(angka.reshape(3,2))

print("+++++ CH1 +++++")

a = np.array([10,20,30,40])
print(a.shape)

print("+++++ satu latihan terakhir +++++")

x = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90],
    [100,110,120],
])
print(x.shape)
print(x.ndim)
print(x.size)
