/*
Accepted
1757 [Easy]
Runtime: 1348 ms, faster than 22.01% of Oracle online submissions for Recyclable and Low Fat Products.
*/

/* Write your PL/SQL query statement below */
SELECT product_id FROM Products WHERE low_fats='Y' and recyclable='Y';