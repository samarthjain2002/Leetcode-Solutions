/*
Accepted
1148 [Easy]
Runtime: 1305 ms, faster than 5.02% of Oracle online submissions for Article Views I.
*/

/* Write your MySQL query statement below */
SELECT DISTINCT author_id AS id
FROM Views WHERE author_id=viewer_id
ORDER BY id;