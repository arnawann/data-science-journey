import pandas as pd # Scatter Plot
import matplotlib.pyplot as plt

df = pd.read_csv("03- Pandas/data/sales_data.csv")

df["Revenue"] = df["Price"]* df["Quantity"]

plt.figure(figsize=(10,5))

plt.scatter(
    df["Quantity"], 
    df["Revenue"],
    color="purple",
    s=150
)
plt.title("Quantity vs Revenue")
plt.xlabel("Quantity")
plt.ylabel("Revenue")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()