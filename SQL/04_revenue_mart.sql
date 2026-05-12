DROP TABLE IF EXISTS revenue_mart;

CREATE TABLE revenue_mart AS
SELECT
    user_id,
    COUNT(*) AS total_orders,
    SUM(price) AS total_revenue,
    AVG(price) AS avg_order_value
FROM staging_events
WHERE event_type = 'purchase'
GROUP BY user_id;