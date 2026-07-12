import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("03- Pandas/data/sales_data.csv")

df["Revenue"] = df["Price"] * df["Quantity"]

plt.figure(figsize=(10,5))

plt.bar(df["Product"], df["Revenue"])

plt.title("Revenue by Product")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    "04- Matplotlib/revenue_chart.pdf",
    dpi=300,
    transparent=True
)

plt.show()