/*
Accepted
1341 [Medium]
Runtime: 299 ms, faster than 77.01% of PostgreSQL online submissions for Movie Rating.
*/

-- Write your PostgreSQL query statement below
(
    SELECT name AS results
    FROM Users U INNER JOIN (
        SELECT user_id, COUNT(*) AS number_of_ratings
        FROM MovieRating
        GROUP BY user_id
    ) AS RatingCount
    ON U.user_id = RatingCount.user_id
    ORDER BY number_of_ratings DESC, name
    LIMIT 1
)
UNION ALL
(
    SELECT title AS results
    FROM Movies
    WHERE movie_id = (
        SELECT Ratings.movie_id
        FROM Movies M INNER JOIN (
            SELECT movie_id, AVG(rating) AS average
            FROM MovieRating
            WHERE created_at BETWEEN DATE '2020-02-01' AND DATE '2020-03-01' - 1
            GROUP BY movie_id
        ) Ratings
        ON M.movie_id = Ratings.movie_id
        ORDER BY average DESC, title
        LIMIT 1
    )
);