import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("03- Pandas/data/sales_data.csv")

df["Revenue"] = df["Price"] * df["Quantity"]

sns.scatterplot(
    data=df,
    x="Quantity",
    y="Revenue",
    color="purple",
    s=150,
    marker="o"
)
plt.title("Quantity vs Revenue")
plt.grid(True)
plt.tight_layout()
plt.show()