import streamlit as st
from compare_logs import run_discrepancy_check

st.title("📊 AAK Tracker Discrepancy Checker")

st.markdown("Compare tracking data across Mac, PC, and Web apps to find discrepancies in session reporting.")

if st.button("Run Analysis"):
    run_discrepancy_check()
