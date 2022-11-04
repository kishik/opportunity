import pandas as pd
import pydeck as pdk
import requests
import streamlit as st

from main_page import load_data

st.set_page_config(
    page_title="Transactions",
    page_icon=":shark:",
    layout="wide",
    initial_sidebar_state="expanded",

)


def map_draw():
    url = 'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid={api_key}'
    req = requests.get(url=url.format(city_name='Москва', api_key='267c99ba130b445b455b4aa7d9b5e617'))
    url_back = 'http://127.0.0.1:5000/get_transactions'
    # gps_dft = pd.DataFrame(columns=['city', 'lat', 'lon'])
    # gps_dff = pd.DataFrame(columns=['city', 'lat', 'lon'])
    patern = requests.get(url_back)
    df = load_data(patern.json(), 5000)
    # df_true = df[df['oper_result'] == 'Успешно']
    # df_false = df[df['oper_result'] == 'Отказ']
    # cities_dft = pd.DataFrame(df_true['city'])
    # cities_dff = pd.DataFrame(df_false['city'])
    # df2_true = df_true.groupby(['city']).size().reset_index(name='counts')
    #
    # df2_false = df_false.groupby(['city']).size().reset_index(name='counts')
    # lat = []
    # lon = []
    res = pd.DataFrame(columns=['count', 'lat', 'lon'])
    print(res)
    res['count'] = res['count'].astype(int)
    res['lat'] = res['lat'].astype(float)
    res['lon'] = res['lon'].astype(float)
    # res = res.append({'count': 100, 'lat': 55.75, 'lon': 37.62}, ignore_index=True)
    # res = res.append({'count': 50, 'lat': 59.94, 'lon': 30.31}, ignore_index=True)
    # res = res.append({'count': 14, 'lat': 48.72, 'lon': 44.5}, ignore_index=True)
    # res = res.append({'count': 12, 'lat': 56.14, 'lon': 40.4}, ignore_index=True)
    # res = res.append({'count': 12, 'lat': 59.58, 'lon': 30.13}, ignore_index=True)
    # res = res.append({'count': 18, 'lat': 43.11, 'lon': 131.87}, ignore_index=True)
    # res = res.append({'count': 17, 'lat': 48.48, 'lon': 135.08}, ignore_index=True)
    print(df.head())
    cities = pd.DataFrame(df['city'])
    print(cities.head())
    for i in range(len(df)):
        city = cities.iloc[i, :].values[0]
        print(city)
        req = requests.get(url=url.format(city_name=city, api_key='267c99ba130b445b455b4aa7d9b5e617'))
        data = req.json()[0]
        print(data['lat'], data['lon'])
        res = res.append({'count': i, 'lat': data['lat'], 'lon': data['lon']}, ignore_index=True)
    print(res.head())
    # df2_true['lat'] = lat
    # df2_true['lon'] = lon
    # lat = []
    # lon = []
    # for i in range(len(df2_false)):
    #     city = df2_false['city'][i]
    #     req = requests.get(url=url.format(city_name=city, api_key='267c99ba130b445b455b4aa7d9b5e617'))
    #     data = req.json()[0]
    #     print(data['lat'], data['lon'])
    #     lat.append(data['lat'])
    #     lon.append(data['lon'])
    # df2_false['lat'] = lat
    # df2_false['lon'] = lon

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
