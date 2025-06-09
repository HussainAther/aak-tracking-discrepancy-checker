import pandas as pd

def analyze_discrepancies(logs):
    report = []
    for eid, sessions in logs.items():
        df = pd.DataFrame(sessions)
        df['date'] = pd.to_datetime(df['start_time']).dt.date
        daily_minutes = df.groupby(['date', 'platform'])['duration_minutes'].sum().unstack(fill_value=0)
        report.append((eid, daily_minutes))
    return report
