import pandas as pd
import random
from faker import Faker

fake = Faker()

NUM_EMPLOYEES = 2000

departments = [
    "Operations",
    "Customer Support",
    "Finance",
    "HR",
    "Technology",
    "Sales",
    "Compliance"
]

roles = [
    "Analyst",
    "Senior Analyst",
    "Associate",
    "Manager",
    "Team Lead",
    "Executive",
    "Coordinator"
]

locations = [
    "Jaipur",
    "Bangalore",
    "Pune",
    "Hyderabad",
    "Mumbai",
    "Remote"
]

shifts = [
    "Morning",
    "General",
    "Evening",
    "Night"
]

salary_bands = [
    "L1",
    "L2",
    "L3",
    "L4"
]

employees = []

for emp_id in range(1001, 3001):

    employee = {
        "employee_id": emp_id,
        "full_name": fake.name(),
        "department": random.choice(departments),
        "role": random.choice(roles),
        "manager_id": random.randint(1001, 1100),
        "location": random.choice(locations),
        "shift": random.choice(shifts),
        "joining_date": fake.date_between(start_date='-5y', end_date='today'),
        "salary_band": random.choice(salary_bands),
        "employment_status": random.choice(
            ["Active", "Active", "Active", "Inactive"]
        )
    }

    employees.append(employee)

df = pd.DataFrame(employees)

df.to_csv(
    "datasets/raw/employees/employees.csv",
    index=False
)

print("Employee dataset generated successfully.")
print(df.head())