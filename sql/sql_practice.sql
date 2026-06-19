#1.统计行为分布( df["behavior_type"].value_counts() ) (cnt=COUNT)
SELECT
    behavior_type,
    COUNT(*) AS cnt
FROM dwd_user_behavior
GROUP BY behavior_type
ORDER BY cnt DECS;

#2.Top10热门商品
SELECT 
    item_id,
    COUNT(*) AS cnt
FROM dwd_user_behavior
GROUP BY item_id
ORDER BY cnt DESC
LIMIT 10;

#3.Top10热门品类
SELECT
    category_id,
    COUNT(*) AS cnt
FROM dwd_user_behavior
GROUP BY category_id
ORDER BY cnt DECS
LIMIT 10;

#4.购买用户数
SELECT 
    COUNT(DISTINCT user_id)
FROM dwd_user_behavior
WHERE behavior_type="buy";

#5.浏览用户数
SELECT
    COUNT(DISTINCT user_id)
FROM dwd_user_behavior
WHERE behavior_type='pv';

#6.高价值用户数量
SELECT COUNT(*)
FROM dws_user_profile
WHERE user_level='高价值用户';

#7.用户分层统计
SELECT
    user_level,
    COUNT(*) AS user_cnt
FROM dws_user_profile
GROUP BY user_level;

#8.转化率
SELECT *
FROM ads_conversion;

#9.购买次数最多的用户
SELECT
    user_id,
    buy_count
FROM dws_user_profile
ORDER BY buy_count DESC
LIMIT 10;

#10.浏览最多的用户
SELECT
    user_id,
    pv_count
FROM dws_user_profile
ORDER BY pv_count DESC
LIMIT 10;

SELECT COUNT(*) FROM dwd_user_behavior;