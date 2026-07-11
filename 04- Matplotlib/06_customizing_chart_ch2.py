import pandas as pd # Line Chart
import matplotlib.pyplot as plt

df = pd.read_csv("03- Pandas/data/sales_data.csv")

df["Revenue"] = df["Price"] * df["Quantity"]

plt.figure(figsize=(10,5)) 

plt.plot(
    df["Product"], 
    df["Revenue"],
    color="Red",
    marker="o",
    linewidth=3
)

plt.title("Revenue by Product", fontsize=18)
plt.xlabel("Product", fontsize=12)
plt.ylabel("Revenue", fontsize=12)

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()
