/* To view all data */
SELECT *
 FROM subscriptions
 LIMIT 20;
 
 /* segments in dataset */
 SELECT DISTINCT segment
 FROM subscriptions;
 
 /* first sub, latest sub, latest cancel */
 SELECT  MIN(subscription_start) AS earliest_sub,
 MAX(subscription_start) AS latest_sub, MAX(subscription_end) AS latest_cancel
 FROM subscriptions;

/* Range of months in data */
SELECT MIN(subscription_start) AS earliest_start, 
MAX(subscription_start) AS latest_start
FROM subscriptions;

/* Churn rate code */
WITH months AS 
(select 
'2017-01-01' as first_day,
  '2017-01-31' as last_day
  UNION
 select 
'2017-02-01' as first_day,
  '2017-02-28' as last_day
UNION
select 
'2017-03-01' as first_day,
  '2017-03-31' as last_day
  ),
cross_join AS
(SELECT * FROM subscriptions 
cross join months),
status AS 
(select id,first_day AS month,
CASE
   WHEN (subscription_start < first_day) AND 
   (subscription_end > first_day OR subscription_end IS NULL) and (segment = 87)
   THEN 1 
   ELSE 0 
END AS is_active_87,
CASE 
   WHEN (subscription_start < first_day) AND 
   (subscription_end > first_day OR subscription_end IS NULL) AND (segment = 30) 
   THEN 1   
   ELSE 0
END AS is_active_30,
CASE 
   WHEN (subscription_end BETWEEN first_day AND last_day) AND (segment = 87)
   THEN 1 
   ELSE 0
END AS is_canceled_87,
CASE 
   WHEN (subscription_end BETWEEN first_day AND last_day) AND (segment = 30)
   THEN 1 
   ELSE 0
END AS is_canceled_30
FROM cross_join),
status_aggregate AS 
(SELECT month,
  sum(is_active_87) as sum_active_87,
  sum(is_active_30) as sum_active_30,
  sum(is_canceled_87) as sum_canceled_87,
  sum(is_canceled_30) as sum_canceled_30
FROM status
GROUP BY month)
SELECT month, 
1.0*sum_canceled_87/sum_active_87 as churn_rate_87,
1.0*sum_canceled_30/sum_active_30 as churn_rate_30
FROM status_aggregate;
