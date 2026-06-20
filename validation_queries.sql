-- View all patients
SELECT *
FROM Patients;

-- Total number of patients
SELECT COUNT(*)
FROM Patients;

-- Total number of doctors
SELECT COUNT(*)
FROM Doctors;

-- Total revenue
SELECT SUM(TotalAmount)
FROM Billing;

-- Paid Bills
SELECT *
FROM Billing
WHERE PaymentStatus='Paid';

-- Top 10 highest bills
SELECT *
FROM Billing
ORDER BY TotalAmount DESC
LIMIT 10;

-- Doctors by Department
SELECT Department,
COUNT(*) AS TotalDoctors
FROM Doctors
GROUP BY Department;

-- Appointment Status
SELECT Status,
COUNT(*) AS TotalAppointments
FROM Appointments
GROUP BY Status;

