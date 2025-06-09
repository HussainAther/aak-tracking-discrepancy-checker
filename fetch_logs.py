import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("API_URL", "http://localhost:8000")

ENDPOINTS = {
    "sessions": "/employee_data_sessions",
    "mouse": "/employee_data_mouse_movement",
    "keyboard": "/employee_data_keyboard"
}

DATE_FROM = "2024-06-01"
DATE_TO = "2025-05-31"

def load_employee_ids():
    with open("employee_ids.txt", "r") as f:
        return [int(line.strip()) for line in f if line.strip().isdigit()]

def fetch_all_logs():
    logs = {}
    employee_ids = load_employee_ids()
    for eid in employee_ids:
        logs[eid] = {}
        for key, endpoint in ENDPOINTS.items():
            params = {
                "employee_id": eid,
                "date_from": DATE_FROM,
                "date_to": DATE_TO
            }
            try:
                res = requests.get(f"{API_URL}{endpoint}", params=params)
                if res.status_code == 200:
                    logs[eid][key] = res.json()
                else:
                    print(f"❌ Error fetching {key} for {eid}: {res.status_code} — {res.text}")
            except Exception as e:
                print(f"❌ Exception fetching {key} for {eid}: {e}")
    return logs

