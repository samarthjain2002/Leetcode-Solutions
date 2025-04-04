/*
Accepted
610 [Easy]
Runtime: 172 ms, faster than 98.00% of PostgresQL online submissions for Triangle Judgement.
*/

-- Write your PostgreSQL query statement below
SELECT *, CASE WHEN x + y > z AND y + z > x AND z + x > y THEN 'Yes' ELSE 'No' END AS triangle
FROM Triangle