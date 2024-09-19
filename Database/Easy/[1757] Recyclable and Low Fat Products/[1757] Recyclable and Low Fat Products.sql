/*
Accepted
1757 [Easy]
Runtime: 463 ms, faster than 79.41% of MySQL online submissions for Recyclable and Low Fat Products.
*/

/* Write your MySQL query statement below */
SELECT product_id FROM Products WHERE low_fats = 'Y' AND recyclable = 'Y'