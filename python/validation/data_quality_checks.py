import pandas as pd

attendance = pd.read_csv(
    "datasets/raw/attendance/attendance.csv"
)

print("Checking for null employee IDs...")
print(attendance["employee_id"].isnull().sum())

print("Checking duplicates...")
print(attendance.duplicated().sum())

print("Checking attendance status values...")
print(attendance["attendance_status"].value_counts())