import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="淘宝用户行为分析",
    layout="wide"
)

# =====================
# 路径
# =====================
project_root = os.path.dirname(
    os.path.dirname(__file__)
)

dws_path = os.path.join(
    project_root,
    "dws",
    "dws_user_profile.csv"
)

ads_item_path = os.path.join(
    project_root,
    "ads",
    "ads_top_item.csv"
)

ads_category_path = os.path.join(
    project_root,
    "ads",
    "ads_top_category.csv"
)

ads_conversion_path = os.path.join(
    project_root,
    "ads",
    "ads_conversion.csv"
)

# =====================
# 读取数据
# =====================
dws = pd.read_csv(dws_path)

ads_item = pd.read_csv(
    ads_item_path
)

ads_category = pd.read_csv(
    ads_category_path
)

ads_conversion = pd.read_csv(
    ads_conversion_path
)

# =====================
# 标题
# =====================
st.title("🛒 淘宝用户行为分析 Dashboard")

st.title("🛒 Ecommerce User Analysis Dashboard")

# =====================
# KPI指标
# =====================

total_users = len(dws)

buyer_users = len(
    dws[dws["buy_count"] > 0]
)

conversion_rate = buyer_users / total_users

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "总用户数",
        f"{total_users:,}"
    )

with col2:
    st.metric(
        "购买用户数",
        f"{buyer_users:,}"
    )

with col3:
    st.metric(
        "转化率",
        f"{conversion_rate:.2%}"
    )


# =====================
# 用户分层
# =====================
st.subheader("用户分层分布")

user_level = dws["user_level"].value_counts()

st.bar_chart(user_level)



# =====================
# TOP10商品
# =====================
st.subheader("Top10 商品排行榜")

top10_item = ads_item.head(10)

st.dataframe(top10_item)

# =====================
# TOP10品类
# =====================
st.subheader("Top10 品类排行榜")

top10_category = ads_category.head(10)

st.dataframe(top10_category)

# =====================
# 明细表
# =====================
st.subheader("用户画像样例")

st.dataframe(
    dws.head(20)
)




st.sidebar.title("筛选条件")

level = st.sidebar.selectbox(
    "用户等级",
    ["全部"] +
    list(dws["user_level"].unique())
)

if level != "全部":
    filtered = dws[
        dws["user_level"] == level
    ]
else:
    filtered = dws

st.write(
    f"当前用户数：{len(filtered)}"
)