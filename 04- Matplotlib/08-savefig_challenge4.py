import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("03- Pandas/data/sales_data.csv")

plt.figure(figsize=(6,6))

category = df.groupby("Category")["Quantity"].sum()

plt.pie(
    category,
    labels=category.index,
    autopct="%1.1f%%",
    shadow=True,
    startangle=90

)

plt.title("Quantity tiap kategori")
plt.savefig(
    "04- Matplotlib/pie_chart.pdf"
)
plt.show()