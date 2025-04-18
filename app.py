import streamlit as st
import pandas as pd
import joblib

model = joblib.load('house_price_model.pkl')

# Load the exact same cleaned dataset used in training
@st.cache_data
def load_cleaned_locations():
    df = pd.read_csv("Bengaluru_House_Data.csv")
    df.drop(['society', 'balcony', 'availability'], axis=1, inplace=True)
    df.dropna(inplace=True)
    df['BHK'] = df['size'].apply(lambda x: int(x.split(' ')[0]) if isinstance(x, str) else None)
    df.dropna(inplace=True)

    def convert_sqft_to_num(x):
        try:
            return float(x)
        except:
            if '-' in str(x):
                tokens = x.split('-')
                return (float(tokens[0]) + float(tokens[1])) / 2
            return None

    df['total_sqft'] = df['total_sqft'].apply(convert_sqft_to_num)
    df.dropna(inplace=True)
    df = df[df['total_sqft'] / df['BHK'] >= 300]
    df = df[df['bath'] < df['BHK'] + 2]
    return sorted(df['location'].unique().tolist())

# Extract exact training-time location values
locations = load_cleaned_locations()

# Streamlit UI
st.title("🏡 Bangalore House Price Prediction")
st.markdown("Enter property details to estimate the market price.")

# Input fields
location = st.selectbox("Location", locations)
total_sqft = st.number_input("Total Square Feet Area", min_value=300, max_value=10000, step=10)
bath = st.selectbox("Bathrooms", [1, 2, 3, 4, 5])
bhk = st.selectbox("BHK (Bedrooms)", [1, 2, 3, 4, 5])

# Predict
if st.button("Predict Price"):
    input_data = pd.DataFrame([[location, total_sqft, bath, bhk]],
                              columns=['location', 'total_sqft', 'bath', 'BHK'])
    try:
        prediction = model.predict(input_data)[0]
        st.success(f"🏷️ Estimated Price: ₹ {prediction * 1e5:,.0f}")
    except Exception as e:
        st.error(f"❌ Prediction failed: {e}")
