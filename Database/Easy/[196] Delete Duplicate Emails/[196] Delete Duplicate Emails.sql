/*
Accepted
196 [Easy]
Runtime: 250 ms, faster than 87.85% of Oracle online submissions for Delete Duplicate Emails.
*/

-- Write your PostgreSQL query statement below
DELETE FROM Person
WHERE id IN (
    SELECT id FROM (
        SELECT A.id
        FROM Person A INNER JOIN Person B
        ON A.email = B.email
        WHERE A.id > B.id
    ) AS subquery
)