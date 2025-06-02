/*
Accepted
3570 [Easy]
Runtime: 227 ms, faster than 100.00% of PostgresQL online submissions for Find Books with No Available Copies.
*/

-- Write your PostgreSQL query statement below
WITH not_returned AS (
    SELECT book_id, COUNT(*) AS total_copies_borrowed
    FROM borrowing_records
    WHERE return_date IS NULL
    GROUP BY book_id
)

SELECT L.book_id, title, author, genre, publication_year, total_copies AS current_borrowers
FROM library_books L INNER JOIN not_returned N
ON L.book_id = N.book_id
WHERE L.total_copies = N.total_copies_borrowed
ORDER BY current_borrowers DESC, title