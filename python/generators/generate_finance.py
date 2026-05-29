import pandas as pd
import numpy as np
import random

employees = pd.read_csv(
    "datasets/raw/employees/employees.csv"
)

finance_records = []

finance_id = 1

for _, employee in employees.iterrows():

    salary_band = employee["salary_band"]

    if salary_band == "L1":
        payroll_cost = random.randint(25000, 40000)

    elif salary_band == "L2":
        payroll_cost = random.randint(40000, 70000)

    elif salary_band == "L3":
        payroll_cost = random.randint(70000, 120000)

    else:
        payroll_cost = random.randint(120000, 200000)

    overtime_cost = round(
        payroll_cost * np.random.uniform(0.05, 0.2),
        2
    )

    productivity_cost_ratio = round(
        np.random.uniform(0.7, 1.3),
        2
    )

    finance_records.append({
        "finance_id": finance_id,
        "employee_id": employee["employee_id"],
        "department": employee["department"],
        "payroll_cost": payroll_cost,
        "overtime_cost": overtime_cost,
        "productivity_cost_ratio": productivity_cost_ratio
    })

    finance_id += 1

finance_df = pd.DataFrame(finance_records)

finance_df.to_csv(
    "datasets/raw/finance/finance.csv",
    index=False
)

print("Finance dataset generated.")
print(finance_df.head())