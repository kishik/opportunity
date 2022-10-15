import streamlit as st
from visualisation import page_config

page_config()

st.set_page_config(
        page_title="Transactions",
        page_icon=":shark:",
        layout="wide",
        initial_sidebar_state="expanded",

    )

st.header("Лучшие клиенты")
img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    # To read image file buffer as bytes:
    bytes_data = img_file_buffer.getvalue()
    # Check the type of bytes_data:
    # Should output: <class 'bytes'>

    st.write(type(bytes_data))
