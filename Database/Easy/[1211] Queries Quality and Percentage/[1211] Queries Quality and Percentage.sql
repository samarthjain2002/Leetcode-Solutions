/*
Accepted
1211 [Easy]
Runtime: 221 ms, faster than 95.47% of PostgresQL online submissions for Queries Quality and Percentage.
*/

-- Write your PostgreSQL query statement below
SELECT query_name, 
ROUND(AVG(rating / position::NUMERIC), 2) AS quality, 
ROUND(COUNT(*) FILTER (WHERE rating < 3) / COUNT(*)::NUMERIC * 100, 2) AS poor_query_percentage
FROM Queries
GROUP BY query_name