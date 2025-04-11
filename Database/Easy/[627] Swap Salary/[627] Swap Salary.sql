/*
Accepted
627 [Easy]
Runtime: 201 ms, faster than 81.09% of PostgreSQL online submissions for Swap Salary.
*/

-- Write your PostgreSQL query statement below
UPDATE Salary
SET sex = CASE WHEN sex = 'f' THEN 'm' WHEN sex = 'm' THEN 'f' END