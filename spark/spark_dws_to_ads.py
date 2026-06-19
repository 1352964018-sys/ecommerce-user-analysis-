from pyspark.sql import SparkSession
from pyspark.sql.functions import *

import os

spark = SparkSession.builder \
    .appName("DWS_to_ADS") \
    .master("local[*]") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# ===============================
# 路径
# ===============================

project_root = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

dwd_path = os.path.join(
    project_root,
    "dwd",
    "dwd_user_behavior.csv"
)

dws_path = os.path.join(
    project_root,
    "dws",
    "dws_user_profile.csv"
)

ads_path = os.path.join(
    project_root,
    "ads"
)

# ===============================
# 读取数据
# ===============================

dwd = spark.read.option(
    "header", True
).csv(
    dwd_path,
    inferSchema=True
)

dws = spark.read.option(
    "header", True
).csv(
    dws_path,
    inferSchema=True
)

# ===============================
# TOP10商品
# ===============================

top_item = (
    dwd.groupBy("item_id")
    .count()
    .orderBy(desc("count"))
    .limit(10)
)

(
    top_item.coalesce(1)
    .write
    .mode("overwrite")
    .option("header", True)
    .csv(os.path.join(ads_path, "ads_top_item"))
)

# ===============================
# TOP10品类
# ===============================

top_category = (
    dwd.groupBy("category_id")
    .count()
    .orderBy(desc("count"))
    .limit(10)
)

(
    top_category.coalesce(1)
    .write
    .mode("overwrite")
    .option("header", True)
    .csv(os.path.join(ads_path, "ads_top_category"))
)

# ===============================
# 转化率
# ===============================

total_user = dws.count()

buyer = dws.filter(
    col("buy_count") > 0
).count()

conversion = spark.createDataFrame(
    [
        (
            total_user,
            buyer,
            buyer / total_user
        )
    ],
    [
        "total_user",
        "buyer_user",
        "conversion_rate"
    ]
)

(
    conversion.coalesce(1)
    .write
    .mode("overwrite")
    .option("header", True)
    .csv(os.path.join(ads_path, "ads_conversion"))
)

print("ADS生成完成")

spark.stop()