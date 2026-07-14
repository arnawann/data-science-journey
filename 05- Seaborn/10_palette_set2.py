import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_palette("Set2")

df = pd.read_csv("03- Pandas/data/sales_data.csv")

df["Revenue"] = df["Price"] * df["Quantity"]

plt.figure(figsize=(12,5))

sns.violinplot(
    data=df,
    x="Category",
    y="Revenue",
)

plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue (Rp)")

plt.tight_layout()
plt.show()