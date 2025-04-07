/*
Accepted
1789 [Easy]
Runtime: 515 ms, faster than 96.84% of MySQL online submissions for Primary Department for Each Employee.
*/

# Write your MySQL query statement below
SELECT employee_id, department_id
FROM Employee
GROUP BY employee_id HAVING COUNT(*) = 1
    UNION
SELECT employee_id, department_id
FROM Employee
WHERE primary_flag = 'Y'