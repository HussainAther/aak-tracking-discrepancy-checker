
import pandas as pd
from datetime import datetime

def analyze_discrepancies(logs):
    df = pd.DataFrame(logs["sessions"])
    df["start_time"] = pd.to_datetime(df["start_time"])
    df["end_time"] = pd.to_datetime(df["end_time"])
    df["duration_min"] = (df["end_time"] - df["start_time"]).dt.total_seconds() / 60
    summary = df.groupby(df["start_time"].dt.date)["duration_min"].sum().reset_index()
    return summary.to_dict(orient="records")
