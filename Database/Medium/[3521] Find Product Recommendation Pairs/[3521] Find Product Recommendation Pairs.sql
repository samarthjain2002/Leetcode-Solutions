/*
Accepted
3521 [Medium]
Runtime: 347 ms, faster than 30.53% of PostgresQL online submissions for Find Product Recommendation Pairs.
*/

-- Write your PostgreSQL query statement below
SELECT product1_id, product2_id, A.category AS product1_category, B.category AS product2_category, customer_count
FROM (
    SELECT A.product_id AS product1_id, B.product_id AS product2_id, COUNT(*) AS customer_count
    FROM ProductPurchases A INNER JOIN ProductPurchases B
    ON A.user_id = B.user_id AND A.product_id < B.product_id
    GROUP BY A.product_id, B.product_id
    HAVING COUNT(*) >= 3
) AS subq INNER JOIN ProductInfo A ON subq.product1_id = A.product_id
INNER JOIN ProductInfo B ON subq.product2_id = B.product_id
ORDER BY 5 DESC, 1, 2
