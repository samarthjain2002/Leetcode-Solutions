/*
Accepted
596 [Easy]
Runtime: 638 ms, faster than 24.41% of PostgresQL online submissions for Classes More Than 5 Students.
*/

-- Write your PostgreSQL query statement below
SELECT class
FROM Courses
GROUP BY class HAVING COUNT(*) >= 5