/*
Accepted
586 [Easy]
Runtime: 233 ms, faster than 97.74% of Oracle online submissions for Customer Placing the Largest Number of Orders.
*/

-- Write your PostgreSQL query statement below
SELECT customer_number
FROM Orders
GROUP BY customer_number
ORDER BY COUNT(order_number) DESC
LIMIT 1;