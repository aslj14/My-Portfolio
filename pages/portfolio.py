import streamlit as st
import pandas

st.title("My Portfolio")

col1, col2 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")

with col1:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col2:
    for index, row in df[10:].iterrows():
        st.header(row["title"])