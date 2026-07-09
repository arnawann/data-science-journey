import pandas as pd

product = {
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer", "Webcam"],
    "Price": [15000,500,1200,3500,2500,800]
}

df = pd.DataFrame(product)

print("=== Seluruh Tabel ===")
print(df)

print("=== Head(3) ===")
print(df.head(3))

print("=== Tail(2) ===")
print(df.tail(2))
