import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("03- Pandas/data/sales_data.csv")

df["Revenue"] = df["Price"] * df["Quantity"]

sns.lineplot(
    data=df,
    x="Product",
    y="Revenue",
    color="red",
    linewidth=3,
    marker="o"
)

plt.xticks(rotation=45)

plt.title("Revenue by Product")

plt.grid(True)

plt.tight_layout()

plt.show()