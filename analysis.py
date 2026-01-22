import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("pricing_dataset.csv")

# Demand proxy (important hack)
df["demand"] = df["sold_quantity"] / (df["stock"] + 1)

# Price vs Demand
sns.scatterplot(x="final_price", y="demand", data=df)
plt.title("Price vs Demand")
plt.show()

# Category-wise demand
category_demand = df.groupby("category")["demand"].mean().sort_values()
print(category_demand)

# Discount sensitivity
sns.boxplot(x="discount_pct", y="demand", data=df)
plt.title("Discount vs Demand")
plt.show()
