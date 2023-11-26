/*
Accepted
577 [Easy]
Runtime: 1694 ms, faster than 34.28% of Oracle online submissions for Employee Bonus.
*/

/* Write your PL/SQL query statement below */
SELECT Employee.name, Bonus.bonus
FROM Employee LEFT OUTER JOIN Bonus ON Employee.empId = Bonus.empId
WHERE bonus < 1000 OR bonus IS NULL;