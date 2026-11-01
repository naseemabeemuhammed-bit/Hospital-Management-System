create database hospital_management;
use hospital_management;

create table patients(
patient_id int primary key auto_increment,
name varchar(100) not null,
age int,
gender varchar(20),
phone varchar(15),
address varchar(200)
);

create table doctors(
doctor_id int primary key auto_increment,
name varchar(100) not null,
specialization varchar(100),
phone varchar(15)
);

create table appointments(
appointment_id int primary key auto_increment,
patient_id int,
doctor_id int,
appointment_date date,
appointment_time time,
status varchar(50),
foreign key (patient_id)references patients(patient_id),
foreign key(doctor_id) references doctors(doctor_id)
);

create table prescriptions(
prescription_id int primary key auto_increment,
patient_id int,
doctor_id int,
medicine varchar(100),
instructions varchar(200),
foreign key (patient_id) references patients(patient_id),
foreign key(doctor_id) references doctors(doctor_id)
);

create table billing(
bill_id int primary key auto_increment,
patient_id int,
amount decimal(10,2),
payment_status varchar(50),
foreign key(patient_id) references patients(patient_id)
);

insert into patients(name,age,gender,phone,address) value
('Arun',25,'Male','9876543210','Chennai'),
('Priya',22,'Female','9876543211','Kanchipuram'),
('Rahul',30,'Male','9876543212','Tambaram'),
('Divya',28,'Female','9876543213','Chennai'),
('Kumar',35,'Male','9876543214','Vellore'),
('Anjali',26,'Female','9876543215','Chennai'),
('Vijay',40,'Male','9876543216','Madurai'),
('Meena',30,'Female','9876543217','Salem'),
('Suresh', 29, 'Male', '9876543218', 'Coimbatore'),
('Kavitha', 45, 'Female', '9876543219', 'Trichy'),
('Manoj', 27, 'Male', '9876543220', 'Chennai'),
('Lakshmi', 38, 'Female', '9876543221', 'Kanchipuram'),
('Ramesh', 50, 'Male', '9876543222', 'Vellore'),
('Deepa', 31, 'Female', '9876543223', 'Tambaram'),
('Prakash', 33, 'Male', '9876543224', 'Chennai'),
('Nisha', 24, 'Female', '9876543225', 'Madurai'),
('Ganesh', 42, 'Male', '9876543226', 'Salem'),
('Swetha', 29, 'Female', '9876543227', 'Chennai'),
('Senthil', 36, 'Male', '9876543228', 'Trichy'),
('Aarthi', 27, 'Female', '9876543229', 'Kanchipuram');

select*from patients;

INSERT INTO doctors (name, specialization, phone)
VALUES
('Dr. Rajesh Kumar', 'Cardiologist', '9000000001'),
('Dr. Priya Sharma', 'Dermatologist', '9000000002'),
('Dr. Arun Kumar', 'Neurologist', '9000000003'),
('Dr. Meena Devi', 'Pediatrician', '9000000004'),
('Dr. Suresh Babu', 'Orthopedic', '9000000005'),
('Dr. Kavitha', 'Gynecologist', '9000000006'),
('Dr. Vijay', 'General Physician', '9000000007'),
('Dr. Anitha', 'ENT Specialist', '9000000008'),
('Dr. Ramesh', 'Dentist', '9000000009'),
('Dr. Deepa', 'Ophthalmologist', '9000000010');

select*from doctors;

INSERT INTO appointments
(patient_id, doctor_id, appointment_date, appointment_time, status)
VALUES
(1, 1, '2026-09-10', '09:00:00', 'Completed'),
(2, 2, '2026-09-10', '09:30:00', 'Completed'),
(3, 3, '2026-09-11', '10:00:00', 'Scheduled'),
(4, 4, '2026-09-11', '10:30:00', 'Scheduled'),
(5, 5, '2026-09-12', '11:00:00', 'Completed'),
(6, 6, '2026-09-12', '11:30:00', 'Scheduled'),
(7, 7, '2026-09-13', '09:00:00', 'Completed'),
(8, 8, '2026-09-13', '09:30:00', 'Scheduled'),
(9, 9, '2026-09-14', '10:00:00', 'Completed'),
(10, 10, '2026-09-14', '10:30:00', 'Scheduled'),
(11, 1, '2026-09-15', '11:00:00', 'Scheduled'),
(12, 2, '2026-09-15', '11:30:00', 'Completed'),
(13, 3, '2026-09-16', '09:00:00', 'Scheduled'),
(14, 4, '2026-09-16', '09:30:00', 'Completed'),
(15, 5, '2026-09-17', '10:00:00', 'Scheduled'),
(16, 6, '2026-09-17', '10:30:00', 'Completed'),
(17, 7, '2026-09-18', '11:00:00', 'Scheduled'),
(18, 8, '2026-09-18', '11:30:00', 'Completed'),
(19, 9, '2026-09-19', '09:00:00', 'Scheduled'),
(20, 10, '2026-09-19', '09:30:00', 'Scheduled');

select*from appointments;

INSERT INTO prescriptions
(patient_id, doctor_id, medicine, instructions)
VALUES
(1, 1, 'Aspirin', 'Take after food'),
(2, 2, 'Cetirizine', 'Take once daily'),
(3, 3, 'Paracetamol', 'Take twice daily'),
(4, 4, 'Amoxicillin', 'Take after food'),
(5, 5, 'Ibuprofen', 'Take after meals'),
(6, 6, 'Vitamin Tablets', 'Take once daily'),
(7, 7, 'Paracetamol', 'Take when needed'),
(8, 8, 'Ear Drops', 'Use twice daily'),
(9, 9, 'Pain Relief Medicine', 'Take after food'),
(10, 10, 'Eye Drops', 'Use three times daily'),
(11, 1, 'Aspirin', 'Take once daily'),
(12, 2, 'Skin Cream', 'Apply twice daily'),
(13, 3, 'Vitamin B12', 'Take once daily'),
(14, 4, 'Cough Syrup', 'Take twice daily'),
(15, 5, 'Pain Killer', 'Take after meals'),
(16, 6, 'Iron Tablets', 'Take once daily'),
(17, 7, 'Antacid', 'Take before food'),
(18, 8, 'Nasal Spray', 'Use twice daily'),
(19, 9, 'Dental Medicine', 'Take as prescribed'),
(20, 10, 'Eye Medicine', 'Use twice daily');

select*from prescriptions;

INSERT INTO billing
(patient_id, amount, payment_status)
VALUES
(1, 1500.00, 'Paid'),
(2, 2000.00, 'Paid'),
(3, 1800.00, 'Pending'),
(4, 2500.00, 'Paid'),
(5, 3000.00, 'Paid'),
(6, 2200.00, 'Pending'),
(7, 1200.00, 'Paid'),
(8, 1700.00, 'Paid'),
(9, 3500.00, 'Pending'),
(10, 2800.00, 'Paid'),
(11, 1500.00, 'Paid'),
(12, 2300.00, 'Pending'),
(13, 1900.00, 'Paid'),
(14, 2100.00, 'Paid'),
(15, 4000.00, 'Pending'),
(16, 2600.00, 'Paid'),
(17, 1400.00, 'Paid'),
(18, 1600.00, 'Pending'),
(19, 3200.00, 'Paid'),
(20, 2700.00, 'Paid');

select*from billing;
