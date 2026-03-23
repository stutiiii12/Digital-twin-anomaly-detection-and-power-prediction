import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# load your dataset
df = pd.read_csv(r"C:\Users\Stuti\Downloads\T1.csv")

st.title("🌬️ Wind Farm Digital Twin")

# train a simple model (independent of your notebook)
X = df[['Wind Speed (m/s)']]
y = df['LV ActivePower (kW)']

model = LinearRegression()
model.fit(X, y)

# user input
wind_speed = st.slider("Wind Speed", 0.0, 25.0, 5.0)

# prediction
predicted_power = model.predict([[wind_speed]])[0]

st.write(f"### Predicted Power: {predicted_power:.2f} kW")

# show data
st.line_chart(df[['Wind Speed (m/s)', 'LV ActivePower (kW)']])