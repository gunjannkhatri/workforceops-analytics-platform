import pandas as pd

attendance = pd.read_parquet(
    "datasets/processed/silver/attendance_silver.parquet"
)

summary = attendance.groupby(
    "employee_id"
).agg({
    "work_hours": "sum",
    "overtime_hours": "sum",
    "late_minutes": "mean"
}).reset_index()

summary.to_parquet(
    "datasets/processed/gold/workforce_summary.parquet",
    index=False
)

print("Gold layer created.")