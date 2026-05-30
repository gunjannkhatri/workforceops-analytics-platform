import pandas as pd

attendance = pd.read_csv(
    "datasets/raw/attendance/attendance.csv"
)

attendance.columns = [
    col.lower().strip()
    for col in attendance.columns
]

attendance.to_parquet(
    "datasets/processed/bronze/attendance_bronze.parquet",
    index=False
)

print("Bronze layer created.")