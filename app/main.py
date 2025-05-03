from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import pickle
import numpy as np
from fastapi import Request

app = FastAPI()

# Load the trained model
with open("model/house_price_model.pkl", "rb") as f:
    model = pickle.load(f)

templates = Jinja2Templates(directory="app/templates")  

# Root endpoint to serve the HTML page
@app.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Define the input model for the house features
class HouseFeatures(BaseModel):
    YearBuilt: int
    OverallQual: int
    TotalBsmtSF: float
    GrLivArea: float
    FullBath: int
    HalfBath: int
    GarageCars: int
    GarageArea: float
    TotRmsAbvGrd: int
    Fireplaces: int

# Define a prediction endpoint
@app.post("/predict")
def predict(features: HouseFeatures):
    data = np.array([[
        features.YearBuilt,
        features.OverallQual,
        features.TotalBsmtSF,
        features.GrLivArea,
        features.FullBath,
        features.HalfBath,
        features.GarageCars,
        features.GarageArea,
        features.TotRmsAbvGrd,
        features.Fireplaces
    ]])

    prediction = model.predict(data)
    return {"PredictedPrice": prediction[0]}