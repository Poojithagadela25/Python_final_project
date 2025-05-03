import pandas as pd
import pickle
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Load the full engineered dataset
df = pd.read_csv("data/engineered_ameshousing.csv")

# We'll use just these 10 key features for simplicity
selected_features = [
    "YearBuilt", "OverallQual", "TotalBsmtSF", "GrLivArea",
    "FullBath", "HalfBath", "GarageCars", "GarageArea",
    "TotRmsAbvGrd", "Fireplaces"
]

X = df[selected_features]
y = df["SalePrice"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = GradientBoostingRegressor()
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)

# Calculate R2 score and RMSE
r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5  # Calculate RMSE manually by taking the square root of MSE

print(f"R2 Score: {r2:.4f}")
print(f"RMSE: {rmse:.2f}")

# Save model
with open("model/house_price_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved using 10 features.")