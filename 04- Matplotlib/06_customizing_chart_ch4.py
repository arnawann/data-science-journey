import pandas as pd # Histogram
import matplotlib.pyplot as plt

df = pd.read_csv("03- Pandas/data/sales_data.csv")

plt.figure(figsize=(10,5))

plt.hist(
    df["Quantity"],
    color="Orange",
    edgecolor="Black"
)

plt.title("Distribution of Product Quantity")
plt.xlabel("Quantity") 
plt.ylabel("Frequency")

plt.show()