import pandas as pd
import pydeck as pdk
import requests
import streamlit as st

from visualisation import load_data

st.set_page_config(
    page_title="Transactions",
    page_icon=":shark:",
    layout="wide",
    initial_sidebar_state="expanded",
)

url = 'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid={api_key}'
req = requests.get(url=url.format(city_name='Москва', api_key='267c99ba130b445b455b4aa7d9b5e617'))

gps = pd.DataFrame(columns=['lat', 'lon'])
df = load_data('transactions.json', 100)
cities = pd.DataFrame(df['city'])
df2 = cities.groupby(['city']).city.transform('count')
for i in range(len(cities)):
    city = cities.values[i]
    req = requests.get(url=url.format(city_name=city, api_key='267c99ba130b445b455b4aa7d9b5e617'))
    data = req.json()[0]
    print(data['lat'], data['lon'])
    new_row = {'lat': data['lat'], 'lon': data['lon']}
    gps = gps.append(new_row, ignore_index=True)

st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=55.7504461,
        longitude=37.6174943,
        zoom=11,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
            'HexagonLayer',
            data=gps,
            get_position='[lon, lat]',
            radius=20000,
            elevation_scale=4,
            elevation_range=[0, 1000],
            pickable=True,
            extruded=True,
        ),
        pdk.Layer(
            'ScatterplotLayer',
            data=gps,
            get_position='[lon, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=20000,
        ),
    ],
))
