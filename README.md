# Ecommerce User Analysis

基于淘宝用户行为数据构建的数据分析与数据仓库项目。

## 项目简介

本项目基于阿里云天池公开数据集《UserBehavior》，完成从原始数据到数据仓库四层模型（ODS → DWD → DWS → ADS）的搭建，并使用 Python、Pandas、SQLite 实现用户行为分析、用户画像构建和运营指标统计。

项目模拟互联网电商公司的离线数仓开发流程，涵盖数据清洗、指标计算、用户分层、商品分析和数据库建模等核心内容。

---

## 数据集介绍

数据来源：阿里云天池 UserBehavior 数据集

数据规模：

* 用户数：987,994
* 商品数：4,162,024
* 行为记录数：100,150,807

字段说明：

| 字段            | 含义     |
| ------------- | ------ |
| user_id       | 用户ID   |
| item_id       | 商品ID   |
| category_id   | 商品类目ID |
| behavior_type | 用户行为   |
| timestamp     | 行为时间   |

行为类型：

* pv：浏览
* fav：收藏
* cart：加购
* buy：购买

---

## 技术栈

### 数据处理

* Python
* Pandas

### 数据库

* SQLite

### 数据分析

* SQL
* 用户画像分析
* 用户留存分析
* 转化率分析

### 数据仓库

* ODS
* DWD
* DWS
* ADS

### 后续规划

* PySpark
* Hive
* Hadoop
* Airflow

---

## 项目架构

```text
UserBehavior.csv
       │
       ▼
ODS（原始数据层）
       │
       ▼
DWD（明细数据层）
       │
       ▼
DWS（用户画像层）
       │
       ▼
ADS（分析结果层）
```

项目目录：

```text
ecommerce-user-analysis/
│
├── data/
│   └── UserBehavior.csv
│
├── ods/
│   └── ods_user_behavior.csv
│
├── dwd/
│   └── dwd_user_behavior.csv
│
├── dws/
│   └── dws_user_profile.csv
│
├── ads/
│   ├── ads_top_item.csv
│   ├── ads_top_category.csv
│   └── ads_conversion.csv
│
├── db/
│   └── ecommerce.db
│
├── notebook/
│   ├── analysis.py
│   ├── load_sqlite.py
│   └── sql_practice.sql
│
└── README.md
```

---

## 已完成功能

### 数据清洗

* 时间异常值过滤
* 时间字段格式转换
* 日期字段提取

### 用户分析

* 用户总数统计
* DAU（日活）分析
* 次日留存率分析

### 商品分析

* 商品热度排行榜
* 商品购买排行榜
* 品类排行榜

### 转化分析

* 浏览用户统计
* 购买用户统计
* 购买转化率计算

### 用户画像

构建 DWS 用户画像宽表：

* pv_count
* fav_count
* cart_count
* buy_count
* is_buyer

用户分层：

* 潜在用户
* 普通购买用户
* 高价值用户

### SQLite 数仓

导入以下分析表：

* dwd_user_behavior
* dws_user_profile
* ads_top_item
* ads_top_category
* ads_conversion

---

## 核心指标

### 用户规模

* 总用户数：987,994

### 转化率

* 浏览用户数：984,108
* 购买用户数：672,404
* 转化率：68.33%

### DAU峰值

* 日期：2017-12-02
* 活跃用户数：941,709

### 用户分层

| 用户类型   | 数量      |
| ------ | ------- |
| 潜在用户   | 314,796 |
| 普通购买用户 | 548,045 |
| 高价值用户  | 121,267 |

---

## SQL示例

查询购买次数最多的用户：

```sql
SELECT
    user_id,
    buy_count
FROM dws_user_profile
ORDER BY buy_count DESC
LIMIT 10;
```

查询最热门商品：

```sql
SELECT *
FROM ads_top_item
LIMIT 10;
```

---

## 项目成果

* 完成千万级电商行为数据分析
* 完成ODS-DWD-DWS-ADS四层数仓建模
* 完成SQLite离线数仓搭建
* 完成用户画像与用户分层
* 具备迁移至Spark/Hive的基础架构

---

## 后续优化

* [ ] 使用 PySpark 重构 ETL
* [ ] Hive 数仓改造
* [ ] Airflow 调度
* [ ] ECharts 数据可视化
* [ ] Streamlit 数据分析看板
* [ ] Docker 项目部署

