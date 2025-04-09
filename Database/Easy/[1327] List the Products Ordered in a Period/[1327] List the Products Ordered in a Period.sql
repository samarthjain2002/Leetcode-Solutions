/*
Accepted
1327 [Easy]
Runtime: 243 ms, faster than 72.92% of PostgreSQL online submissions for List the Products Ordered in a Period.
*/

-- Write your PostgreSQL query statement below
SELECT product_name, unit
FROM Products P INNER JOIN (
    SELECT product_id, SUM(unit) AS unit
    FROM Orders
    WHERE order_date BETWEEN DATE '2020-02-01' AND DATE '2020-03-01' - 1
    GROUP BY product_id HAVING SUM(unit) >= 100
) AS O
ON P.product_id = O.product_id 