import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("03- Pandas/data/sales_data.csv")
df["Revenue"] = df["Price"] * df["Quantity"]

g = sns.pairplot(
    df[["Price", "Quantity", "Revenue"]],
    diag_kind="kde"
)
g.savefig("05- Seaborn/seaborn_pairplot.png")
plt.show()