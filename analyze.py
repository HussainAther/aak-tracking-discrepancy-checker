import pandas as pd

def analyze_discrepancies(logs):
    report = []
    for eid, data in logs.items():
        session_data = data.get("sessions", [])
        if not session_data:
            print(f"No session data for {eid}")
            continue

        df = pd.DataFrame(session_data)

        if 'start_time' not in df.columns or 'end_time' not in df.columns:
            print(f"Missing start_time/end_time for employee {eid}, columns found: {df.columns.tolist()}")
            continue

        df['start_time'] = pd.to_datetime(df['start_time'])
        df['end_time'] = pd.to_datetime(df['end_time'])
        df['duration'] = (df['end_time'] - df['start_time']).dt.total_seconds() / 60  # minutes
        df['date'] = df['start_time'].dt.date

        daily_summary = df.groupby('date')['duration'].sum().reset_index()
        report.append((eid, daily_summary))
    return report

