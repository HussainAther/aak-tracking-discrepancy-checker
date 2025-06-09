import os
import requests
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()

API_URL = os.getenv("API_URL")
API_KEY = os.getenv("API_KEY")
HEADERS = {"Authorization": f"Bearer {API_KEY}"}

ENDPOINTS = {
    "sessions": "/employee_data_sessions",
    "mouse": "/employee_data_mouse_movement",
    "keyboard": "/employee_data_keyboard"
}

DATE_FROM = "2024-06-01"
DATE_TO = "2025-05-31"

def fetch_all_logs():
    logs = {}
    employee_ids = [101, 102, 103]  # Replace with real IDs or dynamic fetch
    for eid in employee_ids:
        logs[eid] = {}
        for key, endpoint in ENDPOINTS.items():
            params = {
                "employee_id": eid,
                "date_from": DATE_FROM,
                "date_to": DATE_TO
            }
            res = requests.get(f"{API_URL}{endpoint}", params=params, headers=HEADERS)
            if res.status_code == 200:
                logs[eid][key] = res.json()
            else:
                print(f"Error fetching {key} for {eid}: {res.status_code}")
    return logs
