DROP TABLE IF EXISTS users_mart;

CREATE TABLE user_mart AS 
SELECT 
	user_id , 
	MIN(event_datetime) as first_visit ,
	COUNT(DISTINCT session_id) as total_session , 
    SUM(CASE WHEN event_type = 'purchase' THEN 1 ELSE 0 END) AS total_orders,
    SUM(CASE WHEN event_type = 'purchase' THEN price ELSE 0 END) AS total_revenue
FROM staging_events
GROUP BY user_id;