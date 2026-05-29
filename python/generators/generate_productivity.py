import pandas as pd
import numpy as np
from datetime import datetime

employees = pd.read_csv(
    "datasets/raw/employees/employees.csv"
)

employees = employees[
    employees["employment_status"] == "Active"
]

productivity_records = []

date_range = pd.date_range(
    start="2025-01-01",
    end="2025-12-31"
)

productivity_id = 1

for _, employee in employees.iterrows():

    employee_id = employee["employee_id"]
    department = employee["department"]

    for current_date in date_range:

        if current_date.weekday() >= 5:
            continue

        if department == "Customer Support":

            calls_handled = max(
                20,
                int(np.random.normal(85, 20))
            )

            tickets_resolved = max(
                10,
                int(np.random.normal(45, 10))
            )

            tasks_completed = max(
                15,
                int(np.random.normal(60, 12))
            )

        elif department == "Technology":

            calls_handled = max(
                0,
                int(np.random.normal(5, 3))
            )

            tickets_resolved = max(
                5,
                int(np.random.normal(18, 5))
            )

            tasks_completed = max(
                5,
                int(np.random.normal(22, 6))
            )

        else:

            calls_handled = max(
                5,
                int(np.random.normal(30, 10))
            )

            tickets_resolved = max(
                5,
                int(np.random.normal(20, 8))
            )

            tasks_completed = max(
                10,
                int(np.random.normal(35, 10))
            )

        avg_handle_time = round(
            np.random.normal(12, 3),
            2
        )

        idle_minutes = max(
            0,
            round(np.random.normal(45, 20), 2)
        )

        sla_score = round(
            np.random.normal(92, 5),
            2
        )

        productivity_score = round(
            (
                tasks_completed * 0.4 +
                tickets_resolved * 0.3 +
                sla_score * 0.3
            ) / 2,
            2
        )

        productivity_records.append({
            "productivity_id": productivity_id,
            "employee_id": employee_id,
            "date": current_date.date(),
            "tasks_completed": tasks_completed,
            "calls_handled": calls_handled,
            "tickets_resolved": tickets_resolved,
            "avg_handle_time": avg_handle_time,
            "idle_minutes": idle_minutes,
            "sla_score": sla_score,
            "productivity_score": productivity_score
        })

        productivity_id += 1

productivity_df = pd.DataFrame(productivity_records)

productivity_df.to_csv(
    "datasets/raw/productivity/productivity.csv",
    index=False
)

print("Productivity dataset generated.")
print(productivity_df.head())