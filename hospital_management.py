import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="hospital_management"
)
cursor=connection.cursor()

while True:
    print("\n====HOSPITAL MANAGEMENT SYSTEM====")
    print("1. Patient Management")
    print("2. Doctor Management ")
    print("3. Appointments Management")
    print("4. Prescription Management")
    print("5. Billing Management")
    print("6. Exit")

    choice=input("Enter your choice:")

    if choice=="1":
        while True:
            print("\n ---PATIENT MANAGEMENT---")
            print("1. View Patients")
            print("2. Add Patient")
            print("3. Update Patient")
            print("4. Delete Patient")
            print("5. Back to Main Menu")

            patient_choice=input("Enter your choice:")

            if patient_choice=="1":
                cursor.execute("select*from patients")
                patients=cursor.fetchall()

                for patient in patients:
                    print(patient)
            elif patient_choice=="2":
                name=input("Enter Patient name:")
                age=int(input("Enter patient age:"))
                gender=input("Enter patient gender:")
                phone=input("Enter patient phone number:")
                address=input("Enter patient address:")

                cursor.execute("insert into patients(name,age,gender,phone,address)values(%s,%s,%s,%s,%s)",(name,age,gender,phone,address))
                connection.commit()
                print("Patient updated successfully!")
            elif patient_choice=="3":
                patient_id=int(input("Enter patient ID to update:"))
                new_phone=input("Enter new phone number:")
                
                cursor.execute("update patients set phone=%s where patient_id=%s",(new_phone,patient_id))
                connection.commit()
                print("Patient updated successfully! ")
            elif patient_choice=="4":
                patient_id=int(input("Enter patient ID to delete:"))
                cursor.execute("delete from appointments WHERE patient_id=%s ",(patient_id,))
                cursor.execute("delete from prescriptions WHERE patient_id=%s ",(patient_id,))
                cursor.execute("delete from billing WHERE patient_id=%s ",(patient_id,))
                cursor.execute("delete from patients WHERE patient_id=%s ",(patient_id,))
                connection.commit()
                print("Patient deleted successfully!")
            elif patient_choice=="5":
                break
            else:
                print("Invalid choice! Please try again.")

    elif choice=="2":
        while True:
            print("\n ---DOCTOR MANAGEMENT---")
            print("1. View Doctor list")
            print("2. Add doctor list")
            print("3. Update doctor list")
            print("4. Delete doctor list")
            print("5. Back to Main Menu")

            doctor_choice=input("Enter your choice:")

            if doctor_choice=="1":
                cursor.execute("select*from doctors")
                doctors=cursor.fetchall()
                for doctor in doctors:
                    print(doctor)
            elif doctor_choice=="2":
                doctor_name=input("Enter doctor name:")
                specialization=input("Enter specialization:")
                phone=input("Enter doctor phone number:")
                cursor.execute("insert into doctors(name,specialization,phone)values(%s,%s,%s)",(doctor_name,specialization,phone))
                connection.commit()
                print("Doctor added successfully!")
            elif doctor_choice=="3":
                doctor_id=int(input("Enter doctor ID to update:"))
                specialization=input("Enter specialization:")
                cursor.execute("update doctors set specialization=%s where doctor_id=%s",(specialization,doctor_id))
                connection.commit()
                print("Doctor updated successfully!")
            elif doctor_choice=="4":
                doctor_id=int(input("Enter doctor ID to delete:"))
                cursor.execute("delete from appointments WHERE doctor_id=%s",(doctor_id,))
                cursor.execute("delete from prescriptions WHERE doctor_id=%s",(doctor_id,))
                cursor.execute("delete from doctors WHERE doctor_id=%s",(doctor_id,))
                connection.commit()
                print("Doctor deleted successfully!")
            elif doctor_choice=="5":
                break
            else:
                print("Invalid choice! Please try again.")
    elif choice=="3":
        while True:
            print("\n ---APPOINTMENTS MANAGEMENT---")
            print("1. View Appointment list")
            print("2. Add appointment list")
            print("3. Update appointment list")
            print("4. Delete appointment list")
            print("5. Back to Main Menu")

            appointment_choice=input("Enter your choice")

            if appointment_choice=="1":
                cursor.execute("select*from appointments")
                appointments=cursor.fetchall()
                for appointment in appointments:
                    print(appointment)
            elif appointment_choice=="2":
                patient_id=int(input("Enter Patient ID:"))
                doctor_id=int(input("Enter Doctor ID:"))
                appointment_date=input("Enter Appointment Date(YYYY-MM-DD):")
                appointment_time=input("Enter Appointment Time(HH:MM:SS):")
                status=input("Enter appointment status:")
                cursor.execute("insert into appointments(patient_id,doctor_id,appointment_date,appointment_time,status)values(%s,%s,%s,%s,%s)",(patient_id,doctor_id,appointment_date,appointment_time,status))
                connection.commit()
                print("Appointment added successfully!")
            elif appointment_choice=="3":
                appointment_id=int(input("Enter appointment ID to update:"))
                status=input("Enter Appointment Status:")
                cursor.execute("update appointments set status=%s where appointment_id=%s",(status,appointment_id_id))
                connection.commit()
                print("Appointment update successfully!")
            elif appointment_choice=="4":
                appointment_id=int(input("Enter Appointment ID to delete:"))
                cursor.execute("delete from appointments WHERE  appointment_id=%s",(appointment_id,))
                connection.commit()
                print("Appointment Deleted successfully!")
            elif appointment_choice=="5":
                break
            else:
                print("Invalid choice! Please try again.")

    elif choice=="4":
        while True:
            print("\n ---PRESCRIPTIONS MANAGEMENT---")
            print("1. View Prescription list")
            print("2. Add Prescription list")
            print("3. Update Prescription list")
            print("4. Delete Prescription list")
            print("5. Back to Main Menu")

            prescription_choice=input("Enter your choice:")

            if prescription_choice=="1":
                cursor.execute("select*from prescriptions")
                prescriptions=cursor.fetchall()
                for prescription in prescriptions:
                    print(prescription)
            elif prescription_choice=="2":
                patient_id=int(input("Enter Patient ID:"))
                doctor_id=int(input("Enter Doctor ID:"))
                medicine=input("Enter Medicine name:")
                instructions=input("Enter Instructions:")
                cursor.execute("insert into prescriptions(patient_id,doctor_id,medicine,instructions)values(%s,%s,%s,%s)",(patient_id,doctor_id,medicine,instructions))
                connection.commit()
                print("Prescriptions added successfully!")
            elif prescription_choice=="3":
                prescription_id=int(input("Enter Prescription ID to update:"))
                instructions=input("Enter instructions :")
                cursor.execute("update prescriptions set instructions=%s where prescription_id=%s",(instructions,prescription_id))
                connection.commit()
                print("Prescriptions updated successfully!")
            elif prescription_choice=="4":
                prescription_id=int(input("Enter Prescription ID to delete:"))
                cursor.execute("delete from prescriptions WHERE prescription_id=%s",(prescription_id,))
                connection.commit()
                print("Prescriptions deleted successfully!")
            elif prescription_choice=="5":
                break
            else:
                print("Invalid choice! Please try again.")

    elif choice=="5":
        while True:
            print("\n ---BILLING MANAGEMENT---")
            print("1. View billing list")
            print("2. Add billing list")
            print("3. Update billing list")
            print("4. Delete billing list")
            print("5. Back to Main Menu")

            billing_choice=input("Enter your choice:")

            if billing_choice=="1":
                cursor.execute("select*from billing")
                billing=cursor.fetchall()
                for bill in billing:
                    print(bill)
            elif billing_choice=="2":
                patient_id=int(input("Enter Patient ID:"))
                amount=float(input("Enter amount value:"))
                payment_status=input("Enter payment status :")
                cursor.execute("insert into billing(patient_id,amount,payment_status)values(%s,%s,%s)",(patient_id,amount,payment_status))
                connection.commit()
                print("Billing added successfully")
            elif billing_choice=="3":
                bill_id=int(input("Enter Bill ID to update:"))
                payment_status=input("Enter payment status:")
                cursor.execute("update billing set payment_status=%s where bill_id=%s",(payment_status,billing_id))
                connection.commit()
                print("Billing updated successfully!")
            elif billing_choice=="4":
                bill_id=int(input("Enter bill ID to delete:"))
                cursor.execute("delete from billing WHERE bill_id=%s",(bill_id,))
                connection.commit()
                print("Billing deleted successfully!")
            elif billing_choice=="5":
                break
            else:
                print("Invalid choice! Please try again.")
    elif choice=="6":
        print("Thank You! Exiting Hospital Management System.")
        break

    else:
        print("Invalid choice! Please try again.")