import json

import pandas as pd
import pydeck as pdk
import requests
import streamlit as st
import numpy as np
import altair as alt
from bokeh.plotting import figure
from main_page import load_data

st.set_page_config(
    page_title="Transactions",
    page_icon=":shark:",
    layout="wide",
    initial_sidebar_state="expanded",

)

server = 'http://127.0.0.1:5000/{}'
methods = {'transactions': 'get_transactions', 'cities': 'cities_count'}


def map_draw():

    url = 'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid={api_key}'

    df = load_data(requests.get(server.format(methods['transactions'])).json(), 5000)
    res = pd.DataFrame(columns=['count', 'lat', 'lon'])
    print(res)

    # couunt_cities = requests.get(server.format(methods['cities'])).json()

    res['count'] = res['count'].astype(int)
    res['lat'] = res['lat'].astype(float)
    res['lon'] = res['lon'].astype(float)
    # print(df.head())
    cities = pd.DataFrame(df['city'])
    # print(cities.head())
    for i in range(len(df)):
        city = cities.iloc[i, :].values[0]
        print(city)
        req = requests.get(url=url.format(city_name=city, api_key='267c99ba130b445b455b4aa7d9b5e617'))
        data = req.json()[0]
        print(data['lat'], data['lon'])
        res = res.append({'count': i, 'lat': data['lat'], 'lon': data['lon']}, ignore_index=True)
    print(res.head())

    print('hi')
    st.pydeck_chart(pdk.Deck(
        map_style=None,
        tooltip={"text": "{position}\nCount: {count}"},
        initial_view_state=pdk.ViewState(
            latitude=55.7504461,
            longitude=37.6174943,
            zoom=11,
            pitch=50,
        ),
        layers=[
            # pdk.Layer(
            #     'HexagonLayer',
            #     data=df2_true,
            #     get_position='[lon, lat]',
            #     radius=200,
            #     auto_highlight=True,
            #     elevation_scale=50,
            #     pickable=True,
            #     elevation_range=[0, 3000],
            #     extruded=True,
            #     coverage=1
            # ),
            pdk.Layer(
                'GridLayer',
                data=res,
                get_position='[lon, lat]',
                pickable=True,
                extruded=True,
                cell_size=200000,
                elevation_scale=400,
            ),
        ],
    ))


if __name__ == '__main__':
    st.header('Карта распределения мошенических операций')
    map_draw()
