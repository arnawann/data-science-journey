#suruh bandingin sama barplot, btw yg di sini matplotlib
import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv("03- Pandas/data/sales_data.csv")

plt.bar(
   df["Product"],
   df["Quantity"] 
)

plt.xticks(rotation=45)
plt.savefig("matplotlib_bar.png")
plt.show()