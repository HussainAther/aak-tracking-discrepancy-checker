import pandas as pd
from datetime import datetime

def analyze_discrepancies(logs):
    result = {}

    # Session time analysis
    session_df = pd.DataFrame(logs.get("sessions", []))
    if not session_df.empty:
        session_df["start_time"] = pd.to_datetime(session_df["start_time"])
        session_df["end_time"] = pd.to_datetime(session_df["end_time"])
        session_df["duration_min"] = (session_df["end_time"] - session_df["start_time"]).dt.total_seconds() / 60
        session_summary = session_df.groupby(session_df["start_time"].dt.date)["duration_min"].sum().reset_index()
        result["sessions"] = session_summary.to_dict(orient="records")

    # Mouse movement
    mouse_df = pd.DataFrame(logs.get("mouse", []))
    if not mouse_df.empty and "timestamp" in mouse_df.columns:
        mouse_df["timestamp"] = pd.to_datetime(mouse_df["timestamp"])
        result["mouse_activity_count"] = len(mouse_df)

    # Keyboard activity
    keyboard_df = pd.DataFrame(logs.get("keyboard", []))
    if not keyboard_df.empty and "timestamp" in keyboard_df.columns:
        keyboard_df["timestamp"] = pd.to_datetime(keyboard_df["timestamp"])
        result["keyboard_activity_count"] = len(keyboard_df)

    return result

