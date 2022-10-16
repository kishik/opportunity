import json

import requests
import streamlit as st

st.set_page_config(
    page_title="Transactions",
    page_icon=":shark:",
    layout="wide",
    initial_sidebar_state="expanded",

)


uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    if uploaded_file is not None:
        url = 'http://127.0.0.1:5000/import_transactions'
        data = json.loads(uploaded_file.getvalue().decode('utf-8'))
        x = requests.post(url, json=data)
        # visualisation(uploaded_file.json())
        load_patterns(x.text)
        '''
        TypeError: Cannot cast Index to dtype int64
        '''
