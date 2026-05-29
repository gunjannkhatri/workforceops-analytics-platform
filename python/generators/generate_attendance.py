import pandas as pd
import numpy as np
from datetime import datetime, timedelta

employees = pd.read_csv(
    "datasets/raw/employees/employees.csv"
)

employees = employees[
    employees["employment_status"] == "Active"
]

attendance_records = []

start_date = datetime(2025, 1, 1)
end_date = datetime(2025, 12, 31)

date_range = pd.date_range(start_date, end_date)

attendance_id = 1

for _, employee in employees.iterrows():

    employee_id = employee["employee_id"]
    shift = employee["shift"]
    department = employee["department"]

    for current_date in date_range:

        if current_date.weekday() >= 5:
            continue

        attendance_status = np.random.choice(
            ["Present", "Present", "Present", "Absent", "Leave"],
            p=[0.82, 0.08, 0.03, 0.04, 0.03]
        )

        if attendance_status != "Present":

            attendance_records.append({
                "attendance_id": attendance_id,
                "employee_id": employee_id,
                "attendance_date": current_date.date(),
                "checkin_time": None,
                "checkout_time": None,
                "late_minutes": None,
                "work_hours": 0,
                "overtime_hours": 0,
                "attendance_status": attendance_status
            })

            attendance_id += 1
            continue

        if shift == "Morning":
            checkin_hour = 8
        elif shift == "General":
            checkin_hour = 9
        elif shift == "Evening":
            checkin_hour = 14
        else:
            checkin_hour = 20

        late_minutes = max(0, int(np.random.normal(10, 15)))

        checkin_time = datetime.combine(
            current_date.date(),
            datetime.min.time()
        ) + timedelta(
            hours=checkin_hour,
            minutes=late_minutes
        )

        work_hours = round(np.random.normal(8.5, 1.2), 2)

        if department in ["Operations", "Customer Support"]:
            overtime_hours = max(
                0,
                round(np.random.normal(1.5, 1), 2)
            )
        else:
            overtime_hours = max(
                0,
                round(np.random.normal(0.5, 0.5), 2)
            )

        checkout_time = checkin_time + timedelta(
            hours=work_hours + overtime_hours
        )

        attendance_records.append({
            "attendance_id": attendance_id,
            "employee_id": employee_id,
            "attendance_date": current_date.date(),
            "checkin_time": checkin_time,
            "checkout_time": checkout_time,
            "late_minutes": late_minutes,
            "work_hours": work_hours,
            "overtime_hours": overtime_hours,
            "attendance_status": attendance_status
        })

        attendance_id += 1

attendance_df = pd.DataFrame(attendance_records)

attendance_df.to_csv(
    "datasets/raw/attendance/attendance.csv",
    index=False
)

print("Attendance dataset generated.")
print(attendance_df.head())
