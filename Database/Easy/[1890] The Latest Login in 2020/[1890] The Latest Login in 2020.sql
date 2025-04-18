/*
Accepted
1890 [Easy]
Runtime: 385 ms, faster than 76.38% of MySQL online submissions for The Latest Login in 2020.
*/

-- Write your PostgreSQL query statement below
SELECT user_id, MAX(time_stamp) AS last_stamp
FROM Logins
WHERE time_stamp >= '2020-01-01' AND time_stamp < '2021-01-01'
GROUP BY user_id