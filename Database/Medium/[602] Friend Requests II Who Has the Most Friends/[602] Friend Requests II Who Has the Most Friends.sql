/*
Accepted
602 [Medium]
Runtime: 330 ms, faster than 80.12% of MySQL online submissions for Friend Requests II Who Has the Most Friends.
*/

# Write your MySQL query statement below
WITH CTE1 AS (
    SELECT requester_id AS person_id
    FROM RequestAccepted
    UNION ALL
    SELECT accepter_id AS person_id
    FROM RequestAccepted
)

SELECT person_id AS id, COUNT(person_id) AS num
FROM CTE1
GROUP BY person_id
ORDER BY COUNT(person_id) DESC
LIMIT 1