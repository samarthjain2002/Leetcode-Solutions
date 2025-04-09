/*
Accepted
1517 [Easy]
Runtime: 298 ms, faster than 77.09% of PostgresQL online submissions for Find Users With Valid E-Mails.
*/

-- Write your PostgreSQL query statement below
SELECT *
FROM Users
WHERE mail ~ '^[a-zA-Z]+[a-zA-Z0-9_.-]*@leetcode\.com$'