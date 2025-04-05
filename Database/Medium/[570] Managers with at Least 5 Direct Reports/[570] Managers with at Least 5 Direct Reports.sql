/*
Accepted
570 [Medium]
Runtime: 318 ms, faster than 87.44% of PostgresQL online submissions for Managers with at Least 5 Direct Reports.
*/

-- Write your PostgreSQL query statement below
SELECT name
FROM Employee
WHERE id IN (
    SELECT managerId
    FROM Employee
    GROUP BY managerId HAVING COUNT(DISTINCT(id)) >= 5
)