import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("03- Pandas/data/sales_data.csv")

sns.histplot(
    data=df,
    x="Price",
    color="green",
    bins=8,
    kde=True

)

plt.title("Distribution of Product Prices")

plt.tight_layout()

plt.show()