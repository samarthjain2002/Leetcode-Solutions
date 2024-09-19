/*
Accepted
1068 [Easy]
*/

/*
Runtime: 1846 ms, faster than 8.94% of MySQL online submissions for Product Sales Analysis I.
*/

SELECT product_name, year, price
FROM Sales S, Product P
WHERE S.product_id = P.product_id

/*
JOIN (INNER JOIN)
Runtime: 1423 ms, faster than 26.26% of MySQL online submissions for Product Sales Analysis I.
*/

SELECT product_name, year, price
FROM Sales JOIN Product
ON Sales.product_id = Product.product_id

/*
LEFT JOIN
Runtime: 1210 ms, faster than 60.15% of MySQL online submissions for Product Sales Analysis I.
*/

SELECT product_name, year, price
FROM Sales LEFT JOIN Product
ON Sales.product_id = Product.product_id