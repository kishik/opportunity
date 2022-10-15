import pydeck as pdk
import pandas as pd
import numpy as np
import streamlit as st
import requests
from visualisation import load_data, page_config

page_config()

st.set_page_config(
        page_title="Transactions",
        page_icon=":shark:",
        layout="wide",
        initial_sidebar_state="expanded",

    )

url = 'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid={api_key}'
req = requests.get(url=url.format(city_name='Москва', api_key='267c99ba130b445b455b4aa7d9b5e617'))
print(req.json())

gps = pd.DataFrame(columns=[('lat', 'lon')])
df = load_data('transactions.json')
df = df.loc[:, 'city']
print(df)
for i in range(df.shape[0]):
    city = df.at[i]
    req = requests.get(url=url.format(city_name=city, api_key='267c99ba130b445b455b4aa7d9b5e617'))
    gps = gps.append((req['lat'], req['lot']))
print(gps)
df = pd.DataFrame(
   gps,
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
