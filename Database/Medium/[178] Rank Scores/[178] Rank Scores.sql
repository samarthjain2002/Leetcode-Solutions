/*
Accepted
178 [Medium]
Runtime: 252 ms, faster than 71.08% of PostgresQL online submissions for Rank Scores.
*/

-- Write your PostgreSQL query statement below
SELECT score, DENSE_RANK() OVER (ORDER BY score DESC) AS rank
FROM Scores