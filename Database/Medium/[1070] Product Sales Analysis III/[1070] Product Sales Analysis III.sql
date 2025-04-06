/*
Accepted
1070 [Medium]
Runtime: 1391 ms, faster than 71.49% of MySQL online submissions for Product Sales Analysis III.
*/

# Write your MySQL query statement below
WITH
FirstYear AS (
    SELECT product_id, MIN(year) AS first_year
    FROM Sales
    GROUP BY product_id
)

SELECT product_id, year AS first_year, quantity, price
FROM Sales
WHERE (product_id, year) IN (SELECT * FROM FirstYear)