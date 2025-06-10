import os
import requests
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()

API_URL = os.getenv("API_URL")
HEADERS = {"x-api-key": os.getenv("API_KEY")} if os.getenv("API_KEY") else {}

ENDPOINTS = {
    "sessions": "/employee_data_sessions",
    "mouse": "/employee_data_mouse_movement",
    "keyboard": "/employee_data_keyboard"
}

DATE_FROM = "2024-06-01"
DATE_TO = "2025-05-31"

def fetch_all_logs():
    logs = {}
    employee_ids = [101, 102, 103]
    for eid in employee_ids:
        logs[eid] = {}
        for key, endpoint in ENDPOINTS.items():
            params = {
                "employee_id": eid,
                "date_from": DATE_FROM,
                "date_to": DATE_TO
            }
            try:
                res = requests.get(f"{API_URL}{endpoint}", params=params, headers=HEADERS)
                if res.status_code == 200:
                    logs[eid][key] = res.json()
                    print(f"✅ Fetched {key} for employee {eid} ({len(logs[eid][key])} records)")
                else:
                    print(f"❌ Error fetching {key} for {eid}: {res.status_code} — {res.text}")
            except Exception as e:
                print(f"⚠️ Exception fetching {key} for {eid}: {e}")
    return logs

if __name__ == "__main__":
    print("📥 Starting data pull...")
    logs = fetch_all_logs()
    print("\n📊 Summary of fetched logs:")
    for eid, sections in logs.items():
        print(f"Employee {eid}:")
        for section, records in sections.items():
            print(f"  - {section}: {len(records)} records")

