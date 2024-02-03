# app.py

import streamlit as st

# Page Title
st.title("My Streamlit App")

# Text Input
user_input = st.text_input("Enter your name:")
st.write("Hello, " + user_input + "!")
