/*
Accepted
177 [Medium]
Runtime: 228 ms, faster than 78.48% of PostgreSQL online submissions for Nth Highest Salary.
*/

CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN
  RETURN QUERY (
    -- Write your PostgreSQL query statement below.
    SELECT SubQuery.salary
    FROM (
        SELECT Employee.salary, DENSE_RANK() OVER (ORDER BY Employee.salary DESC) AS rank
        FROM Employee
    ) AS SubQuery
    WHERE SubQuery.rank = N
    LIMIT 1
  );
END;
$$ LANGUAGE plpgsql;