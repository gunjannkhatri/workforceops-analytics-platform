CREATE TABLE dim_employee (
employee_id INT PRIMARY KEY,
full_name VARCHAR(255),
department VARCHAR(100),
role VARCHAR(100),
location VARCHAR(100),
shift VARCHAR(50)
);

CREATE TABLE fact_attendance (
attendance_id INT PRIMARY KEY,
employee_id INT,
attendance_date DATE,
work_hours FLOAT,
overtime_hours FLOAT,
late_minutes FLOAT,
attendance_status VARCHAR(50)
);

CREATE TABLE fact_productivity (
productivity_id INT PRIMARY KEY,
employee_id INT,
date DATE,
tasks_completed INT,
calls_handled INT,
tickets_resolved INT,
avg_handle_time FLOAT,
idle_minutes FLOAT,
sla_score FLOAT,
productivity_score FLOAT
);

CREATE TABLE fact_finance (
finance_id INT PRIMARY KEY,
employee_id INT,
payroll_cost FLOAT,
overtime_cost FLOAT,
productivity_cost_ratio FLOAT
);
