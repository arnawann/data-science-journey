import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("03- Pandas/data/sales_data.csv")

df["Revenue"] = df["Price"] * df["Quantity"]

sns.histplot(
    data=df,
    x="Revenue",
    color="purple",
    kde=True
)

plt.title("Distribution of Revenue")
plt.tight_layout()
plt.savefig("05- Seaborn/seaborn_histogram.png")
plt.show()