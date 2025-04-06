/*
Accepted
619 [Easy]
Runtime: 188 ms, faster than 94.70% of PostgresQL online submissions for Biggest Single Number.
*/

-- Write your PostgreSQL query statement below
SELECT MAX(num) AS num
FROM (
    SELECT num
    FROM MyNumbers
    GROUP BY num HAVING COUNT(*) = 1
);