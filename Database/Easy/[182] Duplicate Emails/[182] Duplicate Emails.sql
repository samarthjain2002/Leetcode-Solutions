/*
Accepted
182 [Easy]
Runtime: 205 ms, faster than 97.46% of Oracle online submissions for Duplicate Emails.
*/

-- Write your PostgreSQL query statement below
SELECT DISTINCT A.email as Email
FROM Person A JOIN Person B
ON A.email = B.email AND A.id != B.id