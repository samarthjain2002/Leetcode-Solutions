/*
Accepted
584 [Easy]
Runtime: 1020 ms, faster than 48.25% of Oracle online submissions for Find Customer Referee.
*/

/* Write your PL/SQL query statement below */
SELECT name FROM Customer WHERE referee_id!=2 OR referee_id IS null;