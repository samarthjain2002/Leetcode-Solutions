/*
Accepted
1873 [Easy]
Runtime: 302 ms, faster than 82.31% of PostgresQL online submissions for Calculate Special Bonus.
*/

-- Write your PostgreSQL query statement below
SELECT employee_id, CASE WHEN employee_id % 2 = 1 AND name NOT LIKE 'M%' THEN salary ELSE 0 END AS bonus
FROM Employees
ORDER BY employee_id