
import csv
import os
from datetime import datetime


def validate_record(name, date, status):
    if name.strip() == "":
        return False
    if status.strip().capitalize() not in ["Present", "Absent"]:
        return False
    if len(date) != 10 or date[4] != "-" or date[7] != "-":
        return False
    if not date.replace("-", "").isdigit():
        return False
    if not datetime.strptime(date, "%Y-%m-%d"):
        return False
    return True


def read_attendance():
    records = []
    if not os.path.exists("attendance.csv"):
        print("Warning: attendance.csv was not found.")
        print("Please create the file and try again.")
        return records

    with open("attendance.csv", "r", newline="") as file:
        reader = csv.reader(file)
        header = next(reader, None)
        if header != ["employee_name", "date", "status"]:
            print("Invalid or missing CSV header.")
            return records

        row_number = 1
        for row in reader:
            row_number += 1
            if len(row) == 3 and validate_record(row[0], row[1], row[2]):
                records.append([row[0].strip(), row[1], row[2].strip().capitalize()])
            else:
                print(f"Warning: Row {row_number} skipped because it has missing fields or an invalid attendance status.")

    print("Valid records:", len(records))
    return records


def calculate_attendance(records):
    attendance = {}

    for name, date, status in records:
        if name not in attendance:
            attendance[name] = [0, 0]

        if status == "Present":
            attendance[name][0] += 1
        else:
            attendance[name][1] += 1

    for name in attendance:
        present = attendance[name][0]
        absent = attendance[name][1]
        total = present + absent

        if total > 0:
            percentage = present / total * 100
        else:
            percentage = 0

        attendance[name] = [present, absent, total, percentage]

    return attendance


def identify_low_attendance(attendance):
    low = []

    for name in attendance:
        if attendance[name][3] < 75:
            low.append(name)

    return low


def analyze_attendance():
    records = read_attendance()

    if len(records) == 0:
        print("No valid records found.")
        return

    attendance = calculate_attendance(records)

    print("\nEmployee Present Absent Total Attendance")

    for name in attendance:
        present, absent, total, percentage = attendance[name]
        print(
            name, present, absent, total,
            format(percentage, ".2f") + "%"
        )

    print("\nEmployees below 75%:")
    low = identify_low_attendance(attendance)

    if len(low) == 0:
        print("None")

    for name in low:
        print(name, format(attendance[name][3], ".2f") + "%")


def generate_report():
    records = read_attendance()

    if len(records) == 0:
        print("No valid attendance records found.")
        return

    attendance = calculate_attendance(records)
    low_attendance = identify_low_attendance(attendance)

    with open("attendance_report.txt", "w") as file:
        file.write("EMPLOYEE ATTENDANCE REPORT\n")
        file.write("=" * 40 + "\n")

        for name, details in attendance.items():
            present = details[0]
            absent = details[1]
            total = details[2]
            percentage = details[3]

            file.write(f"Employee: {name}\n")
            file.write(f"Present days: {present}\n")
            file.write(f"Absent days: {absent}\n")
            file.write(f"Total recorded days: {total}\n")
            file.write(f"Attendance percentage: {percentage:.2f}%\n")

            if percentage < 75:
                file.write("Status: BELOW 75%\n")
            else:
                file.write("Status: Meets attendance threshold\n")

            file.write("\n")

        file.write(f"Employees below 75% attendance: {len(low_attendance)}\n" )

    print("Report generated.")
    


def append_attendance():
    name = input("Employee name: ").strip()
    date = input("Date (YYYY-MM-DD): ").strip()
    status = input("Status (Present/Absent): ").strip()
    if not validate_record(name, date, status):
        print("Invalid record. Please check the details.")
        return

    if os.path.exists("attendance.csv"):
        with open("attendance.csv", "r", newline="") as file:
            reader = csv.reader(file)
            header = next(reader, None)
            if header != ["employee_name", "date", "status"]:
                print("Invalid CSV header. Record not added.")
                return

    file_exists = os.path.exists("attendance.csv")
    if file_exists:
        with open("attendance.csv", "r") as file:
            content = file.read()
        if content and not content.endswith("\n"):
            with open("attendance.csv", "a") as file:
                file.write("\n")

    with open("attendance.csv", "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists or os.path.getsize("attendance.csv") == 0:
            writer.writerow(["employee_name", "date", "status"])
        writer.writerow([name, date, status.strip().capitalize()])
    print("Attendance record added successfully.")
    print("Existing records have been preserved.")


while True:
    print("\n========== EMPLOYEE ATTENDANCE SYSTEM ==========")
    print("1. Analyze Attendance")
    print("2. Add Attendance Record")
    print("3. Generate Report")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        analyze_attendance()
    elif choice == "2":
        append_attendance()
    elif choice == "3":
        generate_report()
    elif choice == "4":
        print("Exiting program.")
        break
    else:
        print("Invalid choice.")
