/*
Accepted
1251 [Easy]
Runtime: 238 ms, faster than 81.67% of PostgresQL online submissions for Average Selling Price.
*/

-- Write your PostgreSQL query statement below
SELECT P.product_id, COALESCE(ROUND(SUM(price * units) / SUM(units)::NUMERIC, 2), 0) as average_price
FROM Prices P LEFT JOIN UnitsSold U
ON P.product_id = U.product_id AND purchase_date BETWEEN start_date AND end_date
GROUP BY P.product_id