/*
Accepted
3497 [Medium]
Runtime: 271 ms, faster than 15.65% of PostgresQL online submissions for Analyze Subscription Conversion.
*/

-- Write your PostgreSQL query statement below
WITH
PaidSubscribers AS (
    SELECT DISTINCT user_id
    FROM UserActivity
    WHERE activity_type = 'paid'
),
TrialActivity AS (
    SELECT user_id, ROUND(AVG(activity_duration), 2) AS trial_avg_duration
    FROM UserActivity
    WHERE user_id IN (SELECT * FROM PaidSubscribers) AND activity_type = 'free_trial'
    GROUP BY user_id
),
PaidActivity AS (
    SELECT user_id, ROUND(AVG(activity_duration), 2) AS paid_avg_duration
    FROM UserActivity
    WHERE user_id IN (SELECT * FROM PaidSubscribers) AND activity_type = 'paid'
    GROUP BY user_id
)

SELECT A.user_id, trial_avg_duration, paid_avg_duration
FROM PaidSubscribers A INNER JOIN TrialActivity B
ON A.user_id = B.user_id INNER JOIN PaidActivity C
ON B. user_id = C.user_id