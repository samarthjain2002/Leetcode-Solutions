/*
Accepted
183 [Easy]
Runtime: 251 ms, faster than 81.88% of Oracle online submissions for Customers Who Never Order.
*/

-- Write your PostgreSQL query statement below
SELECT name AS Customers
FROM Customers
WHERE id NOT IN (
    SELECT customerId
    FROM Orders
)