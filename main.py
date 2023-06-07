import streamlit as st

col1, col2 = st.columns(2)

with col1:
    st.image("images/DwG9sh8I_a.png")

with col2:
    st.title("Ariel Johnson")
    content = """
    Hi, I am Ariel!
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(content2)