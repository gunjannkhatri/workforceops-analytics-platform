import pandas as pd

attendance = pd.read_parquet(
    "datasets/processed/bronze/attendance_bronze.parquet"
)

attendance = attendance.drop_duplicates()

attendance["late_minutes"] = attendance[
    "late_minutes"
].fillna(0)

attendance.to_parquet(
    "datasets/processed/silver/attendance_silver.parquet",
    index=False
)

print("Silver layer created.")