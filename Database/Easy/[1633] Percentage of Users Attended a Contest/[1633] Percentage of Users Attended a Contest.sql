/*
Accepted
1633 [Easy]
Runtime: 884 ms, faster than 99.52% of PostgresQL online submissions for Percentage of Users Attended a Contest.
*/

-- Write your PostgreSQL query statement below
SELECT contest_id, ROUND((COUNT(*) / (SELECT COUNT(*) FROM Users)::NUMERIC) * 100, 2) AS percentage
FROM Register
GROUP BY contest_id
ORDER BY percentage DESC, contest_id;