/*
Accepted
1050 [Easy]
Runtime: 290 ms, faster than 94.84% of PostgreSQL online submissions for Actors and Directors Who Cooperated At Least Three Times.
*/

-- Write your PostgreSQL query statement below
SELECT actor_id, director_id
FROM ActorDirector
GROUP BY actor_id, director_id HAVING COUNT(*) >= 3