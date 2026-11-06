import io
import os

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st


st.set_page_config(page_title="Netflix Insights Dashboard", page_icon="🎬", layout="wide")
sns.set_theme(style="whitegrid")

st.markdown(
    """
    <style>
    .main { background-color: #f5f5f5; }
    .stMetric {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    </style>
    """,
    unsafe_allow_html=True,
)


@st.cache_data
def load_data():
    path = "netflix_data.csv" if os.path.exists("netflix_data.csv") else "/content/netflix_data.csv"
    data = pd.read_csv(path)
    data["decade"] = (data["release_year"] // 10) * 10
    data["date_added_parsed"] = pd.to_datetime(data["date_added"], errors="coerce")
    data["added_year"] = data["date_added_parsed"].dt.year
    return data


df_full = load_data()
min_year, max_year = int(df_full["release_year"].min()), int(df_full["release_year"].max())
min_duration, max_duration = int(df_full["duration"].min()), int(df_full["duration"].max())

st.sidebar.header("Dashboard Filters")
selected_types = st.sidebar.multiselect(
    "Content type",
    sorted(df_full["type"].dropna().unique()),
    default=sorted(df_full["type"].dropna().unique()),
)
selected_genres = st.sidebar.multiselect(
    "Genre",
    sorted(df_full["genre"].dropna().unique()),
    default=sorted(df_full["genre"].dropna().unique()),
)
selected_years = st.sidebar.slider(
    "Release year",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year),
)
selected_duration = st.sidebar.slider(
    "Duration (minutes)",
    min_value=min_duration,
    max_value=max_duration,
    value=(min_duration, max_duration),
)

df = df_full[
    df_full["type"].isin(selected_types)
    & df_full["genre"].isin(selected_genres)
    & df_full["release_year"].between(*selected_years)
    & df_full["duration"].between(*selected_duration)
].copy()
movies = df[df["type"] == "Movie"].copy()

st.title("🎬 Netflix Content Analysis")
st.caption("An interactive, decision-ready analysis of Netflix catalog composition, trends, and data quality.")

if df.empty:
    st.warning("No titles match the selected filters. Expand the filters to continue.")
    st.stop()

total_titles = len(df)
movie_share = (df["type"].eq("Movie").mean()) * 100
avg_duration = movies["duration"].mean() if not movies.empty else 0
top_genre = df["genre"].mode().iat[0] if not df["genre"].mode().empty else "N/A"
missing_cells = int(df_full.isna().sum().sum())
total_cells = df_full.shape[0] * df_full.shape[1]

col_m1, col_m2, col_m3, col_m4 = st.columns(4)
col_m1.metric("Filtered Titles", f"{total_titles:,}")
col_m2.metric("Movie Share", f"{movie_share:.1f}%")
col_m3.metric("Avg Movie Duration", f"{avg_duration:.1f} min" if not movies.empty else "N/A")
col_m4.metric("Top Genre", top_genre)

st.download_button(
    "⬇️ Download filtered data",
    data=df.to_csv(index=False).encode("utf-8"),
    file_name="netflix_filtered_data.csv",
    mime="text/csv",
)

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["📈 Executive Overview", "📅 1990s Deep Dive", "🎭 Genres & Talent", "📊 Statistics", "✅ Data Quality"]
)

with tab1:
    st.header("Executive Overview")
    st.write("Use the filters to compare catalog composition, production volume, and movie-length trends.")
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Titles Released by Year")
        yearly = df.groupby(["release_year", "type"]).size().reset_index(name="titles")
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.lineplot(data=yearly, x="release_year", y="titles", hue="type", marker="o", ax=ax)
        ax.set_xlabel("Release year")
        ax.set_ylabel("Titles")
        st.pyplot(fig, clear_figure=True)
    with c2:
        st.subheader("Average Movie Duration by Decade")
        decade_avg = movies.groupby("decade", as_index=False)["duration"].mean()
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.lineplot(data=decade_avg, x="decade", y="duration", marker="o", color="#E50914", ax=ax)
        ax.set_xlabel("Decade")
        ax.set_ylabel("Minutes")
        st.pyplot(fig, clear_figure=True)

    st.subheader("Movie Duration Distribution")
    if movies.empty:
        st.info("The current filters contain no movies.")
    else:
        fig, ax = plt.subplots(figsize=(12, 4))
        sns.histplot(movies["duration"], bins=40, kde=True, color="#E50914", ax=ax)
        ax.set_xlabel("Duration (minutes)")
        st.pyplot(fig, clear_figure=True)

