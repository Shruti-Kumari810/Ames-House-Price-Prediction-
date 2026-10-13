import streamlit as st 
import requests

st.set_page_config(page_title = "house Price Predictor", page_icon = "🏠", layout = "centered")

st.title("Ames House Price Predictor 🏠")
st.write("Enter the specification of the house below to estimate its market value instantly..")

col1 , col2 = st.columns(2)

with col1:
    overall_qual = st.slider("Overall Quality (1-10)" , min_value = 1 , max_value = 10 , value = 6)
    gr_liv_area = st.number_input("Above Ground Living Area (sq ft)", min_value=300, max_value=5000, value=1500)
    garage_cars = st.selectbox("Garage Capacity (Cars)", [0, 1, 2, 3, 4], index=2)

with col2:
    total_bsmt_sf = st.number_input("Total Basement Area (sq ft)", min_value=0, max_value=3000, value=800)
    full_bath = st.selectbox("Full Bathrooms", [1, 2, 3, 4], index=1)
    year_built = st.number_input("Year Built", min_value=1800, max_value=2026, value=2005)

neighborhood = st.selectbox("Neighborhood", [
    "CollgCr", "Veenker", "Crawfor", "NoRidge", "Mitchel", "Somerst", 
    "NWAmes", "OldTown", "BrkSide", "Sawyer", "NridgHt", "NAmes"
])

if st.button("Predict House Price", type="primary"):
    payload = {
        "OverallQual": overall_qual,
        "GrLivArea": gr_liv_area,
        "GarageCars": garage_cars,
        "TotalBsmtSF": total_bsmt_sf,
        "FullBath": full_bath,
        "YearBuilt": year_built,
        "Neighborhood": neighborhood
    }
    
    try:
        # Request prediction from FastAPI backend
        response = requests.post("http://127.0.0.1:8000/predict", json=payload)
        
        if response.status_code == 200:
            result = response.json()
            predicted_price = result["predicted_sale_price"]
            st.success(f"Estimated House Price: **${predicted_price:,.2f}**")
        else:
            st.error("Error communicating with the prediction backend.")
    except Exception as e:
        st.error(f"Could not connect to FastAPI server. Make sure it is running! Error: {e}")