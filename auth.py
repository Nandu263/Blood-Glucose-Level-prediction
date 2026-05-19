import streamlit as st

def login():
    st.sidebar.title("Login")

    role = st.sidebar.selectbox("Login As", ["Patient", "Doctor"])
    user = st.sidebar.text_input("Username")
    pwd = st.sidebar.text_input("Password", type="password")

    if role == "Patient" and user == "patient" and pwd == "1234":
        return "patient"
    elif role == "Doctor" and user == "doctor" and pwd == "admin":
        return "doctor"

    return None