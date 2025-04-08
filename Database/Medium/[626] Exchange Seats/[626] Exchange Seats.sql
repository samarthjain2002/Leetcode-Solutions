/*
Accepted
626 [Medium]
Runtime: 183 ms, faster than 87.77% of PostgreSQL online submissions for Exchange Seats.
*/

-- Write your PostgreSQL query statement below
SELECT A.id, COALESCE(CASE WHEN A.id % 2 = 1 THEN B.student ELSE C.student END, (
    SELECT student
    FROM Seat
    WHERE id = (SELECT MAX(id) FROM Seat)
)) AS student
FROM Seat A LEFT JOIN Seat B
ON A.id = B.id - 1 LEFT JOIN Seat C
ON A.id = C.id + 1



/*
Runtime: 186 ms, faster than 85.13% of PostgreSQL online submissions for Exchange Seats.
*/
-- Write your PostgreSQL query statement below
SELECT 
    CASE
        WHEN id % 2 = 1 AND id + 1 IN (SELECT id FROM Seat) THEN id + 1
        WHEN id % 2 = 0 THEN id - 1
        ELSE id
    END AS id,
    student
FROM Seat
ORDER BY id;