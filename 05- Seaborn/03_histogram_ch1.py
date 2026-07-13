import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("03- Pandas/data/sales_data.csv")

df["Revenue"] = df["Price"] * df["Quantity"]

sns.histplot(
    data=df,
    x="Quantity",
    color="orange",
    bins=6
)

plt.title("Distribution of Quantity")

plt.tight_layout()
plt.show()