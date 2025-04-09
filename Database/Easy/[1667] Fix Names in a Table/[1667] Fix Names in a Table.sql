/*
Accepted
1667 [Easy]
Runtime: 449 ms, faster than 78.84% of PostgresQL online submissions for Fix Names in a Table.
*/

-- Write your PostgreSQL query statement below
SELECT user_id, CONCAT(UPPER(SUBSTRING(name FROM 1 FOR 1)), LOWER(SUBSTRING(name FROM 2))) AS name
FROM Users
ORDER BY user_id