import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv(r"C:\Users\Stuti\Downloads\T1.csv")

st.title("🌬️ Wind Farm Digital Twin")

X = df[['Wind Speed (m/s)']]
y = df['LV ActivePower (kW)']

model = LinearRegression()
model.fit(X, y)

wind_speed = st.slider("Wind Speed", 0.0, 25.0, 5.0)
predicted_power = model.predict([[wind_speed]])[0]
st.write(f"### Predicted Power: {predicted_power:.2f} kW")
st.line_chart(df[['Wind Speed (m/s)', 'LV ActivePower (kW)']])
