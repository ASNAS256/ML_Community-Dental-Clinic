# ==============================
# 3. ROUTES: app/patients/routes.py
# ==============================
from flask import render_template, request, redirect, url_for
from app.extensions import db
from app.models.patient import Patient
from . import patients_bp
from datetime import datetime

# LIST + SEARCH
@patients_bp.route('/')
def list_patients():
    search = request.args.get('search')

    if search:
        patients = Patient.query.filter(Patient.full_name.ilike(f"%{search}%")).all()
    else:
        patients = Patient.query.all()

    return render_template('patients/list.html', patients=patients)

# ADD PATIENT
@patients_bp.route('/add', methods=['GET', 'POST'])
def add_patient():
    if request.method == 'POST':
        patient = Patient(
            full_name=request.form['full_name'],
            dob=datetime.strptime(request.form['dob'], '%Y-%m-%d'),
            sex=request.form['sex'],
            phone=request.form['phone'],
            address=request.form['address'],
            village=request.form['village'],
            parish=request.form['parish'],
            sub_county=request.form['sub_county'],
            occupation=request.form['occupation'],
            insurance_status=request.form['insurance_status'],
            next_of_kin=request.form['next_of_kin']
        )

        db.session.add(patient)
        db.session.commit()

        return redirect(url_for('patients.list_patients'))

    return render_template('patients/add.html')

# EDIT PATIENT
@patients_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_patient(id):
    patient = Patient.query.get_or_404(id)

    if request.method == 'POST':
        patient.full_name = request.form['full_name']
        patient.dob = datetime.strptime(request.form['dob'], '%Y-%m-%d')
        patient.sex = request.form['sex']
        patient.phone = request.form['phone']
        patient.address = request.form['address']
        patient.village = request.form['village']
        patient.parish = request.form['parish']
        patient.sub_county = request.form['sub_county']
        patient.occupation = request.form['occupation']
        patient.insurance_status = request.form['insurance_status']
        patient.next_of_kin = request.form['next_of_kin']

        db.session.commit()

        return redirect(url_for('patients.list_patients'))

    return render_template('patients/edit.html', patient=patient)

# DELETE PATIENT
@patients_bp.route('/delete/<int:id>')
def delete_patient(id):
    patient = Patient.query.get_or_404(id)

    db.session.delete(patient)
    db.session.commit()

    return redirect(url_for('patients.list_patients'))