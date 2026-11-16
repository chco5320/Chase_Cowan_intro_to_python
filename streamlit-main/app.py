import streamlit as st
import pandas as pd
import numpy as np

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(page_title="Sales Dashboard", page_icon="📊", layout="wide")

# ── Sidebar controls ─────────────────────────────────────────────────────────
st.sidebar.title("⚙️ Settings")
num_months = st.sidebar.slider("Months to display", min_value=3, max_value=24, value=12)
show_raw = st.sidebar.checkbox("Show raw data", value=False)
region = st.sidebar.selectbox("Region", ["All", "North", "South", "East", "West"])

# ── Fake data ─────────────────────────────────────────────────────────────────
rng = np.random.default_rng(42)
months = pd.date_range("2024-01", periods=num_months, freq="MS").strftime("%b %Y")

regions = ["North", "South", "East", "West"]
data = {
    r: rng.integers(50_000, 200_000, size=num_months) for r in regions
}
df = pd.DataFrame(data, index=months)

if region != "All":
    df_display = df[[region]]
else:
    df_display = df

# ── Title ──────────────────────────────────────────────────────────────────────
st.title("📊 Sales Dashboard")
st.caption(f"Showing {num_months} months · Region: {region}")

# ── KPI row ────────────────────────────────────────────────────────────────────
total = df_display.values.sum()
avg_monthly = df_display.values.mean()
best_month_idx = df_display.sum(axis=1).idxmax()

col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", f"${total:,.0f}")
col2.metric("Avg Monthly Revenue", f"${avg_monthly:,.0f}")
col3.metric("Best Month", best_month_idx)

st.divider()

# ── Charts ────────────────────────────────────────────────────────────────────
chart_col, pie_col = st.columns([2, 1])

with chart_col:
    st.subheader("Revenue over time")
    st.line_chart(df_display)

with pie_col:
    st.subheader("Revenue by region")
    region_totals = df.sum().rename("Total")
    st.bar_chart(region_totals)

st.divider()

# ── Raw data table ─────────────────────────────────────────────────────────────
if show_raw:
    st.subheader("Raw data")
    st.dataframe(
        df_display.style.format("${:,.0f}"),
        use_container_width=True,
    )

# ── Interactive input example ─────────────────────────────────────────────────
st.divider()
st.subheader("💬 Ask about the data")
question = st.text_input("Type a question (demo — echoes back):", placeholder="e.g. Which region sold the most?")
if question:
    best_region = df.sum().idxmax()
    st.info(
        f"Best performing region across all time: **{best_region}** "
        f"(${df[best_region].sum():,.0f} total). _(This is a static demo response.)_"
    )
