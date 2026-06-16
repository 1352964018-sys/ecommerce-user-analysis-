import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("../charts", exist_ok=True)

dws = pd.read_csv("../dws/dws_user_profile.csv")

level_count = dws["user_level"].value_counts()
plt.rcParams["font.sans-serif"] = ["SimHei"] # 设置Matplotlib字体为SimHei，以正确显示中文
plt.rcParams["axes.unicode_minus"] = False # 关闭坐标轴unicode负号渲染，解决负数'-'变成方框乱码
#用户分层饼图
plt.figure(figsize=(8,6))
plt.pie(
    level_count,
    labels=level_count.index,
    autopct="%1.1f%%"
)
plt.title("User Segmentation")
plt.savefig(
    "../charts/user_level.png"
)
plt.show()

#Top 10 商品排行榜
ads_item = pd.read_csv(
    "../ads/ads_top_item.csv"
)
top10 = ads_item.head(10)
plt.figure(figsize=(10,6))
plt.bar(
    top10["item_id"].astype(str),
    top10["cnt"]
)
plt.xticks(rotation=45)
plt.title("Top10 Item Ranking")
plt.tight_layout()
plt.savefig(
    "../charts/top10_item.png"
)
plt.show()

#Top10品类排行榜
ads_category = pd.read_csv(
    "../ads/ads_top_category.csv"
)
top10 = ads_category.head(10)
plt.figure(figsize=(10,6))
plt.bar(
    top10["category_id"].astype(str),
    top10["cnt"]
)
plt.xticks(rotation=45)
plt.title("Top10 Category Ranking")
plt.tight_layout()
plt.savefig(
    "../charts/top10_category.png"
)
plt.show()

#转化率图
ads_conversion = pd.read_csv(
    "../ads/ads_conversion.csv"
)
rate = ads_conversion[
    "conversion_rate"
].iloc[0]
plt.figure(figsize=(6,4))
plt.bar(
    ["Conversion Rate"],
    [rate]
)
plt.title(
    f"Conversion Rate {rate:.2%}"
)
plt.savefig(
    "../charts/conversion_rate.png"
)
plt.show()