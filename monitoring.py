import streamlit as st

def monitoring_page():
    st.title("Real-Time Monitoring")

    bp = st.slider("Blood Pressure", 80, 180, 120)

    if bp > 140:
        st.error("High Blood Pressure!")

    elif bp < 90:
        st.warning("Low Blood Pressure!")

    else:
        st.success("BP Normal")