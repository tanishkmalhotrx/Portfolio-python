import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Tanishk Malhotra")
    content = """
    Hi, I am Tanishk Malhotra. I am student at IIT Madras studying data science and programming. I love
    working with python, HTML, CSS, JS.
    """
    st.info(content)