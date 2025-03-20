/*
Accepted
197 [Easy]
Runtime: 384 ms, faster than 62.94% of PostgreSQL online submissions for Rising Temperature.
*/

-- Write your PostgreSQL query statement below
SELECT A.id
FROM Weather A, Weather B
WHERE A.recordDate - 1 = B.recordDate AND A.temperature > B.temperature