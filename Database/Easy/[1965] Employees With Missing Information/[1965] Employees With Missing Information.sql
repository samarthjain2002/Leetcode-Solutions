/*
Accepted
1789 [Easy]
Runtime: 201 ms, faster than 88.11% of MySQL online submissions for Employees With Missing Information.
*/

-- Write your PostgreSQL query statement below
SELECT *
FROM (
    (   
        SELECT employee_id
        FROM Employees
        WHERE employee_id NOT IN (
            SELECT employee_id
            FROM Salaries
        )
    )
        UNION
    (
        SELECT employee_id
        FROM Salaries
        WHERE employee_id NOT IN (
            SELECT employee_id
            FROM Employees
        )
    )
)
ORDER BY employee_id