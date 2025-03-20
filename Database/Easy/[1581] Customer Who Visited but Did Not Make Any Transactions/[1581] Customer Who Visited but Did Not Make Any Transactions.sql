/*
Accepted
1581 [Easy]
Runtime: 3316 ms, faster than 5.01% of PostgreSQL online submissions for Customer Who Visited but Did Not Make Any Transactions.
*/
-- Write your PostgreSQL query statement below
SELECT customer_id, COUNT(V.visit_id) AS count_no_trans
FROM Visits V LEFT JOIN Transactions T
ON V.visit_id = T.visit_id
WHERE T.visit_id IS NULL
GROUP BY customer_id;