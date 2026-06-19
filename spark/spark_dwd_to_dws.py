from pyspark.sql import SparkSession
from pyspark.sql.functions import *

import os

# ===============================
# SparkSession
# ===============================

spark = SparkSession.builder \
    .appName("DWD_to_DWS") \
    .master("local[*]") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# ===============================
# 路径
# ===============================

project_root = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

input_path = os.path.join(
    project_root,
    "dwd",
    "dwd_user_behavior.csv"
)

output_path = os.path.join(
    project_root,
    "dws",
    "dws_user_profile"
)

# ===============================
# 读取DWD
# ===============================

df = spark.read.option(
    "header", True
).csv(
    input_path,
    inferSchema=True
)

print("DWD记录数：", df.count())

# ===============================
# 用户画像
# ===============================

result = (
    df.groupBy("user_id")
    .agg(
        count("*").alias("total_behavior"),

        sum(
            when(col("behavior_type") == "pv", 1)
            .otherwise(0)
        ).alias("pv_count"),

        sum(
            when(col("behavior_type") == "cart", 1)
            .otherwise(0)
        ).alias("cart_count"),

        sum(
            when(col("behavior_type") == "fav", 1)
            .otherwise(0)
        ).alias("fav_count"),

        sum(
            when(col("behavior_type") == "buy", 1)
            .otherwise(0)
        ).alias("buy_count")
    )
)

# ===============================
# 用户分层
# ===============================

result = result.withColumn(
    "user_level",
    when(col("buy_count") >= 10, "高价值用户")
    .when(col("buy_count") >= 3, "活跃用户")
    .otherwise("普通用户")
)

result.show(10, False)

# ===============================
# 保存
# ===============================

(
    result.coalesce(1)
    .write
    .mode("overwrite")
    .option("header", True)
    .csv(output_path)
)

print("DWS生成完成")

spark.stop()