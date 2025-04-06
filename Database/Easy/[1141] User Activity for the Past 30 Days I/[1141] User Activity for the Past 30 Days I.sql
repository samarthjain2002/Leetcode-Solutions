/*
Accepted
1141 [Easy]
Runtime: 395 ms, faster than 83.10% of PostgresQL online submissions for User Activity for the Past 30 Days I.
*/

-- Write your PostgreSQL query statement below
SELECT activity_date AS day, COUNT(DISTINCT(user_id)) as active_users
FROM Activity
WHERE activity_date BETWEEN DATE '2019-07-27' - 29 AND DATE '2019-07-27'
GROUP BY activity_date