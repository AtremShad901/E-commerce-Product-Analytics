DROP TABLE IF EXISTS sessions_mart ;

CREATE TABLE sessions_mart AS
SELECT
    session_id,
    user_id,
    event_datetime,
    MAX(CASE WHEN event_type = 'purchase' THEN 1 ELSE 0 END) AS converted
FROM staging_events
GROUP BY session_id, user_id;