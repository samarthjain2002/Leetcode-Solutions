/*
Accepted
1978 [Easy]
Runtime: 254 ms, faster than 72.16% of PostgreSQL online submissions for Employees Whose Manager Left the Company.
*/

-- Write your PostgreSQL query statement below
SELECT employee_id
FROM Employees
WHERE salary < 30000 AND manager_id NOT IN (
    SELECT employee_id
    FROM Employees
)
ORDER BY employee_id