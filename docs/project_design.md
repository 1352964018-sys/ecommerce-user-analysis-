# 电商用户行为分析项目

## 一、项目背景

本项目基于阿里天池 UserBehavior 用户行为数据集，对电商平台用户行为进行分析，构建完整的数据仓库体系，实现用户画像、用户分层、用户留存分析、转化率分析以及商品热度分析。

项目采用 Python + Pandas + SQLite 技术栈，模拟互联网公司常见的数据仓库开发流程。

---

## 二、项目目标

通过对用户行为数据进行清洗、加工和建模，实现：

* 用户行为分析
* 用户活跃度分析
* 用户留存分析
* 用户购买转化分析
* 用户画像构建
* 用户价值分层
* 商品热度分析
* 品类热度分析

最终形成完整的数据仓库项目。

---

## 三、数据集介绍

数据来源：

阿里天池 UserBehavior 数据集

数据规模：

* 原始数据量：100,150,807 条
* 清洗后数据量：100,135,351 条
* 用户数：987,994
* 商品数：4,162,024

字段说明：

| 字段名           | 含义   |
| ------------- | ---- |
| user_id       | 用户ID |
| item_id       | 商品ID |
| category_id   | 品类ID |
| behavior_type | 行为类型 |
| timestamp     | 行为时间 |

行为类型：

* pv：浏览
* fav：收藏
* cart：加购
* buy：购买

---

## 四、项目技术栈

### 数据处理

* Python
* Pandas
* NumPy

### 数据存储

* SQLite

### 数据分析

* SQL
* Pandas GroupBy

### 数据可视化

* Matplotlib

---

## 五、数据仓库架构设计

采用经典四层数仓模型：

ODS → DWD → DWS → ADS

### ODS层（原始数据层）

作用：

存储原始业务数据。

表：

ods_user_behavior.csv

---

### DWD层（明细数据层）

作用：

完成数据清洗与标准化。

处理内容：

* 时间字段转换
* 异常时间过滤
* 字段标准化
* 日期字段拆分

表：

dwd_user_behavior.csv

---

### DWS层（主题汇总层）

作用：

构建用户画像宽表。

统计指标：

* pv_count
* fav_count
* cart_count
* buy_count
* is_buyer

用户分层规则：

高价值用户：

buy_count ≥ 5

普通购买用户：

1 ≤ buy_count < 5

潜在用户：

buy_count = 0

表：

dws_user_profile.csv

---

### ADS层（应用数据层）

作用：

面向业务指标输出。

生成表：

ads_top_item.csv

商品热度排行榜

ads_top_category.csv

品类热度排行榜

ads_conversion.csv

用户转化率指标

---

## 六、核心指标分析

### DAU（日活用户）

统计每日活跃用户数量。

计算方式：

DAU = COUNT(DISTINCT user_id)

---

### 次日留存率

定义：

某天活跃用户中，第二天仍然活跃的用户比例。

计算公式：

次日留存率 = 次日仍活跃用户数 ÷ 当日活跃用户数

---

### 用户转化率

定义：

浏览用户最终完成购买的比例。

计算公式：

转化率 = 购买用户数 ÷ 浏览用户数

项目结果：

转化率约为 68.33%

---

## 七、项目成果

成功构建：

* ODS原始数据层
* DWD明细数据层
* DWS用户画像层
* ADS业务指标层

完成：

* 用户画像分析
* 用户分层分析
* DAU分析
* 留存率分析
* 转化率分析
* 商品热度分析
* 品类热度分析

最终数据落地至 SQLite 数据库，实现完整的数据仓库项目闭环。

---

## 八、项目目录结构

ecommerce-user-analysis/

├── data/

│ └── UserBehavior.csv

├── ods/

│ └── ods_user_behavior.csv

├── dwd/

│ └── dwd_user_behavior.csv

├── dws/

│ └── dws_user_profile.csv

├── ads/

│ ├── ads_top_item.csv

│ ├── ads_top_category.csv

│ └── ads_conversion.csv

├── db/

│ └── ecommerce.db

├── notebook/

│ ├── analysis.py

│ ├── load_sqlite.py

│ └── sql_practice.sql

└── docs/

└── project_design.md

---

## 九、项目价值

本项目完整模拟互联网企业数据仓库开发流程，覆盖：

* 数据清洗
* 数据建模
* 数据仓库分层
* SQL分析
* 用户画像构建
* 指标体系建设

具备数据分析实习生、数据开发实习生、商业分析实习生岗位的项目展示价值。
