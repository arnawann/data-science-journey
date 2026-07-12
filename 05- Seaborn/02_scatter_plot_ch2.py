import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("03- Pandas/data/sales_data.csv")

df["Revenue"] = df["Price"] * df["Quantity"]

sns.scatterplot(
    data=df,
    x="Price",
    y="Revenue",
    color="orange",
    marker="D"
)
plt.title("Price vs Revenue")
plt.grid(True)
plt.tight_layout()
plt.savefig("05- Seaborn/seaborn_scatter.png")
plt.show()