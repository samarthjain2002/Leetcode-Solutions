/*
Accepted
1204 [Medium]
Runtime: 471 ms, faster than 86.89% of MySQL online submissions for Last Person to Fit in the Bus.
*/

-- Write your PostgreSQL query statement below
WITH RunningWeight AS (
    SELECT *, SUM(weight) OVER (ORDER BY turn) AS running_weight
    FROM Queue
)

SELECT person_name
FROM RunningWeight
WHERE running_weight <= 1000
ORDER BY running_weight DESC
LIMIT 1;