import pandas as pd
import logging
from src.logger import Logger 

class DataLoader:
    def __init__(self, file_path: str):
        """
        Initialize DataLoader with the path to the dataset.
        """
        self.file_path = file_path
        self.data = None
        self.logger = Logger().get_logger()

    def load_data(self) -> pd.DataFrame:
        """
        Load data from CSV file, clean column names, and return as a DataFrame.
        """
        try:
            # Load data
            self.data = pd.read_csv(self.file_path)

            # Clean column names
            self.data.columns = (
                self.data.columns
                .str.strip()
                .str.replace(" ", "")
                .str.replace("/", "")
            )

            # Log success message
            self.logger.info(f" Data loaded and cleaned. Shape: {self.data.shape}")
            print(f" Data loaded and cleaned. Shape: {self.data.shape}")
            return self.data

        except FileNotFoundError:
            # Log error if file is not found
            self.logger.error(f" File not found at {self.file_path}")
            print(f" File not found at {self.file_path}")
            return pd.DataFrame()

        except Exception as e:
            # Log any other error that occurs
            self.logger.error(f" Error loading data: {e}")
            print(f" Error loading data: {e}")
            return pd.DataFrame()


# Runs directly for testing
if __name__ == "__main__":
    # Define the path to your dataset
    file_path = "data/cleaned_ameshousing.csv" 

    # Initialize the DataLoader and load the data
    loader = DataLoader(file_path)
    df = loader.load_data()

    # Check if the DataFrame is empty and print the first few rows if it's not
    if not df.empty:
        print(df.head())
    else:
        print(" DataFrame is empty. Please check your file path or contents.")