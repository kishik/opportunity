import pydeck as pdk
import pandas as pd
import numpy as np
import streamlit as st
import requests

url = 'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid={api_key}'
req = requests.get(url=url.format(city_name='Москва', api_key='267c99ba130b445b455b4aa7d9b5e617'))
print(req.json())
df = pd.DataFrame(
   np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
   columns=['lat', 'lon'])

st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=37.76,
        longitude=-122.4,
        zoom=11,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
           'HexagonLayer',
           data=df,
           get_position='[lon, lat]',
           radius=200,
           elevation_scale=4,
           elevation_range=[0, 1000],
           pickable=True,
           extruded=True,
        ),
        pdk.Layer(
            'ScatterplotLayer',
            data=df,
            get_position='[lon, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=200,
        ),
    ],
))
