import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("03- Pandas/data/sales_data.csv")

df["Revenue"] = df["Price"] * df["Quantity"]

sns.barplot(
    data=df,
    x="Product",
    y="Revenue"
)

plt.xticks(rotation=45)
plt.savefig("05- Seaborn/seaborn_bar.png")
plt.show()