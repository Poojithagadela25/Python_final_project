# House Price Prediction using Machine Learning

This project predicts house prices based on key features extracted from the AmesHousing dataset using a full machine learning pipeline in Python.

## Project Overview

This is an end-to-end pipeline that includes:

- *Data Ingestion* from raw CSV
- *Data Cleaning* (handling missing values, dropping high-null columns)
- *Feature Engineering* (encoding, transformations)
- *Model Training* (Gradient Boosting and others)
- *Model Evaluation* (R2, RMSE, MAE, Accuracy within 10%)
- *API Deployment* using FastAPI
- *Interactive Frontend* to test predictions

##  Data Cleaning

- Dropped columns with more than 50% missing values.  
- Filled numerical missing values with **median**.  
- Filled categorical values with **mode**.  

##  Exploratory Data Analysis (EDA)

- Visualizations of correlation, price distributions, and outliers.  
- Key features identified: `OverallQual`, `GrLivArea`, `GarageArea`, `YearBuilt`.  

##  Model Training

- **Algorithm:** Gradient Boosting Regressor  
- **Features Used:** Top 10 based on correlation and EDA  
- **Validation:** 80/20 train-test split  

##  Evaluation Metrics

- **R² Score:** 0.8839  
- **RMSE:** 30,500  

##  Deployment

- A FastAPI-based web API loads the trained model (`.pkl`) and provides predictions on new data.

##  Challenges

- Handling missing data while preserving useful information.  
- Feature selection from over 80 attributes.  
- Modular coding for team collaboration.  

##  Future Improvements

- Hyperparameter tuning for improved performance.  
- User authentication on the frontend.  
- Cloud deployment for scalable predictions.  

 ## end  --

