# 🏠 Real Estate House Price Prediction App

A machine learning-powered web application built with **Streamlit** that predicts house prices in Bengaluru based on:
- Location
- Total square feet
- Number of bathrooms
- Number of BHKs (bedrooms)

This project showcases skills in:
- Data cleaning & preprocessing
- Feature engineering
- Building and saving ML pipelines
- Interactive UI development with Streamlit

---

## 📁 Project Structure

```
├── app.py                      # Streamlit UI logic
├── house_price_model.pkl       # Saved pipeline (preprocessing + model)
├── Bengaluru_House_Data.csv    # Raw dataset used for training
├── requirements.txt            # Python dependencies
└── README.md
```

---

## 📊 Dataset

- **Source:** [Kaggle - Bengaluru House Price Data](https://www.kaggle.com/datasets/amitabhajoy/bengaluru-house-price-data)
- Cleaned to remove nulls, encode categorical variables, and remove outliers.

---

## 🧠 Model

- **Algorithm:** `DecisionTreeRegressor`
- **Features:** `location`, `total_sqft`, `bath`, `BHK`
- **Pipeline includes:**
  - `OneHotEncoder` for location
  - `StandardScaler` for numerical features

---

## 💡 Features

- Live price prediction for properties
- Easy dropdowns and numeric inputs
- Uses real data for Bengaluru locations
