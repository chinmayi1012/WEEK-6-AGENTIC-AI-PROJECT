import streamlit as st
from dashboard import dashboard_page
from analytics import analytics_page
from monitoring import monitoring_page

st.sidebar.title("Healthcare Assistant")

page = st.sidebar.radio(
    "Navigation",
    ["Dashboard", "Analytics", "Monitoring"]
)

if page == "Dashboard":
    dashboard_page()

elif page == "Analytics":
    analytics_page()

elif page == "Monitoring":
    monitoring_page()