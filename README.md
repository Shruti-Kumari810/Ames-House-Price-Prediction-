# Ames House Price Prediction App 🏡

A full-stack machine learning web application built to predict residential property prices in Ames, Iowa. This application transitions an exploratory data analysis (EDA) and machine learning model (Ridge Regression) into a production-ready web application using FastAPI for the backend API and Streamlit for the user interface.

---

## 🌟 Features

* **Interactive Frontend:** Built with Streamlit for intuitive feature input selection (sliders, dropdowns, and number inputs).
* **High-Performance REST API:** Built with FastAPI to handle requests, align feature schemas, and serve low-latency predictions.
* **Ridge Regression Model:** Handles 260 numerical and one-hot encoded categorical features trained on the Ames Housing Dataset.
* **Feature Alignment Pipeline:** Automatically aligns user inputs with the model's expected 260-feature input array before inference.

---

## 🛠️ Tech Stack

* **Machine Learning:** Scikit-Learn, Pandas, NumPy, Joblib
* **Backend API:** FastAPI, Uvicorn
* **Frontend Web App:** Streamlit
* **Language & Tools:** Python 3.14, Git, VS Code

---

## 📁 Project Structure

```text
house-price-prediction-app/
│
├── main.py                 # FastAPI backend server handling model predictions
├── app.py                  # Streamlit frontend application interface
├── house_price_model.pkl   # Serialized trained Ridge Regression model
├── model_features.pkl      # Saved feature columns schema (260 features)
├── .gitignore              # Ignored files (virtual environment, cache)
└── README.md               # Project documentation
