import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("03- Pandas/data/sales_data.csv")

df["Revenue"] = df["Price"] * df["Quantity"]

plt.figure(figsize=(12,5))

plt.scatter(df["Quantity"], df["Revenue"], color="purple", s=150)

plt.xlabel("Quantity")

plt.ylabel("Revenue")

plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(
    "04- Matplotlib/scatter.png",
    dpi=300
)
plt.show()