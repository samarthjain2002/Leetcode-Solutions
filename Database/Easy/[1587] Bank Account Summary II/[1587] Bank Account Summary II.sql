/*
Accepted
1587 [Easy]
Runtime: 344 ms, faster than 49.35% of PostgreSQL online submissions for Bank Account Summary II.
*/

-- Write your PostgreSQL query statement below
SELECT name, balance
FROM Users U INNER JOIN (
    SELECT account, SUM(amount) AS balance
    FROM Transactions
    GROUP BY account HAVING SUM(amount) > 10000
) AS T
ON U.account = T.account



/*
Runtime: 298 ms, faster than 59.64% of PostgreSQL online submissions for Bank Account Summary II.
*/
-- Write your PostgreSQL query statement below
SELECT name, SUM(amount) AS balance
FROM Users U INNER JOIN Transactions T
ON U.account = T.account
GROUP BY U.account, U.name HAVING SUM(amount) > 10000