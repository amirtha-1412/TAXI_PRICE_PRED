import streamlit as st
import pandas as pd
import pickle

st.image('car.png', width=800)
# App title
st.title("TAXI Price Prediction")

# Input fields (fully visible in dark mode)
km = st.number_input("Enter the Trip Distance in KM")
no_of_pass = st.number_input("Enter the no of passengers")
day_of_time = st.selectbox("Select Time of Day", ['Morning', 'Evening', 'Afternoon', 'Night'])
traffic = st.selectbox("Select traffic level", ['Low', 'High', 'Medium'])
weather_con = st.selectbox("Enter the Weather Condition", ['Clear', 'Rain', 'Snow'])
base = st.number_input("Enter Base Fare")
km1 = st.number_input("Enter the rate for one KM")
min1 = st.number_input("Enter the rate for per min")
duration = st.number_input("Enter the Trip duration")

# Button and prediction logic
submit = st.button("Submit")
with open('model_linear.pkl', 'rb') as file:  
    model = pickle.load(file)

if submit:
    if day_of_time == "Morning":
        day_of_time = 1
    if day_of_time == "Afternoon":
        day_of_time = 2
    if day_of_time == "Evening":
        day_of_time = 3
    if day_of_time == "Night":
        day_of_time = 4

    if traffic == "Low":
        traffic = 1    
    if traffic == "Medium":
        traffic = 2   
    if traffic == "High":
        traffic = 3      
    if weather_con == "Clear":
        weather_con = 1
    if weather_con == "Rain":
        weather_con = 2
    if weather_con == "Snow":
        weather_con = 3

    prediction_data = pd.DataFrame({
        'Trip_Distance_km': [km],
        'Time_of_Day': [day_of_time],
        'Passenger_Count': [no_of_pass],
        'Traffic_Conditions': [traffic],
        'Weather': [weather_con],
        'Base_Fare': [base],
        'Per_Km_Rate': [km1],
        'Per_Minute_Rate': [min1],
        'Trip_Duration_Minutes': [duration]
    })

    prediction = model.predict(prediction_data)
    prediction_value = round(float(prediction[0]))  # Round the prediction to the nearest integer
    
    st.markdown(
        f"""
        <style>
        .pulse {{
            display: inline-block;
            padding: 20px 40px;
            border: 2px solid #4CAF50;
            border-radius: 50px;
            font-size: 24px;
            color: #4CAF50;
            font-weight: bold;
            animation: pulse 2s infinite;
        }}
        @keyframes pulse {{
            0% {{ transform: scale(1); }}
            50% {{ transform: scale(1.05); }}
            100% {{ transform: scale(1); }}
        }}
        </style>
        <div class="pulse">
            Estimated Price:{prediction_value} Rupees
        </div>
        """,
        unsafe_allow_html=True
    )