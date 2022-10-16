import json

import requests
import streamlit as st

from visualisation import load_patterns

if __name__ == '__main__':
    uploaded_file = st.file_uploader("Choose a json file")

    if uploaded_file is not None:
        url = 'http://127.0.0.1:5000/import_transactions'
        data = json.loads(uploaded_file.getvalue().decode('utf-8'))
        x = requests.post(url, json=data)
        # visualisation(uploaded_file.json())
        # print(x.text)
        # print(x.json())
        st.dataframe(load_patterns(x.json()))
