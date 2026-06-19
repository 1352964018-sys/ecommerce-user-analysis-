import pandas as pd
import sqlite3
import os

# =========================
# 数据库路径（绝对安全）
# =========================
# __file__ 是当前脚本路径
project_root = os.path.dirname(os.path.dirname(__file__))  # 项目根目录
db_dir = os.path.join(project_root, "db")
os.makedirs(db_dir, exist_ok=True)  # 确保目录存在
db_path = os.path.join(db_dir, "ecommerce.db")

# 连接数据库
conn = sqlite3.connect(db_path)
print("数据库创建成功：", db_path)




# # =========================
# # DWD
# # =========================
# print("开始读取DWD...")
# dwd_path = os.path.join(project_root, "dwd", "dwd_user_behavior.csv")
# dwd = pd.read_csv(dwd_path)
# print("DWD读取完成")
# dwd.to_sql("dwd_user_behavior", conn, if_exists="replace", index=False)
# print("DWD导入成功")

# =========================
# DWS
# =========================
dws_path = os.path.join(project_root, "dws", "dws_user_profile.csv")
dws = pd.read_csv(dws_path)
dws.to_sql("dws_user_profile", conn, if_exists="replace", index=False)
print("DWS导入成功")

# =========================
# ADS商品排行
# =========================
ads_item_path = os.path.join(project_root, "ads", "ads_top_item.csv")
ads_top_item = pd.read_csv(ads_item_path)
ads_top_item.to_sql("ads_top_item", conn, if_exists="replace", index=False)
print("ADS商品排行导入成功")

# =========================
# ADS品类排行
# =========================
ads_category_path = os.path.join(project_root, "ads", "ads_top_category.csv")
ads_top_category = pd.read_csv(ads_category_path)
ads_top_category.to_sql("ads_top_category", conn, if_exists="replace", index=False)
print("ADS品类排行导入成功")

# =========================
# ADS转化率
# =========================
ads_conversion_path = os.path.join(project_root, "ads", "ads_conversion.csv")
ads_conversion = pd.read_csv(ads_conversion_path)
ads_conversion.to_sql("ads_conversion", conn, if_exists="replace", index=False)
print("ADS转化率导入成功")

# =========================
# 完成
# =========================
conn.close()
print("全部导入完成 ✅")