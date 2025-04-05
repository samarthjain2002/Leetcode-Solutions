/*
Accepted
1174 [Medium]
Runtime: 395 ms, faster than 88.40% of PostgresQL online submissions for Immediate Food Delivery II.
*/

-- Write your PostgreSQL query statement below
WITH 
FirstOrders AS (
    SELECT customer_id, MIN(order_date) AS first_order_date
    FROM Delivery
    GROUP BY customer_id
),
Customers AS (
    SELECT DISTINCT(customer_id)
    FROM Delivery
)

SELECT ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM Customers), 2) AS immediate_percentage
FROM Delivery D INNER JOIN FirstOrders F
ON D.customer_id = F.customer_id AND D.order_date = first_order_date
WHERE order_date = customer_pref_delivery_date