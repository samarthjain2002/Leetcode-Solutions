/*
Accepted
1661 [Easy]
Runtime: 164 ms, faster than 93.59% of Oracle online submissions for Average Time of Process per Machine.
*/

-- Write your PostgreSQL query statement below
SELECT A.machine_id, ROUND(AVG(B.timestamp - A.timestamp)::NUMERIC, 3) AS processing_time
FROM Activity A INNER JOIN Activity B
ON A.machine_id = B.machine_id AND A.process_id = B.process_id
WHERE A.activity_type = 'start' AND B.activity_type = 'end'
GROUP BY A.machine_id



/*
Runtime: 172 ms, faster than 89.13% of Oracle online submissions for Average Time of Process per Machine.
*/

-- Write your PostgreSQL query statement below
SELECT machine_id, ROUND((SUM(timeTaken) / COUNT(timeTaken))::NUMERIC, 3) AS processing_time
FROM (
    SELECT A.machine_id, B.timestamp - A.timestamp AS timeTaken
    FROM Activity A INNER JOIN Activity B
    ON A.machine_id = B.machine_id AND A.process_id = B.process_id
    WHERE A.activity_type = 'start' AND B.activity_type = 'end'
)
GROUP BY machine_id
