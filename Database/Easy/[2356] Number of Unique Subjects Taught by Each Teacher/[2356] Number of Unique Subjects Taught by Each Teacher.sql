/*
Accepted
2356 [Easy]
Runtime: 510 ms, faster than 97.88% of PostgresQL online submissions for Number of Unique Subjects Taught by Each Teacher.
*/

-- Write your PostgreSQL query statement below
SELECT teacher_id, COUNT(DISTINCT(subject_id)) as cnt
FROM Teacher
GROUP BY teacher_id