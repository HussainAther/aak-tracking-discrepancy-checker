import matplotlib.pyplot as plt
import streamlit as st

def visualize_discrepancies(report):
    for eid, df in report:
        st.subheader(f"Employee {eid} - Session Duration by Platform")
        st.bar_chart(df)
