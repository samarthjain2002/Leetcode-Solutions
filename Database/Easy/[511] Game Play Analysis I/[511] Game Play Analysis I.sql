/*
Accepted
511 [Easy]
Runtime: 517 ms, faster than 90.37% of Oracle online submissions for Game Play Analysis I.
*/

-- Write your PostgreSQL query statement below
SELECT player_id, MIN(event_date) AS first_login
FROM Activity
GROUP BY player_id