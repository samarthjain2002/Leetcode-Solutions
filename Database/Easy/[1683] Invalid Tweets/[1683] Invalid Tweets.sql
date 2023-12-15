/*
Accepted
1683 [Easy]
Runtime: 1197 ms, faster than 36.72% of Oracle online submissions for Invalid Tweets.
*/

/* Write your PL/SQL query statement below */
SELECT tweet_id FROM Tweets
WHERE LENGTH(content) > 15;