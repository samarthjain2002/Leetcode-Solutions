/*
Accepted
584 [Easy]
Runtime: 429 ms, faster than 75.42% of MySQL online submissions for Find Customer Referee.
*/

/* Write your MySQL query statement below */
SELECT name FROM Customer WHERE referee_id != 2 OR referee_id IS null