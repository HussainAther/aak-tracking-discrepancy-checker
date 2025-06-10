
from fastapi import FastAPI, Query
from datetime import date
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI(title="Mock AAK API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def load_mock(filename):
    with open(f"mock_api/{filename}", "r") as f:
        return json.load(f)

def load_data(filename: str):
    full_path = os.path.join("data", filename)
    with open(full_path, "r") as f:
        return json.load(f)


@app.get("/employee_data_sessions")
def get_sessions(employee_id: int, date_from: str = "2024-06-01", date_to: str = "2025-05-31"):
    return load_mock("sessions.json")

@app.get("/employee_data_mouse_movement")
def get_mouse(employee_id: int, date_from: str = "2024-06-01", date_to: str = "2025-05-31"):
    return load_mock("mouse.json")

@app.get("/employee_data_keyboard")
def get_keyboard(employee_id: int, date_from: str = "2024-06-01", date_to: str = "2025-05-31"):
    return load_mock("keyboard.json")
