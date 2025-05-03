import pandas as pd
import os
import sys 
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
from src.logger import Logger

class DataCleaner:
    def __init__(self, dataframe: pd.DataFrame):
        """
        Initialize DataCleaner with the loaded DataFrame.
        """
        self.df = dataframe
        self.logger = Logger().get_logger()

    def drop_high_missing_columns(self, threshold: float = 0.5) -> pd.DataFrame:
        """
        Drop columns with missing values greater than the threshold.
        """
        missing_fraction = self.df.isnull().mean()
        cols_to_drop = missing_fraction[missing_fraction > threshold].index
        self.df.drop(columns=cols_to_drop, inplace=True)
        self.logger.info(f" Dropped columns with >{threshold*100}% missing values: {list(cols_to_drop)}")
        return self.df

    def fill_missing_values(self) -> pd.DataFrame:
        """
        Fill missing values (median for numeric, mode for categorical).
        """
        for col in self.df.columns:
            if self.df[col].dtype in ['int64', 'float64']:
                self.df[col].fillna(self.df[col].median(), inplace=True)
            else:
                self.df[col].fillna(self.df[col].mode()[0], inplace=True)
        self.logger.info(" Missing values filled.")
        return self.df

    def clean_data(self) -> pd.DataFrame:
        """
        Full cleaning pipeline.
        """
        self.drop_high_missing_columns()
        self.fill_missing_values()
        self.logger.info(" Data cleaning completed.")
        return self.df

    def save_cleaned_data(self, save_path: str):
        """
        Save the cleaned DataFrame to a CSV file.
        """
        try:
            self.df.to_csv(save_path, index=False)
            self.logger.info(f" Cleaned data saved successfully to {save_path}")
            print(f" Cleaned data saved successfully to {save_path}")
        except Exception as e:
            self.logger.error(f" Failed to save cleaned data: {e}")
            print(f" Failed to save cleaned data: {e}")

# For testing individually
if __name__ == "__main__":
    from src.data_loader import DataLoader

    file_path = "data/AmesHousing.csv"
    loader = DataLoader(file_path)
    df = loader.load_data()

    cleaner = DataCleaner(df)
    cleaned_df = cleaner.clean_data()

    # Save the cleaned data
    cleaner.save_cleaned_data("data/cleaned_ameshousing.csv")

    print(cleaned_df.head())