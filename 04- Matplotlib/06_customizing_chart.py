import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv("03- Pandas/data/sales_data.csv")

df["Revenue"] = df["Price"] * df["Quantity"]

plt.figure(figsize=(10,5))

plt.bar(
    df["Product"],
    df["Revenue"],
    color="blue", # warna batang
    edgecolor="black" # garis tepi
)

plt.title("Revenue by Product", fontsize=16)

plt.xlabel("Product", fontsize=12)

plt.ylabel("Revenue (Rp)", fontsize=12)

plt.xticks(rotation=45)

plt.grid(axis="y") # garis bantu horizontal

plt.tight_layout()

plt.show()