/*
Accepted
3436 [Easy]
Runtime: 172 ms, faster than 77.38% of PostgresQL online submissions for Find Valid Emails.
*/

-- Write your PostgreSQL query statement below
SELECT *
FROM Users
WHERE email ~* '^[a-z0-9_]+@[a-z]+\.com$'
ORDER BY user_id