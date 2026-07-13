import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("03- Pandas/data/sales_data.csv")

df["Revenue"] = df["Price"] * df["Quantity"]

sns.boxplot(
    data=df,
    y="Revenue",
    color="green"
)

plt.title("Distribution of Product Prices")

plt.show()
