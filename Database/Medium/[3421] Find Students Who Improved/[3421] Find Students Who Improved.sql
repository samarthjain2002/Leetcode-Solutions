/*
Accepted
3421 [Medium]
Runtime: 206 ms, faster than 53.17% of PostgresQL online submissions for Find Students Who Improved.
*/

-- Write your PostgreSQL query statement below
WITH first_last AS (
    SELECT DISTINCT ON (student_id, subject)
        student_id,
        subject,
        FIRST_VALUE(score) OVER (PARTITION BY student_id, subject ORDER BY exam_date) AS first_score,
        FIRST_VALUE(score) OVER (PARTITION BY student_id, subject ORDER BY exam_date DESC) AS latest_score
    FROM Scores
)
SELECT *
FROM first_last
WHERE latest_score > first_score
ORDER BY student_id, subject;