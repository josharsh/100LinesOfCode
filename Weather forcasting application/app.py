import os
import pyowm
import streamlit as st
from matplotlib import dates
from datetime import datetime
from matplotlib import pyplot as plt
owm = pyowm.OWM('your api key from weather map api')
mgr = owm.weather_manager()
st.title("5 Day Weather Forecast")
st.write("### Write the name of a City and select the Temperature Unit and Graph Type from the sidebar")
place = st.text_input("NAME OF THE CITY :", "")
if place is None:
    st.write("Input a CITY!")
unit = st.selectbox("Select Temperature Unit", ("Celsius", "Fahrenheit"))
g_type = st.selectbox("Select Graph Type", ("Line Graph", "Bar Graph"))
observation = mgr.forecast_at_place(place, '3h')
plt.bar(days, temp_min)
plt.bar(days, temp_max)
forecaster = mgr.forecast_at_place(place, '3h')
print(forecaster.will_have_rain())
print(weather.sunrise_time(timeformat='iso'))
humidity = weather.humidity
print(f'The current humidity is {humidity}%')
