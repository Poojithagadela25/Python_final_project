import pandas as pd
import numpy as np
import pickle
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from src.data_loader import DataLoader
from src.logger import Logger

def main():
    # === Load and clean column names ===
    df = DataLoader(r"data\engineered_ameshousing.csv").load_data()
    df.columns = df.columns.str.strip().str.replace(" ", "").str.replace("/", "")

    # === Define selected features ===
    selected_features = [
        "YearBuilt", "OverallQual", "TotalBsmtSF", "GrLivArea",
        "FullBath", "HalfBath", "GarageCars", "GarageArea",
        "TotRmsAbvGrd", "Fireplaces"
    ]

    # === Verify column presence ===
    for col in selected_features + ["SalePrice"]:
        if col not in df.columns:
            raise KeyError(f" Missing column: {col}")
        else:
            print(f" Column found: {col}")

    X = df[selected_features]
    y = df["SalePrice"]

    # === Define models ===
    models = {
        "LinearRegression": LinearRegression(),
        "Ridge": Ridge(),
        "Lasso": Lasso(),
        "DecisionTree": DecisionTreeRegressor(),
        "GradientBoosting": GradientBoostingRegressor()
    }

    logger = Logger().get_logger()
    results = {}
    trained_models = {}

    # === Train/test split ===
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # === Train and evaluate each model ===
    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        r2 = r2_score(y_test, y_pred)
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))  # This is to get RMSE
        mae = mean_absolute_error(y_test, y_pred)
        acc = np.mean(np.abs(y_test - y_pred) <= 0.1 * y_test)

        print(f"\n{name} Performance:")
        print(f"R2: {r2:.4f}")
        print(f"RMSE: {rmse:.2f}")
        print(f"MAE: {mae:.2f}")
        print(f"Accuracy (±10%): {acc:.2%}")

        results[name] = {
            "R2": round(r2, 4),
            "RMSE": round(rmse, 2),
            "MAE": round(mae, 2),
            "Accuracy(±10%)": round(acc * 100, 2)
        }

        trained_models[name] = model
        logger.info(f"{name}: R2={r2:.4f}, RMSE={rmse:.2f}, MAE={mae:.2f}, Accuracy={acc:.2%}")

    # === Shows all model results ===
    perf_df = pd.DataFrame(results).T.sort_values(by="R2", ascending=False)
    print("\n Model Performance Summary:\n", perf_df)

    # === Save best model ===
    best_model_name = perf_df.index[0]
    with open("model/house_price_model.pkl", "wb") as f:
        pickle.dump(trained_models[best_model_name], f)

    print(f"\n Best model '{best_model_name}' saved to model/house_price_model.pkl")

if __name__ == "__main__":
    main()