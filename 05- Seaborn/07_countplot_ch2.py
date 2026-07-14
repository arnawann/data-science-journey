import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("03- Pandas/data/sales_data.csv")

df["Revenue"] = df["Price"] * df["Quantity"]

sns.countplot(
    data=df,
    x="Category",
    color="orange",
)

plt.title("Total Products by Category")
plt.grid(axis='y')

plt.show()