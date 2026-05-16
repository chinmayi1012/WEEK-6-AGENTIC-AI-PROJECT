import streamlit as st
import pandas as pd

def analytics_page():
    st.title("Health Analytics")

    data = pd.DataFrame({
        "Day": [1, 2, 3, 4, 5],
        "Steps": [3000, 5000, 7000, 6500, 8000]
    })

    st.line_chart(data.set_index("Day"))