/*
Accepted
1164 [Medium]
Runtime: 359 ms, faster than 91.10% of MySQL online submissions for Product Price at a Given Date.
*/

-- Write your PostgreSQL query statement below
WITH 
Changes AS (
    SELECT product_id, MAX(change_date) as change_date
    FROM Products
    WHERE change_date <= DATE '2019-08-16'
    GROUP BY product_id
)

SELECT P.product_id, new_price AS price
FROM Products P INNER JOIN Changes C
ON P.product_id = C.product_id AND P.change_date = C.change_date
    UNION
SELECT product_id, 10
FROM Products
WHERE product_id NOT IN (SELECT product_id FROM Changes)