import streamlit as st
from compare_logs import run_discrepancy_check
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

st.set_page_config(page_title="AAK Discrepancy Checker", layout="wide")

st.title("📊 AAK Tracker Discrepancy Checker")
st.write("Compare tracking data across Mac, PC, and Web apps to find discrepancies in session reporting.")

try:
    run_discrepancy_check()
except Exception as e:
    st.error(f"Something went wrong: {e}")
