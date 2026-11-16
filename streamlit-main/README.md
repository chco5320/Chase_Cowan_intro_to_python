## Streamlit 101

A simple sales dashboard demo showcasing core Streamlit UI patterns.

### What's inside

- **[`app.py`](app.py)** — sales dashboard with sidebar controls, KPI metrics, line/bar charts, a data table, and a text input widget
- **[`requirements.txt`](requirements.txt)** — pinned dependencies

### Features demonstrated

| Pattern | API used |
|---|---|
| Page config | `st.set_page_config()` |
| Sidebar widgets | `st.sidebar.slider`, `.checkbox`, `.selectbox` |
| KPI metrics | `st.metric()` |
| Charts | `st.line_chart()`, `st.bar_chart()` |
| Data table | `st.dataframe()` with pandas styler |
| Text input | `st.text_input()` |
| Layout | `st.columns()`, `st.divider()` |

### Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

Opens at `http://localhost:8501`.
