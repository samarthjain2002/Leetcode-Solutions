/*
Accepted
176 [Medium]
Runtime: 206 ms, faster than 84.65% of PostgresQL online submissions for Second Highest Salary.
*/

-- Write your PostgreSQL query statement below
SELECT CASE WHEN COUNT(salary) = 2 THEN MIN(salary) ELSE NULL END AS SecondHighestSalary
FROM (
    SELECT salary
    FROM Employee
    GROUP BY salary
    ORDER BY salary DESC
    LIMIT 2
)