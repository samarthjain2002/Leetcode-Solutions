/*
Accepted
184 [Medium]
Runtime: 242 ms, faster than 84.91% of PostgreSQL online submissions for Department Highest Salary.
*/

-- Write your PostgreSQL query statement below
SELECT D.name AS Department, E.name AS Employee, E.salary AS Salary
FROM Department D INNER JOIN (
    SELECT *, RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS rank
    FROM Employee
) AS E
ON D.id = E.departmentId
WHERE rank = 1