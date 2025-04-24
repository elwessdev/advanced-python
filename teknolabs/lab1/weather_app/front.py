import streamlit as st
import requests as req

st.title("wessWeather 🌤️")

city = st.text_input("Enter city")

if st.button("Get Weather"):
    if city:
        res = req.post(
                "http://localhost:8000/weather",
                json={"city": city}
            )
        if res.status_code == 200:
            data = res.json()
            st.markdown(f"<h1>Weather in {data['city']}</h1>", unsafe_allow_html=True)
            st.write(f"🌡️ Temperature: {data['temperature']}°C")
            st.write(f"☁️ Description: {data['description']}")
        else:
            st.error("City not found or error occurred.")
