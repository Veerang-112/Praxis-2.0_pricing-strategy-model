import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error

# ----------------------------
# 1. Load Dataset
# ----------------------------
df = pd.read_csv("pricing_dataset.csv")

# Clean column names
df.columns = df.columns.str.strip()

# ----------------------------
# 2. Data Cleaning
# ----------------------------

# Remove ₹ and commas from price columns
df["discounted_price"] = df["discounted_price"].str.replace("₹", "").str.replace(",", "").astype(float)
df["actual_price"] = df["actual_price"].str.replace("₹", "").str.replace(",", "").astype(float)

# Remove % from discount column
df["discount_percentage"] = df["discount_percentage"].str.replace("%", "").astype(float)

# Convert rating and rating_count
df["rating"] = pd.to_numeric(df["rating"], errors="coerce")
df["rating_count"] = df["rating_count"].str.replace(",", "").astype(float)

# Drop missing values
df = df.dropna(subset=["discounted_price", "actual_price", "discount_percentage", "rating", "rating_count"])

# ----------------------------
# 3. Feature Engineering
# ----------------------------

# Profit margin
df["profit_margin"] = df["discounted_price"] - df["actual_price"]

# Demand Proxy (using rating_count)
df["demand"] = df["rating_count"]

# ----------------------------
# 4. Feature Selection
# ----------------------------

features = [
    "discounted_price",
    "actual_price",
    "discount_percentage",
    "rating",
    "profit_margin"
]

X = df[features]
y = df["demand"]

# ----------------------------
# 5. Train Test Split
# ----------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ----------------------------
# 6. Train Model
# ----------------------------

model = RandomForestRegressor(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

# ----------------------------
# 7. Evaluation
# ----------------------------

preds = model.predict(X_test)

print("R2 Score:", r2_score(y_test, preds))
print("RMSE:", np.sqrt(mean_squared_error(y_test, preds)))

# ----------------------------
# 8. Save Model
# ----------------------------

joblib.dump(model, "demand_model.pkl")

print("✅ Model trained and saved as demand_model.pkl")
