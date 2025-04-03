/*
Accepted
1934 [Medium]
Runtime: 228 ms, faster than 99.02% of PostgresQL online submissions for Confirmation Rate.
*/

-- Write your PostgreSQL query statement below
SELECT S.user_id, ROUND(
    AVG(CASE WHEN action = 'confirmed' THEN 1 ELSE 0 END)::NUMERIC, 2
 ) AS confirmation_rate
FROM Signups S LEFT JOIN Confirmations C
ON S.user_id = C.user_id
GROUP BY S.user_id



/*
Runtime: 986 ms, faster than 43.17% of PostgresQL online submissions for Confirmation Rate.
*/

-- Write your PostgreSQL query statement below
SELECT S.user_id, COALESCE(
    ROUND(COUNT(action) FILTER (WHERE action = 'confirmed')::NUMERIC / NULLIF(COUNT(action), 0), 2), 0
 ) AS confirmation_rate
FROM Signups S LEFT JOIN Confirmations C
ON S.user_id = C.user_id
GROUP BY S.user_id