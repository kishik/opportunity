import json
import streamlit as st
import pandas as pd


with open('transactions.json') as json_file:
    data = json.load(json_file)
    data = data['transactions']
    data = data
    result = pd.DataFrame.from_dict(data).T
    result.index = result.index
    print(result.dtypes)

    st.write(result)
