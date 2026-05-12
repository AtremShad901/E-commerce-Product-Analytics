DROP TABLE IF EXISTS staging_events;

CREATE TABLE staging_events AS 
SELECT 
	user_id , 
	session_id , 
	event_type , 
	product_id , 
	category , 
	CAST(price AS REAL ) AS price , 
	device , 
	traffic_source , 
	country,
	city ,
	datetime(event_date) as event_datetime
FROM raw_events