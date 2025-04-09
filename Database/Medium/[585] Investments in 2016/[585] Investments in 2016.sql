/*
Accepted
585 [Medium]
Runtime: 256 ms, faster than 88.46% of PostgresQL online submissions for Investments in 2016.
*/

-- Write your PostgreSQL query statement below
SELECT ROUND(SUM(tiv_2016)::NUMERIC, 2) AS tiv_2016
FROM Insurance
WHERE tiv_2015 IN (SELECT tiv_2015 FROM Insurance GROUP BY 1 HAVING COUNT(*) > 1)
AND (lat, lon) IN (SELECT lat, lon FROM Insurance GROUP BY lat, lon HAVING COUNT(*) = 1)