# ==============================
# PATIENT MODULE IMPLEMENTATION
# ==============================

# 1. MODEL: app/models/patient.py
from datetime import datetime
from app.extensions import db
import uuid


class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.String(50), unique=True, nullable=False, default=lambda: str(uuid.uuid4())[:8])

    full_name = db.Column(db.String(150), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    sex = db.Column(db.String(10))

    phone = db.Column(db.String(20))
    address = db.Column(db.String(200))

    village = db.Column(db.String(100))
    parish = db.Column(db.String(100))
    sub_county = db.Column(db.String(100))

    occupation = db.Column(db.String(100))
    insurance_status = db.Column(db.String(50))
    next_of_kin = db.Column(db.String(150))

    created_at = db.Column(db.DateTime, default=datetime.utcnow)