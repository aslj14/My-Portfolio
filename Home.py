import streamlit as st

col1, col2 = st.columns(2)

with col1:
    st.image("images/cartoonized_ariel.gif")

with col2:
    st.title("Ariel Johnson")
    content = """
    Hi, I am Ariel!
    """
    st.info(content)

