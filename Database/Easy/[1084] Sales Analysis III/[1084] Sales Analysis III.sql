/*
Accepted
1084 [Easy]
Runtime: 935 ms, faster than 88.41% of PostgresQL online submissions for Sales Analysis III.
*/

-- Write your PostgreSQL query statement below
SELECT product_id, product_name
FROM Product
WHERE product_id IN (
    SELECT product_id
    FROM Sales
    WHERE sale_date BETWEEN '2019-01-01' AND '2019-03-31'
) AND product_id NOT IN (
    SELECT product_id
    FROM Sales
    WHERE sale_date NOT BETWEEN '2019-01-01' AND '2019-03-31' 
)