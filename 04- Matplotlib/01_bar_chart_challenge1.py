import matplotlib.pyplot as plt

print("=== Challenge 1 ===")

Products = ("Phone", "Tablet", "Laptop", "Camera", "Printer")

Sales = (80,40,60,30,20)

plt.bar(Products,Sales)

plt.title("Electronic Product Sales")

plt.xlabel("Products")

plt.ylabel("Total Sold")

plt.show()