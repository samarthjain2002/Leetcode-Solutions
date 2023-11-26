/*
Accepted
175 [Easy]
Runtime: 986 ms, faster than 43.17% of Oracle online submissions for Combine Two Tables.
*/

/* Write your PL/SQL query statement below */
SELECT P.firstName, P.lastName, A.city, A.state FROM Person P LEFT OUTER JOIN Address A ON P.personId = A.personID;