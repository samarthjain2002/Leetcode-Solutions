/*
Accepted
1280 [Easy]
Runtime: 1305 ms, faster than 5.02% of Oracle online submissions for Students and Examinations.
*/

-- Write your PostgreSQL query statement below
SELECT S.student_id, S.student_name, S.subject_name, COUNT(E.subject_name) AS attended_exams
FROM (
    SELECT *
    FROM Students CROSS JOIN Subjects
) AS S LEFT JOIN Examinations E ON S.student_id = E.student_id AND S.subject_name = E.subject_name
GROUP BY 1, 2, 3
ORDER BY 1, 3