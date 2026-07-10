import pandas as pd

things = {
    "Name": ["Cupboard", "Table", "Chair", "Sofa", "Bed"],
    "Price": [100, 200, 150, 300, 250],
    "Age": [10, 5, 20, 2, 8]
}
df = pd.DataFrame(things)
print(df)

print("=== Challenge 1: Sort by Price (Descending) ===")
print(df.sort_values("Price", ascending=False))

print("=== Challenge 2: Sort by Age Old-to-New ===")
print(df.sort_values("Age", ascending=False))

print("=== Challenge 3: Sort by Name Z-A ===")
print(df.sort_values("Name", ascending=False))

print("=== Challenge 4: Add New Column ===")
df["City"] = ["Depok", "Jakarta", "Bandung", "Bogor", "Bekasi"]
print(df.sort_values("City"))


