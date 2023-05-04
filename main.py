import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=450)

with col2:
    st.title("Tanishk Malhotra")
    content = """
    Hi, I am Tanishk Malhotra. I am student at IIT Madras studying data science and programming. I love
    working with python, HTML, CSS, JS.
    """
    st.info(content)

st.title("My Work:", )

df = pandas.read_csv("data.csv", sep=";")

col3, col4 = st.columns(2)

with col3:
    for index, row in df[:10].iterrows():
        st.subheader(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.subheader(row["title"])