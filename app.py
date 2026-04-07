
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

st.set_page_config(page_title="Netflix Insights Dashboard", layout="wide")

# --- Custom CSS for Styling ---
st.markdown("""
    <style>
    .main { background-color: #f5f5f5; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_html=True)

# --- Data Loading ---
@st.cache_data
def load_data():
    path = 'netflix_data.csv' if os.path.exists('netflix_data.csv') else '/content/netflix_data.csv'
    df = pd.read_csv(path)
    df['decade'] = (df['release_year'] // 10) * 10
    return df

df_full = load_data()
all_movies = df_full[df_full['type'] == 'Movie']

# --- Sidebar ---
st.sidebar.header("Dashboard Filters")
selected_genres = st.sidebar.multiselect("Filter by Genre", sorted(df_full['genre'].unique()), default=list(df_full['genre'].unique()))
df = df_full[df_full['genre'].isin(selected_genres)]

# --- Header & KPIs ---
st.title("🎬 Netflix Content Analysis")
col_m1, col_m2, col_m3 = st.columns(3)
with col_m1:
    st.metric("Total Titles", len(df))
with col_m2:
    avg_dur = df[df['type']=='Movie']['duration'].mean()
    st.metric("Avg Movie Duration", f"{avg_dur:.1f} min")
with col_m3:
    top_genre = df['genre'].mode()[0]
    st.metric("Top Genre", top_genre)

st.divider()

# --- Main Tabs ---
tab1, tab2, tab3, tab4 = st.tabs(["📈 Historical Trends", "📅 1990s Deep Dive", "🎭 Genres & Talent", "📊 Stats Summary"])

with tab1:
    st.header("Evolution of Netflix Content")
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Average Duration per Decade")
        decade_avg = all_movies.groupby('decade')['duration'].mean().reset_index()
        fig1, ax1 = plt.subplots(figsize=(8, 5))
        sns.lineplot(data=decade_avg, x='decade', y='duration', marker='o', color='#E50914', ax=ax1)
        ax1.set_ylabel("Minutes")
        st.pyplot(fig1)
    with c2:
        st.subheader("Content Volume per Decade")
        movie_counts = all_movies['decade'].value_counts().sort_index().reset_index()
        fig2, ax2 = plt.subplots(figsize=(8, 5))
        sns.barplot(data=movie_counts, x='decade', y='count', palette='Reds_r', ax=ax2)
        st.pyplot(fig2)
    
    st.subheader("Distribution of All Movie Durations")
    fig3, ax3 = plt.subplots(figsize=(12, 4))
    sns.histplot(all_movies['duration'], bins=40, kde=True, color='#E50914', ax=ax3)
    st.pyplot(fig3)

with tab2:
    st.header("The Golden Era: The 1990s")
    movies_90s = all_movies[(all_movies['release_year'] >= 1990) & (all_movies['release_year'] < 2000)]
    
    c3, c4 = st.columns([2, 1])
    with c3:
        st.subheader("1990s Duration Distribution")
        fig4, ax4 = plt.subplots()
        sns.histplot(movies_90s['duration'], bins=20, color='skyblue', kde=True, ax=ax4)
        st.pyplot(fig4)
    with c4:
        st.subheader("Top 10 Genres (90s)")
        genre_90s = movies_90s['genre'].value_counts().head(10)
        st.dataframe(genre_90s, use_container_width=True)

with tab3:
    st.header("Genres and Prolific Directors")
    c5, c6 = st.columns(2)
    with c5:
        st.subheader("Genre Market Share")
        genre_counts = df['genre'].value_counts().head(8)
        fig6, ax6 = plt.subplots()
        ax6.pie(genre_counts, labels=genre_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
        st.pyplot(fig6)
    with c6:
        st.subheader("Top 10 Most Prolific Directors")
        top_10_dir = df[df['director'].notna()]['director'].value_counts().head(10)
        fig7, ax7 = plt.subplots()
        sns.barplot(x=top_10_dir.values, y=top_10_dir.index, palette='viridis', ax=ax7)
        st.pyplot(fig7)

with tab4:
    st.header("Advanced Analytics")
    
    with st.expander("View Correlation Heatmap", expanded=True):
        corr_matrix = df_full.select_dtypes(include=['number']).corr()
        fig_heat, ax_heat = plt.subplots(figsize=(8, 5))
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', ax=ax_heat)
        st.pyplot(fig_heat)

    col_s1, col_s2 = st.columns(2)
    with col_s1:
        st.write("**Numeric Statistics**")
        st.dataframe(df_full.describe(), use_container_width=True)
    with col_s2:
        st.write("**Categorical Statistics**")
        st.dataframe(df_full.describe(include=['O']), use_container_width=True)

if st.sidebar.checkbox("Show Raw Data Table"):
    st.subheader("Raw Dataset View")
    st.dataframe(df)
