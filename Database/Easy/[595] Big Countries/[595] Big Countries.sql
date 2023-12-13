/*
Accepted
595 [Easy]
Runtime: 447 ms, faster than 67.40% of Oracle online submissions for Big Countries.
*/

# Write your MySQL query statement below
SELECT name, population, area FROM World WHERE area >= 3000000 OR population >= 25000000;