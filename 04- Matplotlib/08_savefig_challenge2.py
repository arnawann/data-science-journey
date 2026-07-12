import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("03- Pandas/data/sales_data.csv")

df["Revenue"] = df["Price"] * df["Quantity"]

plt.figure(figsize=(12,5))

plt.plot(
    df["Product"],
    df["Revenue"],
    color="red",
    marker="o"
)

plt.title("Revenue by Product")

plt.xlabel("Product")

plt.ylabel("Revenue (Rp)")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig(
    "04- Matplotlib/revenue_line.jpg"
)
plt.show()