import streamlit as st
import requests
import pandas as pd
import plotly.express as px

# ----------------------------------
# PAGE CONFIG
# ----------------------------------
st.set_page_config(
    page_title="Store Intelligence Dashboard",
    page_icon="🛍️",
    layout="wide"
)

BASE_URL = "http://127.0.0.1:8000"

# ----------------------------------
# CUSTOM CSS
# ----------------------------------
st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

.block-container {
    padding-top: 1rem;
}

.metric-box {
    background-color: #1f2937;
    padding: 15px;
    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------------
# LOAD DATA
# ----------------------------------
metrics = requests.get(
    f"{BASE_URL}/stores/STORE_001/metrics"
).json()

funnel = requests.get(
    f"{BASE_URL}/stores/STORE_001/funnel"
).json()

heatmap = requests.get(
    f"{BASE_URL}/stores/STORE_001/heatmap"
).json()

anomalies = requests.get(
    f"{BASE_URL}/stores/STORE_001/anomalies"
).json()

# ----------------------------------
# HEADER
# ----------------------------------
st.title("🛍️ Store Intelligence Platform")

st.success(
    "Store Status: Operational | Cameras Active: 5 | Analytics Running"
)

# ----------------------------------
# KPI CARDS
# ----------------------------------
st.markdown("## 📊 Key Metrics")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "👥 Visitors",
        metrics.get("unique_visitors", 0)
    )

with c2:
    st.metric(
        "📌 Events",
        metrics.get("total_events", 0)
    )

with c3:
    st.metric(
        "🧾 Billing",
        metrics.get("billing_events", 0)
    )

with c4:
    st.metric(
        "🏬 Zones",
        len(heatmap)
    )

st.divider()

# ----------------------------------
# CHARTS
# ----------------------------------
left, right = st.columns(2)

# Funnel Chart
with left:

    st.subheader("🧭 Visitor Funnel")

    funnel_df = pd.DataFrame({
        "Stage": [
            "Store Entry",
            "Billing"
        ],
        "Count": [
            funnel.get("store_entries", 0),
            funnel.get("billing_visitors", 0)
        ]
    })

    fig_funnel = px.funnel(
        funnel_df,
        x="Count",
        y="Stage",
        title="Conversion Funnel"
    )

    st.plotly_chart(
        fig_funnel,
        use_container_width=True
    )

# Heatmap Chart
with right:

    st.subheader("🔥 Zone Activity")

    heatmap_df = pd.DataFrame(
        list(heatmap.items()),
        columns=["Zone", "Events"]
    )

    fig_zone = px.bar(
        heatmap_df,
        x="Zone",
        y="Events",
        title="Zone Activity Distribution"
    )

    st.plotly_chart(
        fig_zone,
        use_container_width=True
    )

st.divider()

# ----------------------------------
# TABLE + ANOMALIES
# ----------------------------------
left, right = st.columns([2, 1])

with left:

    st.subheader("📋 Zone Statistics")

    st.dataframe(
        heatmap_df,
        use_container_width=True,
        hide_index=True
    )

with right:

    st.subheader("🚨 Anomalies")

    if anomalies:

        for anomaly in anomalies:

            st.warning(
                f"{anomaly.get('type')} ({anomaly.get('severity')})"
            )

    else:

        st.success(
            "No anomalies detected"
        )

st.divider()

# ----------------------------------
# SYSTEM OVERVIEW
# ----------------------------------
st.subheader("⚙️ Architecture")

st.code(
"""
CCTV Videos
      ↓
YOLOv8 Detection
      ↓
ByteTrack Tracking
      ↓
Event Generator
      ↓
FastAPI Backend
      ↓
Streamlit Dashboard
"""
)

st.caption(
    "Purplle Tech Challenge 2026"
)