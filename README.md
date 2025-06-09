# 📊 AAK Tracking Discrepancy Suite

This project helps you identify and analyze discrepancies in activity tracking across different platforms (Mac, PC, Web) using employee session logs. It's split into two parts:

---

## 🧱 Project Structure

```
aak-tracking-suite/
├── backend/       # Mock FastAPI server (simulates real AAK endpoints)
│   ├── main.py
│   ├── sessions.json, mouse.json, keyboard.json
│   ├── requirements.txt
│   └── run.sh
├── client/        # Streamlit app and analysis scripts
│   ├── main.py
│   ├── compare_logs.py
│   ├── fetch_logs.py
│   ├── analyze.py
│   └── .env
└── README.md
```

---

## 🚀 How to Use

### 1. 🔧 Start the Backend (Mock API)

This will run a mock FastAPI server with 3 endpoints:

* `/employee_data_sessions`
* `/employee_data_mouse_movement`
* `/employee_data_keyboard`

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

> 🔁 Leave this running in one terminal window/tab.

---

### 2. 🧠 Launch the Streamlit Discrepancy Checker

```bash
cd ../client
pip install -r ../backend/requirements.txt  # Reuses FastAPI dependencies
streamlit run main.py
```

The Streamlit UI will open in your browser, pull mock logs for employees 101–103, and display platform-based tracking summaries.

---

## 🔍 What It Does

* Pulls mock tracking logs via GET requests
* Compares session time consistency
* Aggregates daily usage
* Identifies missing or inconsistent logs

---

## 🔐 Configuration

Make sure the `.env` file (in `client/`) contains:

```env
API_URL=http://localhost:8000
```

You can change this to the real API URL when it's available again.

---

## 🛠️ Customize

* Want to add real employee IDs? Modify `employee_ids` in `fetch_logs.py`
* Want to hit the real FastAPI server? Replace the `API_URL` in `.env`
* Want to analyze mouse or keyboard behavior? Expand `analyze.py`

---

Made for AAK Tele-Science 🔬 by Syed and team 💡
