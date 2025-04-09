/*
Accepted
185 [Hard]
Runtime: 298 ms, faster than 77.09% of PostgresQL online submissions for Department Top Three Salaries.
*/

-- Write your PostgreSQL query statement below
WITH
DenseRank AS (
    SELECT *, DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC)
    FROM Employee
),
TopThree AS (
    SELECT departmentId, MAX(dense_rank)
    FROM DenseRank
    WHERE dense_rank <= 3
    GROUP BY departmentId
)

SELECT DPT.name AS Department, DR.name AS Employee, salary
FROM DenseRank DR INNER JOIN Department DPT
ON DR.departmentId = DPT.id INNER JOIN TopThree T3
ON DR.departmentId = T3.departmentId
WHERE DR.dense_rank <= T3.max