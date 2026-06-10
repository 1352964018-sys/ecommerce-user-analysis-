import pandas as pd

# 读取数据
df = pd.read_csv("../data/user_behavior.csv")

print("========== 数据预览 ==========")
print(df.head())

print("\n========== 用户数量 ==========")
print(df["user_id"].nunique())

print("\n========== 行为统计 ==========")
print(df["behavior_type"].value_counts())

print("\n========== Top商品排行榜 ==========")
top_items = df["item_id"].value_counts()
print(top_items)

print("\n========== 商品购买排行榜 ==========")
buy_df = df[df["behavior_type"] == "buy"]
print(buy_df["item_id"].value_counts())

pv_users = df[df["behavior_type"] == "pv"]["user_id"].nunique()
buy_users = df[df["behavior_type"] == "buy"]["user_id"].nunique()
conversion_rate = buy_users / pv_users

print("\n========== 购买转化率 ==========")
print(f"转化率: {conversion_rate:.2%}")