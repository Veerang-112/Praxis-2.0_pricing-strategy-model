import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor

df = pd.read_csv("pricing_dataset.csv")

# ---- Feature Engineering ----
df["demand"] = df["sold_quantity"] / (df["stock"] + 1)

features = [
    "final_price",
    "discount_pct",
    "rating",
    "num_reviews",
    "delivery_time_min",
    "profit_margin_pct",
    "weight_g",
    "shelf_life_days"
]

df = df.dropna(subset=features + ["demand"])

X = df[features]
y = df["demand"]

# ---- Train Model ----
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = XGBRegressor(
    n_estimators=300,
    learning_rate=0.05,
    max_depth=5,
    subsample=0.8
)

model.fit(X_train, y_train)

# ---- Elasticity Calculation ----
def price_elasticity(model, base_row, delta=0.05):
    base_price = base_row["final_price"]
    base_demand = model.predict(pd.DataFrame([base_row]))[0]

    base_row["final_price"] = base_price * (1 + delta)
    new_demand = model.predict(pd.DataFrame([base_row]))[0]

    elasticity = ((new_demand - base_demand) / base_demand) / delta
    return elasticity

# Save model
import joblib
joblib.dump(model, "demand_model.pkl")
