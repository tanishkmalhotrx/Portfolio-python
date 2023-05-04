import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="email_forms"):
    user_email = st.text_input("Email address")
    user_message = st.text_area("Message")
    message = f"""\
    Subject: My_website Mail from {user_email}
    From: {user_email}
    {user_message}
    """
    button = st.form_submit_button("Submit")
    if button:
        send_email(user_message)
        st.info("Your Email was sent successfully!")