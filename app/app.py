
import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# --------------------------------------------------
# Page configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Traffic & Accident Risk Analytics",
    page_icon="🚦",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parent.parent
FEATURE_FILE = BASE_DIR / "data" / "processed" / "feature_engineered.csv"
CRASH_FILE = BASE_DIR / "data" / "processed" / "crash_cleaned.csv"

st.title("🚦 Traffic & Accident Risk Analytics")
st.markdown(
    "Explore Texas traffic crashes by location, year, month, "
    "time of day, and recorded severity."
)

# --------------------------------------------------
# Load existing project data
# --------------------------------------------------
@st.cache_data
def load_data():
    if not FEATURE_FILE.exists():
        raise FileNotFoundError(
            f"Could not find {FEATURE_FILE}. "
            "Check that your processed CSV files are in data/processed/."
        )

    df = pd.read_csv(FEATURE_FILE, low_memory=False)

   if CRASH_FILE.exists():
       try:
           with CRASH_FILE.open("rb") as f:
               file_start = f.read(200)

           # Skip Git LFS pointer files instead of reading them as CSV
           if b"git-lfs.github.com/spec/v1" not in file_start:
               crash = pd.read_csv(
                   CRASH_FILE,
                   usecols=lambda c: c in [
                       "Crash_ID", "Crash_Date", "Crash_Time",
                       "Crash_Fatal_Fl", "Death_Cnt", "Tot_Injry_Cnt",
                       "Rpt_CRIS_Cnty_ID", "Rpt_City_ID",
                       "Wthr_Cond_ID", "Light_Cond_ID",
                       "Crash_Speed_Limit", "At_Intrsct_Fl",
                       "Rpt_Street_Name", "Rpt_Street_Desc"
                   ],
                   low_memory=False
               )
               if "Crash_ID" in crash.columns:
                   crash = crash.drop_duplicates(subset=["Crash_ID"])
                   df = df.merge(
                       crash,
                       on="Crash_ID",
                       how="left",
                       suffixes=("", "_detail")
                   )
     except Exception:
         pass

    # Normalize the key fields
    for col in ["Latitude", "Longitude"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    if "Crash_Year" in df.columns:
        df["Crash_Year"] = pd.to_numeric(
            df["Crash_Year"], errors="coerce"
        )

    if "Crash_Month" in df.columns:
        df["Crash_Month"] = pd.to_numeric(
            df["Crash_Month"], errors="coerce"
        )

    if "Crash_Hour" in df.columns:
        df["Crash_Hour"] = pd.to_numeric(
            df["Crash_Hour"], errors="coerce"
        )

    for col in ["Severity_Target", "Time_Period"]:
        if col in df.columns:
            df[col] = df[col].fillna("Unknown").astype(str)

    return df


try:
    df = load_data()
except Exception as e:
    st.error(f"Could not load the project data: {e}")
    st.stop()

if df.empty:
    st.warning("The processed dataset contains no records.")
    st.stop()

# --------------------------------------------------
# Sidebar filters
# --------------------------------------------------
st.sidebar.header("Filter accidents")

years = sorted(df["Crash_Year"].dropna().astype(int).unique().tolist())
selected_years = st.sidebar.multiselect(
    "Crash year",
    years,
    default=years
)

months = sorted(df["Crash_Month"].dropna().astype(int).unique().tolist())
selected_months = st.sidebar.multiselect(
    "Month",
    months,
    default=months,
    format_func=lambda m: pd.Timestamp(2000, m, 1).strftime("%B")
)

periods = sorted(df["Time_Period"].dropna().unique().tolist())
selected_periods = st.sidebar.multiselect(
    "Time of day",
    periods,
    default=periods
)

severities = sorted(df["Severity_Target"].dropna().unique().tolist())
selected_severities = st.sidebar.multiselect(
    "Recorded severity",
    severities,
    default=severities
)

filtered = df.copy()

if selected_years:
    filtered = filtered[
        filtered["Crash_Year"].isin(selected_years)
    ]
else:
    filtered = filtered.iloc[0:0]

if selected_months:
    filtered = filtered[
        filtered["Crash_Month"].isin(selected_months)
    ]
else:
    filtered = filtered.iloc[0:0]

if selected_periods:
    filtered = filtered[
        filtered["Time_Period"].isin(selected_periods)
    ]
else:
    filtered = filtered.iloc[0:0]

if selected_severities:
    filtered = filtered[
        filtered["Severity_Target"].isin(selected_severities)
    ]
else:
    filtered = filtered.iloc[0:0]

# --------------------------------------------------
# Summary metrics
# --------------------------------------------------
total_crashes = len(filtered)
fatal_count = 0
injury_count = 0

if "Crash_Fatal_Fl" in filtered.columns:
    fatal_count = int(
        filtered["Crash_Fatal_Fl"].astype(str).str.upper().eq("Y").sum()
    )

if "Tot_Injry_Cnt" in filtered.columns:
    injury_count = int(
        pd.to_numeric(
            filtered["Tot_Injry_Cnt"], errors="coerce"
        ).fillna(0).gt(0).sum()
    )

valid_coordinates = (
    filtered["Latitude"].between(-90, 90)
    & filtered["Longitude"].between(-180, 180)
    & filtered["Latitude"].notna()
    & filtered["Longitude"].notna()
) if {"Latitude", "Longitude"}.issubset(filtered.columns) else pd.Series(
    False, index=filtered.index
)

map_data = filtered.loc[valid_coordinates].copy()

c1, c2, c3, c4 = st.columns(4)
c1.metric("Crashes in selection", f"{total_crashes:,}")
c2.metric("Fatal-flagged crashes", f"{fatal_count:,}")
c3.metric("Crashes with injuries", f"{injury_count:,}")
c4.metric("Crashes with coordinates", f"{len(map_data):,}")

st.caption(
    "Metrics reflect the selected records. Fatal counts use Crash_Fatal_Fl; "
    "injury counts use Tot_Injry_Cnt when those fields are available."
)

st.divider()

# --------------------------------------------------
# Interactive accident map
# --------------------------------------------------
st.subheader("📍 Where did crashes happen?")

if not map_data.empty:
    max_points = 15000
    plot_data = map_data

    if len(plot_data) > max_points:
        st.info(
            f"Showing a sample of {max_points:,} mapped crashes for performance. "
            "The metrics and other charts use all filtered records."
        )
        plot_data = plot_data.sample(max_points, random_state=42)

    hover_cols = [
        c for c in [
            "Crash_ID", "Crash_Year", "Crash_Month", "Crash_Hour",
            "Time_Period", "Severity_Target", "Rpt_Street_Name",
            "Rpt_Street_Desc", "Wthr_Cond_ID", "Light_Cond_ID"
        ] if c in plot_data.columns
    ]
    fig_map = px.scatter_map(
        plot_data,
        lat="Latitude",
        lon="Longitude",
        color="Severity_Target",
        hover_data=hover_cols,
        zoom=8,
        height=600,
        opacity=0.65,
        map_style="open-street-map",
        title="Crash locations — select a point to inspect its details"
    )
    fig_map.update_layout(
        margin={"r": 0, "t": 45, "l": 0, "b": 0},
        legend_title_text="Recorded severity"
    )
    st.plotly_chart(fig_map, use_container_width=True)

else:
    st.warning(
        "No valid coordinates are available for the current filters. "
        "Try selecting more years or checking the Latitude and Longitude fields."
    )

st.divider()

# --------------------------------------------------
# Interactive charts
# --------------------------------------------------
left, right = st.columns(2)

with left:
    st.subheader("📅 Crashes by month")
    if "Crash_Month" in filtered.columns and not filtered.empty:
        monthly = (
            filtered.groupby("Crash_Month")
            .size()
            .reindex(range(1, 13), fill_value=0)
            .rename("Crashes")
            .reset_index()
        )
        monthly["Month"] = monthly["Crash_Month"].apply(
            lambda m: pd.Timestamp(2000, int(m), 1).strftime("%b")
        )
        fig_month = px.bar(
            monthly, x="Month", y="Crashes",
            title="Monthly crash count"
        )
        st.plotly_chart(fig_month, use_container_width=True)

with right:
    st.subheader("🕒 Crashes by time of day")
    if "Crash_Hour" in filtered.columns and not filtered.empty:
        hourly = (
            filtered.groupby("Crash_Hour")
            .size()
            .reindex(range(24), fill_value=0)
            .rename("Crashes")
            .reset_index()
        )
        fig_hour = px.line(
            hourly, x="Crash_Hour", y="Crashes",
            markers=True,
            title="Crash count by hour (0–23)"
        )
        fig_hour.update_xaxes(dtick=1, title="Hour of day")
        st.plotly_chart(fig_hour, use_container_width=True)

left2, right2 = st.columns(2)

with left2:
    st.subheader("⚠️ Recorded severity")
    if "Severity_Target" in filtered.columns and not filtered.empty:
        severity_counts = (
            filtered["Severity_Target"]
            .value_counts()
            .rename_axis("Severity")
            .reset_index(name="Crashes")
        )
        fig_severity = px.bar(
            severity_counts,
            x="Severity",
            y="Crashes",
            title="Crashes by recorded severity"
        )
        st.plotly_chart(fig_severity, use_container_width=True)

with right2:
    st.subheader("🌤️ Weather conditions")
    if "Wthr_Cond_ID" in filtered.columns:
        weather = filtered["Wthr_Cond_ID"].dropna()
        if not weather.empty:
            weather_counts = (
                weather.astype(str)
                .value_counts()
                .head(15)
                .rename_axis("Weather condition ID")
                .reset_index(name="Crashes")
            )
            fig_weather = px.bar(
                weather_counts,
                x="Weather condition ID",
                y="Crashes",
                title="Crashes by weather condition ID"
            )
            st.plotly_chart(fig_weather, use_container_width=True)
        else:
            st.info("Weather condition values are unavailable in this selection.")
    else:
        st.info("Weather data is not available in the loaded columns.")

st.divider()

# --------------------------------------------------
# Crash record explorer
# --------------------------------------------------
st.subheader("🔎 Explore individual crash records")
st.write(
    "Use the filters above, then search the displayed records. "
    "These are recorded crash details, not live traffic information."
)

search_text = st.text_input(
    "Search by crash ID, street, or severity",
    placeholder="Enter a crash ID or street name..."
)

details = filtered.copy()

if search_text.strip():
    searchable = [
        c for c in [
            "Crash_ID", "Rpt_Street_Name", "Rpt_Street_Desc",
            "Severity_Target"
        ] if c in details.columns
    ]
    if searchable:
        match = pd.Series(False, index=details.index)
        for col in searchable:
            match |= details[col].astype(str).str.contains(
                search_text, case=False, na=False
            )
        details = details[match]

display_cols = [
    c for c in [
        "Crash_ID", "Crash_Year", "Crash_Month", "Crash_Hour",
        "Time_Period", "Severity_Target", "Crash_Fatal_Fl",
        "Death_Cnt", "Tot_Injry_Cnt", "Rpt_Street_Name",
        "Rpt_Street_Desc", "Wthr_Cond_ID", "Light_Cond_ID",
        "Latitude", "Longitude"
    ] if c in details.columns
]

st.dataframe(
    details[display_cols].head(1000),
    use_container_width=True,
    hide_index=True
)

csv_data = details.to_csv(index=False).encode("utf-8")
st.download_button(
    "Download filtered crash records as CSV",
    data=csv_data,
    file_name="filtered_crash_records.csv",
    mime="text/csv"
)

st.caption(
    "Data source: the project's processed Texas crash records. "
    "Weather and light values are displayed as source IDs, not descriptive labels."
)
