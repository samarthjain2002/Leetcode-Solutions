/*
Accepted
1158 [Medium]
Runtime: 509 ms, faster than 96.22% of PostgreSQL online submissions for Market Analysis I.
*/

-- Write your PostgreSQL query statement below
WITH
OrdersIn2019 AS (
    SELECT buyer_id, COUNT(*) AS orders_in_2019
    FROM Orders
    WHERE order_date BETWEEN '2019-01-01' AND '2019-12-31'
    GROUP BY buyer_id
)

SELECT U.user_id AS buyer_id, U.join_date, COALESCE(O.orders_in_2019, 0) AS orders_in_2019
FROM Users U LEFT JOIN OrdersIn2019 O
ON U.user_id = O.buyer_id