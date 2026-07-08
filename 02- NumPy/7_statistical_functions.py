print("=== NumPy Statistical Functions ===")

import numpy as np
scores = np.array([80,75,90,100,85])

print("=== Mean ===")
print(np.mean(scores))

print("=== Sum ===")
print(np.sum(scores))

print("=== Max ===")
print(np.max(scores))

print("=== Min ===")
print(np.min(scores))

print("=== Median ===")
print(np.median(scores))

scores = np.array([70,10,90,100])
print(np.median(scores))

print("=== Standard Deviation ===")
print(np.std(scores))
