import pandas as pd
import os
import shutil

# =======================
# Step0: 目录准备
# =======================
os.makedirs("../ods", exist_ok=True)
os.makedirs("../dwd", exist_ok=True)
os.makedirs("../dws", exist_ok=True)
os.makedirs("../ads", exist_ok=True)

# =======================
# Step1: 读取原始数据
# =======================
columns = ["user_id", "item_id", "category_id", "behavior_type", "timestamp"]

df = pd.read_csv(
    "../data/UserBehavior.csv",
    header=None,
    names=columns,
    # nrows=100  # 可选：测试小数据
)

print("清洗前数据量：", len(df))

# =======================
# Step2: 生成ODS层 原始数据层
# =======================
shutil.copy("../data/UserBehavior.csv", "../ods/ods_user_behavior.csv")
print("ODS层数据已生成")

# =======================
# Step3: 数据清洗 → DWD清洗层
# =======================
df = df[(df["timestamp"] >= 1511481600) & (df["timestamp"] <= 1512691199)]
df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s")
df["date"] = df["timestamp"].dt.date

df.to_csv("../dwd/dwd_user_behavior.csv", index=False)
print("DWD层已生成")

# =======================
# Step4: 指标统计
# =======================
print("\n========== 数据预览 ==========")
print(df.head())

print("\n========== 用户数量 ==========")
print(df["user_id"].nunique())

print("\n========== 行为统计 ==========")
print(df["behavior_type"].value_counts())

print("\n========== Top商品排行榜 ==========")
top_items = df["item_id"].value_counts()
print(top_items.head())

print("\n========== 商品购买排行榜 ==========")
buy_df = df[df["behavior_type"] == "buy"]
print(buy_df["item_id"].value_counts().head())

print("\n========== 购买转化率 ==========")
pv_users = df[df["behavior_type"] == "pv"]["user_id"].nunique()
buy_users = df[df["behavior_type"] == "buy"]["user_id"].nunique()
conversion_rate = buy_users / pv_users
print(f"浏览用户数: {pv_users}")
print(f"购买用户数: {buy_users}")
print(f"转化率: {conversion_rate:.2%}")

print("\n========== DAU（日活用户） ==========")
dau = df.groupby("date")["user_id"].nunique()
print(dau.head())

print("\n========== 最高活跃日 ==========")
max_day = dau.idxmax()
max_users = dau.max()
print(f"日期: {max_day}")
print(f"活跃用户数: {max_users}")

print("\n========== 日期范围 ==========")
print(df["date"].min())
print(df["date"].max())

# =======================
# Step5: 次日留存率
# =======================
print("\n========== 构建每日用户集合 ==========")
daily_users = df.groupby("date")["user_id"].apply(set)
print(daily_users.head())

print("\n========== 次日留存率 ==========")
dates = sorted(daily_users.index)
for i in range(len(dates) - 1):
    current_day = dates[i]
    next_day = dates[i + 1]
    current_users = daily_users[current_day]
    next_users = daily_users[next_day]
    retained_users = current_users & next_users
    retention_rate = len(retained_users) / len(current_users)
    print(f"{current_day} -> {next_day} 留存率: {retention_rate:.2%}")

# =======================
# Step6: DWS 用户画像
# =======================
user_profile = pd.DataFrame()
user_profile["pv_count"] = df[df["behavior_type"]=="pv"].groupby("user_id").size()
user_profile["fav_count"] = df[df["behavior_type"]=="fav"].groupby("user_id").size()
user_profile["cart_count"] = df[df["behavior_type"]=="cart"].groupby("user_id").size()
user_profile["buy_count"] = df[df["behavior_type"]=="buy"].groupby("user_id").size()
user_profile = user_profile.fillna(0)
user_profile["is_buyer"] = (user_profile["buy_count"] > 0).astype(int)

# 用户分层
def user_level(row):
    if row["buy_count"] >= 5:
        return "高价值用户"
    elif row["buy_count"] >= 1:
        return "普通购买用户"
    else:
        return "潜在用户"

user_profile["user_level"] = user_profile.apply(user_level, axis=1)
print("\n========== 用户分层 ==========")
print(user_profile["user_level"].value_counts())

# 保存DWS层
user_profile.to_csv("../dws/dws_user_profile.csv")
print("DWS用户画像层保存成功")

# =======================
# Step7: ADS指标层
# =======================
# 商品排行榜
top_item = df.groupby("item_id").size().reset_index(name="cnt").sort_values("cnt", ascending=False).head(100)
top_item.to_csv("../ads/ads_top_item.csv", index=False)
print("ADS商品排行榜保存成功")

# 品类排行榜
top_category = df.groupby("category_id").size().reset_index(name="cnt").sort_values("cnt", ascending=False).head(100)
top_category.to_csv("../ads/ads_top_category.csv", index=False)
print("ADS品类排行榜保存成功")

# 转化率指标
conversion_df = pd.DataFrame({
    "pv_users": [pv_users],
    "buy_users": [buy_users],
    "conversion_rate": [conversion_rate]
})
conversion_df.to_csv("../ads/ads_conversion.csv", index=False)
print("ADS转化率指标保存成功")

print("\n========== 四层数据仓库生成完毕 ==========")