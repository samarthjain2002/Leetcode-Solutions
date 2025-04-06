/*
Accepted
1731 [Medium]
Runtime: 306 ms, faster than 99.42% of MySQL online submissions for The Number of Employees Which Report to Each Employee.
*/

-- Write your PostgreSQL query statement below
WITH
Managers AS (
    SELECT reports_to AS manager, COUNT(*) AS reports_count, ROUND(AVG(age)) AS average_age
    FROM Employees
    GROUP BY reports_to
)

SELECT employee_id, name, reports_count, average_age
FROM Employees INNER JOIN Managers
ON employee_id = manager
ORDER BY employee_id