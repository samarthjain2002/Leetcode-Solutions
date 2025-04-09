/*
Accepted
1527 [Easy]
Runtime: 273 ms, faster than 57.01% of PostgreSQL online submissions for Patients With a Condition.
*/

-- Write your PostgreSQL query statement below
SELECT patient_id, patient_name, conditions
FROM Patients
WHERE conditions LIKE 'DIAB1%' OR conditions LIKE '% DIAB1%';