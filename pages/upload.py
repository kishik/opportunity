import json
import streamlit as st
import pandas as pd
from visualisation import load_data, visualisation


uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    if uploaded_file is not None:
        visualisation(uploaded_file, 10)
