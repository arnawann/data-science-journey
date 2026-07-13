import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("03- Pandas/data/sales_data.csv")
df["Revenue"] = df["Price"] * df["Quantity"]

sns.pairplot(
    df,
    vars=["Price", "Quantity", "Revenue"],
    hue="Category",
    diag_kind="hist"
)
plt.show()