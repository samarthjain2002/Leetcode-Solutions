/*
Accepted
1407 [Easy]
Runtime: 320 ms, faster than 77.56% of PostgreSQL online submissions for Top Travellers.
*/

-- Write your PostgreSQL query statement below
SELECT name, COALESCE(SUM(distance), 0) AS travelled_distance
FROM Users U LEFT JOIN Rides R
ON U.id = R.user_id
GROUP BY name, U.id
ORDER BY travelled_distance DESC, name