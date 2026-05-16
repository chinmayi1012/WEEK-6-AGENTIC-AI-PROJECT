import streamlit as st

def dashboard_page():
    st.title("Healthcare Dashboard")

    st.metric("Heart Rate", "78 bpm")
    st.metric("Water Intake", "2.5 L")
    st.metric("Sleep", "7 hrs")

    st.success("Medicine Taken On Time")