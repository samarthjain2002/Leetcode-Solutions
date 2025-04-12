/*
Accepted
262 [Hard]
Runtime: 186 ms, faster than 89.40% of PostgresQL online submissions for Trips and Users.
*/

-- Write your PostgreSQL query statement below
SELECT request_at AS Day, ROUND(COUNT(*) FILTER (WHERE status != 'completed') / COUNT(*)::NUMERIC, 2) AS "Cancellation Rate"
FROM Trips T INNER JOIN Users UC
ON T.client_id = UC.users_id INNER JOIN Users UD
ON T.driver_id = UD.users_id
WHERE UC.banned = 'No' AND UD.banned = 'No' AND request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY request_at



/*
Runtime: 181 ms, faster than 96.41% of PostgresQL online submissions for Trips and Users.
*/

-- Write your PostgreSQL query statement below
WITH
CTE1 AS (
    SELECT *
    FROM Trips T INNER JOIN Users UC
    ON T.client_id = UC.users_id INNER JOIN Users UD
    ON T.driver_id = UD.users_id
    WHERE UC.banned = 'No' AND UD.banned = 'No'
)

SELECT request_at AS Day, ROUND(COUNT(*) FILTER (WHERE status != 'completed') / COUNT(*)::NUMERIC, 2) AS "Cancellation Rate"
FROM CTE1
WHERE request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY request_at