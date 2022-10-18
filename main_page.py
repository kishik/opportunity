import json

import pandas as pd
import requests
import streamlit as st

api_url = 'http://api.openweathermap.org/geo/1.0/direct'


def page_config():
    st.set_page_config(
        page_title="Transactions",
        page_icon=":shark:",
        layout="wide",
        initial_sidebar_state="expanded",

    )


def load_data(data, nrows=0):
    if nrows <= 0:
        return pd.DataFrame()
    data = data['transactions']
    result = pd.DataFrame.from_dict(data).T
    result = result[:nrows]
    result.index = result.index.astype(int)
    result['amount'] = result['amount'].astype(int)
    result['passport'] = result['passport'].astype(str)
    result['date'] = pd.to_datetime(result['date'], format='%Y-%m-%dT%H:%M:%S')
    result['account_valid_to'] = pd.to_datetime(result['account_valid_to'], format='%Y-%m-%d')
    result['date_of_birth'] = pd.to_datetime(result['date_of_birth'], format='%Y-%m-%d')
    result['passport_valid_to'] = pd.to_datetime(result['passport_valid_to'], format='%Y-%m-%d')
    return result


def load_patterns(data):
    data = data['fraud_transactions']
    result = pd.DataFrame.from_dict(data).T

    result.index = result.index.astype(str)
    return result


def get_ids(patern):
    chars = " []'"
    s = str(st.session_state['paterns'].json()['fraud_transactions'][patern]['transactions'])
    res = s.translate(str.maketrans('', '', chars))
    return res


if __name__ == '__main__':
    st.header("Решение кейса от команды WIN+NERS")
    paterns = ''
    uploaded_file = st.file_uploader("Загрузите JSON файл прежде чем продолжить работу на сайте")
    if uploaded_file is not None:
        url = 'http://127.0.0.1:5000/import_transactions'
        data = json.loads(uploaded_file.getvalue().decode('utf-8'))
        paterns = requests.post(url, json=data)
        df = load_patterns(paterns.json())
        st.header("Таблица фродовских операций")
        st.dataframe(df)
        df.to_csv('result.csv')
        st.session_state['paterns'] = paterns
