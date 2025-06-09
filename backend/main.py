from fastapi import FastAPI, Query
import json
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="AAK Mock API", version="0.1.0")

# Allow all CORS (for dev purposes)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def load_data(filename):
    with open(filename, "r") as f:
        return json.load(f)

@app.get("/employee_data_sessions")
def get_sessions(employee_id: int, date_from: str = "2024-06-01", date_to: str = "2025-05-31"):
    return load_data("sessions.json")

@app.get("/employee_data_mouse_movement")
def get_mouse(employee_id: int, date_from: str = "2024-06-01", date_to: str = "2025-05-31"):
    return load_data("mouse.json")

@app.get("/employee_data_keyboard")
def get_keyboard(employee_id: int, date_from: str = "2024-06-01", date_to: str = "2025-05-31"):
    return load_data("keyboard.json")

