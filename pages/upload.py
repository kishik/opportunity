import json

import requests
import streamlit as st

from visualisation import load_patterns

st.set_page_config(
    page_title="Transactions",
    page_icon=":shark:",
    layout="wide",
    initial_sidebar_state="expanded",

)

uploaded_file = st.file_uploader("Choose a JSON file")
if uploaded_file is not None:
    url = 'http://127.0.0.1:5000/import_transactions'
    data = json.loads(uploaded_file.getvalue().decode('utf-8'))
    x = requests.post(url, json=data)
    print(type(x))
    print(x)
    df = load_patterns(x.json())
    st.dataframe(df)
    df.to_csv('result.csv')
