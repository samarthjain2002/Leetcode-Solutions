/*
Accepted
1729 [Easy]
Runtime: 520 ms, faster than 95.13% of MySQL online submissions for Find Followers Count.
*/

# Write your  query statement below
SELECT user_id, COUNT(*) AS followers_count
FROM Followers
GROUP BY user_id
ORDER BY user_id