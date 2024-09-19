/*
Accepted
1683 [Easy]
Runtime: 577 ms, faster than 54.46% of MySQL online submissions for Invalid Tweets.
*/

/* Write your MySQL query statement below */
SELECT tweet_id
FROM Tweets
WHERE LENGTH(content) > 15;