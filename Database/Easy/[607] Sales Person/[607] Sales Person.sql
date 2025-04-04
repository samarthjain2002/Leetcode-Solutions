/*
Accepted
607 [Easy]
Runtime: 333 ms, faster than 92.61% of PostgresQL online submissions for Sales Person.
*/

-- Write your PostgreSQL query statement below
SELECT name
FROM SalesPerson
WHERE sales_id NOT IN (
    SELECT sales_id
    FROM Orders
    WHERE com_id = (
        SELECT com_id
        FROM Company
        WHERE name = 'RED'
    )
)