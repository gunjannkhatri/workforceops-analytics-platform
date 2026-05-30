Attendance Rate

SELECT
ROUND(
100.0 *
SUM(
CASE
WHEN attendance_status='Present'
THEN 1
ELSE 0
END
)
/
COUNT(*),
2
) AS attendance_rate
FROM fact_attendance;

Average Productivity Score 

SELECT
AVG(productivity_score)
AS avg_productivity_score
FROM fact_productivity;

Department Ranking

SELECT
e.department,
AVG(p.productivity_score)
AS productivity_score
FROM fact_productivity p
JOIN dim_employee e
ON p.employee_id=e.employee_id
GROUP BY e.department
ORDER BY productivity_score DESC;

Overtime Cost Analysis

SELECT
department,
SUM(overtime_cost)
AS total_overtime_cost
FROM fact_finance f
JOIN dim_employee e
ON f.employee_id=e.employee_id
GROUP BY department
ORDER BY total_overtime_cost DESC;