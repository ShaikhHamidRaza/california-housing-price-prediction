import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("housing_model.pkl")

st.title("California Housing Price Prediction")

st.write("Enter housing features to predict house price")

MedInc = st.number_input("Median Income")
HouseAge = st.number_input("House Age")
AveRooms = st.number_input("Average Rooms")
AveBedrms = st.number_input("Average Bedrooms")
Population = st.number_input("Population")
AveOccup = st.number_input("Average Occupancy")
Latitude = st.number_input("Latitude")
Longitude = st.number_input("Longitude")

if st.button("Predict Price"):

    # Feature Engineering
    rooms_per_household = AveRooms / AveOccup
    bedrooms_per_room = AveBedrms / AveRooms
    population_per_household = Population / AveOccup

    # 11 features for the trained model
    features = np.array([[
        MedInc,
        HouseAge,
        AveRooms,
        AveBedrms,
        Population,
        AveOccup,
        Latitude,
        Longitude,
        rooms_per_household,
        bedrooms_per_room,
        population_per_household
    ]])

    prediction = model.predict(features)

    st.success(f"Predicted House Price: {prediction[0]:.2f}")