/*
Accepted
1795 [Easy]
Runtime: 266 ms, faster than 65.67% of PostgreSQL online submissions for Rearrange Products Table.
*/
-- Write your PostgreSQL query statement below
SELECT 
    product_id,
    store,
    price
FROM 
    Products,
    UNNEST(ARRAY['store1', 'store2', 'store3']) WITH ORDINALITY AS s(store, ord)
    JOIN UNNEST(ARRAY[store1, store2, store3]) WITH ORDINALITY AS p(price, ord)
        ON s.ord = p.ord
WHERE 
    price IS NOT NULL;



/*
Runtime: 281 ms, faster than 61.94% of PostgreSQL online submissions for Rearrange Products Table.
*/
-- Write your PostgreSQL query statement below
SELECT 
    product_id, 
    store,
    price
FROM (
  SELECT 
    product_id, 
    UNNEST(ARRAY['store1', 'store2', 'store3']) AS store,
    UNNEST(ARRAY[store1, store2, store3]) AS price
  FROM 
    Products
) AS unpivot
WHERE price IS NOT NULL



/*
Runtime: 423 ms, faster than 31.53% of PostgreSQL online submissions for Rearrange Products Table.
*/
-- Write your PostgreSQL query statement below
SELECT product_id, 'store1' AS store, store1 as price
FROM Products
WHERE store1 IS NOT NULL
    UNION
SELECT product_id, 'store2' AS store, store2 as price
FROM Products
WHERE store2 IS NOT NULL
    UNION
SELECT product_id, 'store3' AS store, store3 as price
FROM Products
WHERE store3 IS NOT NULL