import pandas as pd
from src.logger import Logger

class FeatureEngineer:
    def __init__(self, dataframe: pd.DataFrame):
        """
        Initialize FeatureEngineer with the cleaned DataFrame.
        """
        self.df = dataframe
        self.logger = Logger().get_logger()

    def create_new_features(self) -> pd.DataFrame:
        """
        Create new meaningful features:
        - TotalBathrooms = FullBath + HalfBath*0.5 + BsmtFullBath + BsmtHalfBath*0.5
        - HouseAge = YrSold - YearBuilt
        - Remodeled = 1 if YearBuilt != YearRemodAdd, else 0
        """
        try:
            self.df['TotalBathrooms'] = (
                self.df['FullBath'] + 0.5 * self.df['HalfBath'] +
                self.df['BsmtFullBath'] + 0.5 * self.df['BsmtHalfBath']
            )
            self.df['HouseAge'] = self.df['YrSold'] - self.df['YearBuilt']
            self.df['Remodeled'] = (self.df['YearBuilt'] != self.df['YearRemodAdd']).astype(int)

            self.logger.info(" New features created: TotalBathrooms, HouseAge, Remodeled.")
        except Exception as e:
            self.logger.error(f" Error creating new features: {e}")

        return self.df

    def encode_categorical(self) -> pd.DataFrame:
        """
        Encode all categorical variables using One-Hot Encoding.
        """
        try:
            categorical_cols = self.df.select_dtypes(include=["object"]).columns.tolist()
            self.df = pd.get_dummies(self.df, columns=categorical_cols, drop_first=True)
            self.logger.info(f" All categorical columns one-hot encoded: {categorical_cols}")
        except Exception as e:
            self.logger.error(f" Error encoding categorical variables: {e}")

        return self.df

    def feature_engineering(self) -> pd.DataFrame:
        """
        Full feature engineering pipeline:
        - Create new features
        - Encode categorical variables
        """
        self.create_new_features()
        self.encode_categorical()
        self.logger.info(" Feature engineering completed.")
        return self.df

    def save_engineered_data(self, save_path: str):
        """
        Save the feature engineered DataFrame to a CSV file.
        """
        try:
            self.df.to_csv(save_path, index=False)
            self.logger.info(f" Feature engineered data saved successfully to {save_path}")
            print(f" Feature engineered data saved successfully to {save_path}")
        except Exception as e:
            self.logger.error(f" Failed to save feature engineered data: {e}")
            print(f"Failed to save feature engineered data: {e}")

# ----------------------------------------------------------------
# For direct testing if you want to run this file alone
if __name__ == "__main__":
    from src.data_loader import DataLoader

    # Load CLEANED data (not raw!)
    file_path = "data/cleaned_ameshousing.csv"
    loader = DataLoader(file_path)
    cleaned_df = loader.load_data()

    # Perform feature engineering
    fe = FeatureEngineer(cleaned_df)
    engineered_df = fe.feature_engineering()

    # Save the engineered dataset
    fe.save_engineered_data("data/engineered_ameshousing.csv")

    print(engineered_df.head())