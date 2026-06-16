# 淘宝用户行为分析项目设计文档

## 项目背景

基于淘宝用户行为数据集，对用户浏览、收藏、加购和购买行为进行分析，构建用户画像、商品排行及转化率指标。

---

## 技术栈

* Python
* Pandas
* SQLite
* SQL
* Streamlit
* Git/GitHub

---

## 项目架构

UserBehavior.csv

↓

ODS（原始数据层）

↓

DWD（明细数据层）

↓

DWS（用户画像层）

↓

ADS（指标应用层）

↓

SQLite

↓

Streamlit Dashboard

---

## ODS层

存储原始业务数据：

* ods_user_behavior.csv

---

## DWD层

完成：

* 时间格式转换
* 数据过滤
* 数据清洗

输出：

* dwd_user_behavior.csv

---

## DWS层

构建用户画像：

* pv_count
* fav_count
* cart_count
* buy_count
* is_buyer
* user_level

输出：

* dws_user_profile.csv

---

## ADS层

生成分析指标：

* 商品排行榜
* 品类排行榜
* 转化率指标

输出：

* ads_top_item.csv
* ads_top_category.csv
* ads_conversion.csv

---

## 数据库设计

SQLite数据库：

ecommerce.db

数据表：

* dwd_user_behavior
* dws_user_profile
* ads_top_item
* ads_top_category
* ads_conversion

---

## Dashboard功能

* KPI指标展示
* 用户画像分析
* 商品排行分析
* 品类排行分析
* 转化率分析

---

## 后续优化

* Spark改造
* SparkSQL
* Hive数仓
* ECharts可视化
* 用户漏斗分析
* 留存分析
