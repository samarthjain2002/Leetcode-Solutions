/*
Accepted
1393 [Medium]
Runtime: 328 ms, faster than 92.91% of PostgreSQL online submissions for Capital GainLoss.
*/

-- Write your PostgreSQL query statement below
SELECT stock_name, SUM(price) FILTER (WHERE operation = 'Sell') - SUM(price) FILTER (WHERE operation = 'Buy') AS capital_gain_loss
FROM Stocks
GROUP BY stock_name