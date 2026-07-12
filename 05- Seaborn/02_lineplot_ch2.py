import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("03- Pandas/data/sales_data.csv")

sns.lineplot(
    data=df,
    x="Product",
    y="Quantity",
    color="red",
    marker="s"
)

plt.xticks(rotation=45)
plt.title("Quantity by Product")
plt.tight_layout()
plt.savefig("05- Seaborn/seaborn_line.png")
plt.show()