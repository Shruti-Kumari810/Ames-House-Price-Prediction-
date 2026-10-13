from fastapi import FastAPI
from pydantic import BaseModel
import joblib 
import pandas as pd

app = FastAPI(title = "House Price Prediction API")

model = joblib.load("house_price_model.pkl")
model_features = joblib.load("model_features.pkl")

class HouseInput(BaseModel):
    OverallQual: int
    GrLivArea: float
    GarageCars: int
    TotalBsmtSF: float
    FullBath: int
    YearBuilt: int
    Neighborhood: str

@app.get("/")
def home():
    return {"message" : "House Price Prediction API is active!!!"}

@app.post("/predict")
def predict_price(data : HouseInput):
    input_dict = data.dict()

    df_input = pd.DataFrame(columns = model_features)
    df_input.loc[0] = 0 

    for key , value in input_dict.items():
        if key in df_input.columns:
            df_input.at[0, key] = value 

    neighborhood_col = f"Neighborhood_{input_dict.get('Neighborhood')}"
    if neighborhood_col in df_input.columns:
        df_input.at[0 , neighborhood_col ] = 1

    prediction = model.predict(df_input)

    return {"predicted_sale_price" : round(float(prediction[0]),2)}