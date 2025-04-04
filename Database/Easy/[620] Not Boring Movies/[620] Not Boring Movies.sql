/*
Accepted
620 [Easy]
Runtime: 237 ms, faster than 74.92% of PostgresQL online submissions for Not Boring Movies.
*/

-- Write your PostgreSQL query statement below
SELECT *
FROM Cinema
WHERE id % 2 != 0 AND description != 'boring'
ORDER BY rating DESC;