with tab2:
    st.header("The Golden Era: The 1990s")
    movies_90s = movies[movies["release_year"].between(1990, 1999)]
    c3, c4 = st.columns([2, 1])
    with c3:
        st.subheader("1990s Duration Distribution")
        if movies_90s.empty:
            st.info("No 1990s movies match the current filters.")
        else:
            fig, ax = plt.subplots(figsize=(8, 5))
            sns.histplot(movies_90s["duration"], bins=20, color="skyblue", kde=True, ax=ax)
            ax.set_xlabel("Duration (minutes)")
            st.pyplot(fig, clear_figure=True)
    with c4:
        st.subheader("Top 10 Genres")
        st.dataframe(
            movies_90s["genre"].value_counts().head(10).rename("titles"),
            use_container_width=True,
        )

    short_action = movies_90s[
        movies_90s["genre"].str.contains("Action", case=False, na=False)
        & (movies_90s["duration"] < 90)
    ]
    st.metric("1990s Action movies under 90 minutes", len(short_action))

with tab3:
    st.header("Genres and Prolific Directors")
    c5, c6 = st.columns(2)
    with c5:
        st.subheader("Genre Market Share")
        genre_counts = df["genre"].value_counts().head(8)
        fig, ax = plt.subplots(figsize=(7, 5))
        ax.pie(
            genre_counts,
            labels=genre_counts.index,
            autopct="%1.1f%%",
            startangle=140,
            colors=sns.color_palette("pastel"),
        )
        st.pyplot(fig, clear_figure=True)
    with c6:
        st.subheader("Top 10 Most Prolific Directors")
        top_directors = df[df["director"].notna()]["director"].value_counts().head(10)
        fig, ax = plt.subplots(figsize=(7, 5))
        sns.barplot(x=top_directors.values, y=top_directors.index, color="#E50914", ax=ax)
        ax.set_xlabel("Titles")
        ax.set_ylabel("")
        st.pyplot(fig, clear_figure=True)

with tab4:
    st.header("Statistics and Relationships")
    numeric = df.select_dtypes(include="number")
    if numeric.shape[1] > 1:
        with st.expander("View correlation heatmap", expanded=True):
            fig, ax = plt.subplots(figsize=(8, 5))
            sns.heatmap(numeric.corr(), annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
            st.pyplot(fig, clear_figure=True)

    col_s1, col_s2 = st.columns(2)
    with col_s1:
        st.write("**Numeric statistics**")
        st.dataframe(numeric.describe().T, use_container_width=True)
    with col_s2:
        st.write("**Categorical statistics**")
        st.dataframe(df.describe(include=["object"]).T, use_container_width=True)

with tab5:
    st.header("Data Quality Checks")
    st.write("These checks make assumptions and missing values visible before analysis.")
    completeness = (
        df_full.isna()
        .mean()
        .mul(100)
        .round(2)
        .sort_values(ascending=False)
        .rename("missing_percent")
        .to_frame()
    )
    q1, q2, q3 = st.columns(3)
    q1.metric("Missing cells", f"{missing_cells:,}")
    q2.metric("Missingness", f"{missing_cells / total_cells * 100:.2f}%")
    q3.metric("Duplicate rows", f"{df_full.duplicated().sum():,}")
    st.subheader("Column completeness")
    st.dataframe(completeness, use_container_width=True)
    st.caption("Missingness is reported from the full source dataset; charts and KPIs reflect the active filters.")

if st.sidebar.checkbox("Show filtered data table"):
    st.subheader("Filtered Data")
    st.dataframe(df.drop(columns=["date_added_parsed"]), use_container_width=True)
