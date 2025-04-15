/*
Accepted
1693 [Easy]
Runtime: 321 ms, faster than 59.67% of PostgresQL online submissions for Daily Leads and Partners.
*/

-- Write your PostgreSQL query statement below
SELECT date_id, make_name, COUNT(DISTINCT(lead_id)) AS unique_leads, COUNT(DISTINCT(partner_id)) AS unique_partners
FROM DailySales
GROUP BY date_id, make_name