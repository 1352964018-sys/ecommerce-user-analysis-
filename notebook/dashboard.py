import streamlit as st
import pandas as pd
import sqlite3
import os
import plotly.graph_objects as go

# =========================

# 页面配置

# =========================

st.set_page_config(
page_title="淘宝用户行为分析",
page_icon="🛒",
layout="wide"
)

# =========================

# 数据库连接

# =========================

project_root = os.path.dirname(
os.path.dirname(__file__)
)

db_path = os.path.join(
project_root,
"db",
"ecommerce.db"
)

conn = sqlite3.connect(db_path)

# =========================

# 读取数据

# =========================

dws = pd.read_sql(
"SELECT * FROM dws_user_profile",
conn
)

ads_item = pd.read_sql(
"SELECT * FROM ads_top_item",
conn
)

ads_category = pd.read_sql(
"SELECT * FROM ads_top_category",
conn
)

ads_conversion = pd.read_sql(
"SELECT * FROM ads_conversion",
conn
)

# =========================

# 侧边栏

# =========================

st.sidebar.title("📊 导航")

page = st.sidebar.radio(
"选择页面",
[
"数据概览",
"用户分析",
"商品分析",
"转化分析"
]
)

# =========================

# 数据概览

# =========================

if page == "数据概览":
    st.title("🛒 淘宝用户行为分析 Dashboard")

    total_users = len(dws)

    buyer_users = int(
    dws["is_buyer"].sum()
)

    rate = float(
    ads_conversion[
        "conversion_rate"
    ].iloc[0]
)

    high_value_users = len(
    dws[
        dws["user_level"]=="高价值用户"
    ]
)

    col1,col2,col3,col4 = st.columns(4)

    col1.metric(
    "总用户数",
    f"{total_users:,}"
)

    col2.metric(
    "购买用户数",
    f"{buyer_users:,}"
)

    col3.metric(
    "转化率",
    f"{rate:.2%}"
)

    col4.metric(
    "高价值用户",
    f"{high_value_users:,}"
)
    st.success("数据仓库已完成 ODS → DWD → DWS → ADS 建设")


# =========================

# 用户分析

# =========================
elif page == "用户分析":


    st.title("👤 用户画像分析")

    level_count = (
    dws["user_level"]
    .value_counts()
)

    st.subheader("用户等级分布")

    st.bar_chart(level_count)

    st.subheader("用户等级统计")

    st.dataframe(
    level_count.reset_index()
)


# =========================

# 商品分析

# =========================

elif page == "商品分析":


    st.title("🔥 商品分析")

    st.subheader("Top10商品")

    top10_item = ads_item.head(10)

    st.bar_chart(
    top10_item.set_index(
        "item_id"
    )["cnt"]
)

    st.dataframe(top10_item)

    st.subheader("Top10品类")

    top10_category = (
    ads_category.head(10)
)

    st.bar_chart(
    top10_category.set_index(
        "category_id"
    )["cnt"]
)

    st.dataframe(top10_category)

# =========================

# 转化分析

# =========================
elif page == "转化分析":


    st.title("📈 转化分析")

    rate = float(
    ads_conversion[
        "conversion_rate"
    ].iloc[0]
)

    st.metric(
    "整体转化率",
    f"{rate:.2%}"
)

    buyer_users = int(
    dws["is_buyer"].sum()
)

    total_users = len(dws)

    fig = go.Figure(
    go.Funnel(
        y=[
            "总用户",
            "购买用户"
        ],
        x=[
            total_users,
            buyer_users
        ]
    )
)

    st.plotly_chart(
    fig,
    use_container_width=True
)
