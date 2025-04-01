/*
Accepted
181 [Easy]
Runtime: 1305 ms, faster than 5.02% of Oracle online submissions for Employees Earning More Than Their Managers.
*/

-- Write your PostgreSQL query statement below
SELECT A.name AS Employee
FROM Employee A JOIN Employee B ON A.managerId = B.id
WHERE A.salary > B.salary