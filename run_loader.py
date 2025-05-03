from src.data_loader import DataLoader

if __name__ == "__main__":
    file_path = "data/AmesHousing.csv"
    loader = DataLoader(file_path)
    df = loader.load_data()

    if not df.empty:
        print(df.head())
    else:
        print("DataFrame is empty.")