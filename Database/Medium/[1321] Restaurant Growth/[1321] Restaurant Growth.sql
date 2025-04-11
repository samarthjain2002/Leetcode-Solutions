/*
Accepted
1321 [Medium]
Runtime: 189 ms, faster than 83.42% of PostgreSQL online submissions for Restaurant Growth.
*/

-- Write your PostgreSQL query statement below
WITH
CTE1 AS (
    SELECT *, SUM(amount) OVER (ORDER BY visited_on) AS running_amount
    FROM Customer
)


SELECT *
FROM (
    (
        SELECT visited_on, AVG(running_amount) AS amount,
        ROUND(AVG(running_amount) / 7.0, 2) AS average_amount
        FROM CTE1
        WHERE visited_on - 6 = (
            SELECT MIN(visited_on)
            FROM CTE1
        )
        GROUP BY visited_on
    )
    UNION
    (
        SELECT A.visited_on, AVG(A.running_amount) - AVG(B.running_amount) AS amount,
        ROUND((AVG(A.running_amount) - AVG(B.running_amount)) / 7.0, 2) AS average_amount
        FROM CTE1 A INNER JOIN CTE1 B
        ON A.visited_on - 7 = B.visited_on
        GROUP BY A.visited_on
        ORDER BY A.visited_on
    )
)
ORDER BY visited_on