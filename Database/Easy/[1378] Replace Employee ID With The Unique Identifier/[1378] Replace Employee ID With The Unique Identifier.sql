/*
Accepted
1378 [Easy]
Runtime: 1004 ms, faster than 84.98% of MySQL online submissions for Replace Employee ID With The Unique Identifier.
*/

/* Write your MySQL query statement below */
SELECT unique_id, name
FROM Employees E LEFT JOIN EmployeeUNI EU
ON E.id = EU.id