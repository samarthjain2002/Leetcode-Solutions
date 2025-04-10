/*
Accepted
1484 [Easy]
Runtime: 335 ms, faster than 80.92% of PostgresQL online submissions for Group Sold Products By The Date.
*/

-- Write your PostgreSQL query statement below
SELECT sell_date, COUNT(DISTINCT(product)) AS num_sold, STRING_AGG(DISTINCT product, ',' ORDER BY product) AS products
FROM Activities
GROUP BY sell_date
ORDER BY sell_date