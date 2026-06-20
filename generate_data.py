from faker import Faker
import pandas as pd
import random
import sqlite3

fake = Faker()

patients = []

for i in range(1,101):
    patients.append({
        "PatientID": i,
        "FirstName": fake.first_name(),
        "LastName": fake.last_name(),
        "Gender": random.choice(["Male","Female"]),
        "BloodType": random.choice(["A+","B+","O+","AB+"]),
        "Phone": fake.phone_number()
    })

patient_df = pd.DataFrame(patients)

print(patient_df.head())

# Save CSV
patient_df.to_csv("datasets/patients.csv", index=False)

print("patients.csv created successfully!")

# ===================== DOCTORS DATA =====================

doctors = []

specializations = [
    "Cardiology",
    "Neurology",
    "Orthopedics",
    "Pediatrics",
    "Dermatology",
    "General Medicine"
]

for i in range(1, 21):
    doctors.append({
        "DoctorID": i,
        "DoctorName": fake.name(),
        "Department": random.choice(specializations),
        "Status": "Active"
    })

doctor_df = pd.DataFrame(doctors)

print(doctor_df.head())

doctor_df.to_csv("datasets/doctors.csv", index=False)

print("doctors.csv created successfully!")

# ===================== APPOINTMENTS DATA =====================

appointments = []

for i in range(1, 501):

    appointments.append({
        "AppointmentID": i,
        "PatientID": random.randint(1,100),
        "DoctorID": random.randint(1,20),
        "AppointmentDate": fake.date_between(start_date="-1y", end_date="today"),
        "Status": random.choice(["Completed","Pending","Cancelled"]),
        "ConsultationFee": random.randint(500,2000)
    })

appointment_df = pd.DataFrame(appointments)

print(appointment_df.head())

appointment_df.to_csv("datasets/appointments.csv", index=False)

print("appointments.csv created successfully!")

# ===================== BILLING DATA =====================

billing = []

for i in range(1,501):

    room_charge = random.randint(1000,5000)
    treatment_charge = random.randint(500,8000)
    medicine_charge = random.randint(100,3000)

    total = room_charge + treatment_charge + medicine_charge

    billing.append({
        "BillID": i,
        "PatientID": random.randint(1,100),
        "AppointmentID": i,
        "RoomCharges": room_charge,
        "TreatmentCharges": treatment_charge,
        "MedicineCharges": medicine_charge,
        "TotalAmount": total,
        "PaymentStatus": random.choice(["Paid","Pending"]),
        "PaymentMethod": random.choice(["Cash","Card","UPI","Insurance"])
    })

billing_df = pd.DataFrame(billing)

billing_df.to_csv("datasets/billing.csv",index=False)

print("billing.csv created successfully!")

# ===================== PHARMACY DATA =====================

medicines = [
"Paracetamol",
"Azithromycin",
"Crocin",
"Dolo 650",
"Amoxicillin",
"Cetirizine",
"Pantoprazole",
"Metformin",
"Insulin",
"Aspirin"
]

pharmacy=[]

for i in range(1,101):

    pharmacy.append({
        "MedicineID":i,
        "MedicineName":random.choice(medicines),
        "Category":random.choice(["Tablet","Syrup","Injection"]),
        "StockQuantity":random.randint(10,500),
        "UnitPrice":random.randint(20,1000)
    })

pharmacy_df=pd.DataFrame(pharmacy)

pharmacy_df.to_csv("datasets/pharmacy.csv",index=False)

print("pharmacy.csv created successfully!")

# ===================== DATABASE =====================

conn = sqlite3.connect("hospital_db.db")

print("Database created successfully!")

# Export dataframes to SQLite tables

patient_df.to_sql(
    "Patients",
    conn,
    if_exists="replace",
    index=False
)

doctor_df.to_sql(
    "Doctors",
    conn,
    if_exists="replace",
    index=False
)

appointment_df.to_sql(
    "Appointments",
    conn,
    if_exists="replace",
    index=False
)

billing_df.to_sql(
    "Billing",
    conn,
    if_exists="replace",
    index=False
)

pharmacy_df.to_sql(
    "Pharmacy",
    conn,
    if_exists="replace",
    index=False
)

print("All tables inserted successfully!")

conn.close()


# ===================== EXCEL FILE =====================

with pd.ExcelWriter("hospital_records.xlsx") as writer:

    patient_df.to_excel(
        writer,
        sheet_name="Patients",
        index=False
    )

    doctor_df.to_excel(
        writer,
        sheet_name="Doctors",
        index=False
    )

    appointment_df.to_excel(
        writer,
        sheet_name="Appointments",
        index=False
    )

    billing_df.to_excel(
        writer,
        sheet_name="Billing",
        index=False
    )

    pharmacy_df.to_excel(
        writer,
        sheet_name="Pharmacy",
        index=False
    )

print("hospital_records.xlsx created successfully!")
