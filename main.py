import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/WIN_20230606_13_58_15_Pro.jpg")

with col2:
    st.title("Ariel Johnson")
    content = """
    Hi, I am Ariel!
    """
    st.info(content)