from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_unixtime
from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    LongType,
)
import os

# ===============================
# 创建 SparkSession
# ===============================
spark = (
    SparkSession.builder
    .appName("Ecommerce User Behavior ETL")
    .master("local[*]")
    .config("spark.driver.memory", "4g")
    .config("spark.executor.memory", "4g")
    .config("spark.sql.shuffle.partitions", "8")
    .getOrCreate()
)

spark.sparkContext.setLogLevel("WARN")

# ===============================
# 项目路径
# ===============================
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ods_path = os.path.join(
    project_root,
    "ods",
    "ods_user_behavior.csv"
)

output_path = os.path.join(
    project_root,
    "dwd",
    "dwd_user_behavior"
)

# ===============================
# Schema
# ===============================
schema = StructType([
    StructField("user_id", StringType(), True),
    StructField("item_id", StringType(), True),
    StructField("category_id", StringType(), True),
    StructField("behavior_type", StringType(), True),
    StructField("timestamp", LongType(), True)
])

# ===============================
# 读取ODS
# ===============================
print("=" * 50)
print("读取 ODS 数据...")
print("=" * 50)

df = (
    spark.read
    .option("header", "false")
    .schema(schema)
    .csv(ods_path)
)

print("ODS记录数：", df.count())

# ===============================
# DWD清洗
# ===============================
dwd = (
    df.dropDuplicates()
      .dropna()
      .withColumn(
          "datetime",
          from_unixtime(col("timestamp"))
      )
)

print("DWD记录数：", dwd.count())

# ===============================
# Spark SQL
# ===============================
dwd.createOrReplaceTempView("dwd_user_behavior")

result = spark.sql("""
SELECT
    user_id,
    item_id,
    category_id,
    behavior_type,
    timestamp,
    datetime
FROM dwd_user_behavior
WHERE behavior_type IN ('pv','cart','fav','buy')
""")

print("=" * 50)
print("Spark SQL 查询完成")
print("=" * 50)

result.show(10, False)

# ===============================
# 保存DWD
# ===============================
(
    result.coalesce(1)
          .write
          .mode("overwrite")
          .option("header", True)
          .csv(output_path)
)

print("=" * 50)
print("DWD生成完成")
print(output_path)
print("=" * 50)

spark.stop()