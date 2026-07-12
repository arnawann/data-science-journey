import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv("03- Pandas/data/sales_data.csv")

df["Revenue"] = df["Price"] * df["Quantity"]

sns.lineplot(
    data=df,
    x="Product",
    y="Revenue",
    color="green",
    linewidth=3,
    marker="o"
)

plt.xticks(rotation=45)
plt.title("Revenue by Product")
plt.tight_layout()
plt.show()