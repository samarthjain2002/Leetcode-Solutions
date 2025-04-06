/*
Accepted
1045 [Medium]
Runtime: 502 ms, faster than 99.65% of MySQL online submissions for Customers Who Bought All Products.
*/

# Write your MySQL query statement below
SELECT customer_id
FROM Customer
GROUP BY customer_id
HAVING COUNT(DISTINCT(product_key)) = (SELECT COUNT(*) FROM Product)