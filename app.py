import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

st.set_page_config(page_title="Dynamic Pricing Predictor", layout="centered")
st.title("🚕 Dynamic Ride Cost Predictor")

# Model paths
MODEL_PATHS = {
    "Linear Regression": "model/linear_regression_model.pkl",
    "Random Forest": "model/random_forest_regressor_model.pkl",
    "Gradient Boosting": "model/gradient_boosting_model.pkl"
}

# Label encoding mappings based on training
location_map = {"Rural": 0, "Suburban": 1, "Urban": 2}
loyalty_map = {"Gold": 0, "Silver": 1, "Regular": 2}
booking_time_map = {"Afternoon": 0, "Evening": 1, "Morning": 2, "Night": 3}
vehicle_type_map = {"Economy": 0, "Premium": 1}

# Input form
st.subheader("Enter Ride Details")

with st.form("prediction_form"):
    model_choice = st.selectbox("Select Prediction Model", list(MODEL_PATHS.keys()))

    num_riders = st.number_input("Number of Riders", min_value=1, max_value=200, value=50)
    num_drivers = st.number_input("Number of Drivers", min_value=1, max_value=200, value=30)
    location = st.selectbox("Location Category", list(location_map.keys()))
    loyalty = st.selectbox("Customer Loyalty Status", list(loyalty_map.keys()))
    past_rides = st.number_input("Number of Past Rides", min_value=0, max_value=1000, value=10)
    rating = st.slider("Average Ratings", min_value=1.0, max_value=5.0, value=4.2, step=0.01)
    booking_time = st.selectbox("Time of Booking", list(booking_time_map.keys()))
    vehicle_type = st.selectbox("Vehicle Type", list(vehicle_type_map.keys()))
    ride_duration = st.number_input("Expected Ride Duration (in minutes)", min_value=1, max_value=500, value=60)

    submitted = st.form_submit_button("Predict Ride Cost")

if submitted:
    model_path = MODEL_PATHS[model_choice]
    if not os.path.exists(model_path):
        st.error(f"Model file not found at: {model_path}")
    else:
        model = joblib.load(model_path)

        # Create DataFrame from encoded input
        input_dict = {
            "Number_of_Riders": [num_riders],
            "Number_of_Drivers": [num_drivers],
            "Location_Category": [location_map[location]],
            "Customer_Loyalty_Status": [loyalty_map[loyalty]],
            "Number_of_Past_Rides": [past_rides],
            "Average_Ratings": [rating],
            "Time_of_Booking": [booking_time_map[booking_time]],
            "Vehicle_Type": [vehicle_type_map[vehicle_type]],
            "Expected_Ride_Duration": [ride_duration]
        }

        input_df = pd.DataFrame(input_dict)

        # Predict
        prediction = model.predict(input_df)[0]
        st.success(f"Estimated Ride Cost: ₹{prediction:.2f}")
