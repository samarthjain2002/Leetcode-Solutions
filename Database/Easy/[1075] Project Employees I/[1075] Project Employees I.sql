/*
Accepted
1075 [Easy]
Runtime: 564 ms, faster than 76.00% of PostgresQL online submissions for Project Employees I.
*/

-- Write your PostgreSQL query statement below
SELECT project_id, ROUND(AVG(experience_years), 2) as average_years
FROM Project P INNER JOIN Employee E
ON P.employee_id = E.employee_id
GROUP BY project_id
ORDER BY P.project_id