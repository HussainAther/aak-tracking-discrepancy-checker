
from fetch_logs import fetch_all_logs
from analyze import analyze_discrepancies
import streamlit as st

def run_discrepancy_check():
    logs = fetch_all_logs()
    for eid, user_logs in logs.items():
        if not user_logs.get("sessions"):
            st.warning(f"No session data for {eid}")
            continue
        report = analyze_discrepancies(user_logs)
        st.subheader(f"Report for Employee {eid}")
        st.json(report)
