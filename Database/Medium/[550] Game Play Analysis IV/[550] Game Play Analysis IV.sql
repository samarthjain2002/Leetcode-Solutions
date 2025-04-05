/*
Accepted
550 [Medium]
Runtime: 469 ms, faster than 99.79% of PostgresQL online submissions for Game Play Analysis IV.
*/

-- Write your PostgreSQL query statement below
WITH 
FirstLogin AS (
    SELECT player_id, MIN(event_date) AS first_login
    FROM Activity
    GROUP BY player_id
),
Players AS (
    SELECT DISTINCT(player_id)
    FROM Activity
)

SELECT ROUND(COUNT(*) / (SELECT COUNT(*) FROM Players)::NUMERIC, 2) as fraction
FROM Activity A INNER JOIN FirstLogin F
ON A.player_id = F.player_id AND event_date = first_login + 1