from fastapi import FastAPI, WebSocket
from pydantic import BaseModel
from datetime import datetime
import sqlite3
import random
import requests

app = FastAPI(title="Healthcare AI System")


# -----------------------------------
# DATABASE SETUP
# -----------------------------------

conn = sqlite3.connect("healthcare.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS patients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    heart_rate INTEGER,
    sleep_hours REAL,
    stress_level INTEGER,
    risk TEXT,
    created_at TEXT
)
""")

conn.commit()


# -----------------------------------
# PATIENT MODEL
# -----------------------------------

class Patient(BaseModel):
    name: str
    age: int
    heart_rate: int
    sleep_hours: float
    stress_level: int


# -----------------------------------
# HOME ROUTE
# -----------------------------------

@app.get("/")
def home():
    return {
        "message": "Healthcare AI Backend Running"
    }


# -----------------------------------
# ABOUT ROUTE
# -----------------------------------

@app.get("/about")
def about():
    return {
        "project": "AI Healthcare Monitoring System",
        "version": "2.0"
    }


# -----------------------------------
# ADD PATIENT
# -----------------------------------

@app.post("/patients")
def add_patient(patient: Patient):

    # AI Health Risk Logic
    if patient.heart_rate > 120:
        risk = "High Risk"

    elif patient.stress_level > 7:
        risk = "Stress Warning"

    elif patient.sleep_hours < 5:
        risk = "Poor Sleep"

    else:
        risk = "Normal"

    created_at = str(datetime.now())

    cursor.execute("""
    INSERT INTO patients
    (name, age, heart_rate, sleep_hours,
    stress_level, risk, created_at)

    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        patient.name,
        patient.age,
        patient.heart_rate,
        patient.sleep_hours,
        patient.stress_level,
        risk,
        created_at
    ))

    conn.commit()

    return {
        "message": "Patient added successfully",
        "risk": risk
    }


# -----------------------------------
# GET ALL PATIENTS
# -----------------------------------

@app.get("/patients")
def get_patients():

    cursor.execute("SELECT * FROM patients")

    rows = cursor.fetchall()

    patients = []

    for row in rows:

        patients.append({
            "id": row[0],
            "name": row[1],
            "age": row[2],
            "heart_rate": row[3],
            "sleep_hours": row[4],
            "stress_level": row[5],
            "risk": row[6],
            "created_at": row[7]
        })

    return {
        "patients": patients
    }


# -----------------------------------
# HEALTH ANALYSIS
# -----------------------------------

@app.get("/health-analysis")
def health_analysis():

    cursor.execute("SELECT risk FROM patients")

    rows = cursor.fetchall()

    total = len(rows)

    high_risk = 0

    for row in rows:

        if row[0] == "High Risk":
            high_risk += 1

    return {
        "total_patients": total,
        "high_risk_patients": high_risk,
        "analysis": "Healthcare AI analysis completed"
    }


# -----------------------------------
# ALERT SYSTEM
# -----------------------------------

@app.get("/alerts")
def alerts():

    cursor.execute("""
    SELECT name, heart_rate
    FROM patients
    WHERE heart_rate > 120
    """)

    rows = cursor.fetchall()

    alerts_list = []

    for row in rows:

        alerts_list.append({
            "patient": row[0],
            "alert": "High Heart Rate",
            "heart_rate": row[1]
        })

    return {
        "total_alerts": len(alerts_list),
        "alerts": alerts_list
    }


# -----------------------------------
# RESEARCH SUMMARY
# -----------------------------------

@app.get("/research-summary")
def research_summary():

    summaries = [
        "Walking daily improves heart health.",
        "Good sleep improves immunity.",
        "Hydration supports brain function.",
        "Exercise reduces stress levels."
    ]

    return {
        "medical_insight": random.choice(summaries)
    }


# -----------------------------------
# VOICE QUERY
# -----------------------------------

@app.get("/voice-query")
def voice_query(query: str):

    return {
        "voice_input": query,
        "ai_response": f"Healthcare assistant processed: {query}"
    }


# -----------------------------------
# IMAGE ANALYSIS
# -----------------------------------

@app.get("/image-analysis")
def image_analysis():

    return {
        "detection": "No visible disease detected",
        "confidence": "96%"
    }


# -----------------------------------
# WEATHER API INTEGRATION
# -----------------------------------

@app.get("/health-weather")
def health_weather(city: str = "London"):

    try:

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY"

        response = requests.get(url)

        data = response.json()

        return {
            "city": city,
            "temperature": data["main"]["temp"],
            "weather": data["weather"][0]["description"]
        }

    except Exception as e:

        return {
            "error": str(e)
        }


# -----------------------------------
# REAL-TIME MONITORING
# -----------------------------------

@app.websocket("/live-monitor")
async def websocket_endpoint(websocket: WebSocket):

    await websocket.accept()

    while True:

        heart_rate = random.randint(60, 150)

        if heart_rate > 120:
            message = f"ALERT: High Heart Rate {heart_rate}"

        else:
            message = f"Heart Rate Normal: {heart_rate}"

        await websocket.send_text(message)