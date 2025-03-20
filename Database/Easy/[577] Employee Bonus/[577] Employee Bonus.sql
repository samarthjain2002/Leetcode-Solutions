/*
Accepted
577 [Easy]
Runtime: 597 ms, faster than 46.41% of PostgreSQL online submissions for Employee Bonus.
*/

-- Write your PostgreSQL query statement below
SELECT name, bonus
FROM Employee E LEFT JOIN Bonus B
ON E.empId = B.empId
WHERE bonus < 1000 or bonus IS NULL;



/*
Runtime: 1694 ms, faster than 34.28% of Oracle online submissions for Employee Bonus.
*/

/* Write your PL/SQL query statement below */
SELECT Employee.name, Bonus.bonus
FROM Employee LEFT OUTER JOIN Bonus ON Employee.empId = Bonus.empId
WHERE bonus < 1000 OR bonus IS NULL;