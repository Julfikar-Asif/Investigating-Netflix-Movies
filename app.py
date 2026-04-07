
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

st.set_page_config(page_title="Netflix Analysis", layout="wide")
st.title("Netflix Movie Trends Analysis")

# Load data
@st.cache_data
def load_data():
    path = 'netflix_data.csv'
    if not os.path.exists(path):
        path = '/content/netflix_data.csv'

    df = pd.read_csv(path)
    df['decade'] = (df['release_year'] // 10) * 10
    return df

df_full = load_data()

# Sidebar Filters
st.sidebar.header("Filters")

# Title Search
title_search = st.sidebar.text_input("Search Movie Title", "")

# Genre Filter
all_genres = sorted(df_full['genre'].unique())
selected_genres = st.sidebar.multiselect("Select Genres", all_genres, default=all_genres)

# Filter dataframe based on selections
df = df_full[df_full['genre'].isin(selected_genres)]
if title_search:
    df = df[df['title'].str.contains(title_search, case=False, na=False)]

# Sidebar / Header Stats
st.header("Key Statistics")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Movies Shown", len(df))
with col2:
    st.metric("Avg Duration", f"{int(df['duration'].mean())} min" if not df.empty else "N/A")
with col3:
    # Download Button Logic
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download Filtered Data",
        data=csv,
        file_name='netflix_filtered_data.csv',
        mime='text/csv',
    )

st.subheader("Average Movie Duration per Decade")
if not df.empty and (df['type'] == 'Movie').any():
    decade_avg = df[df['type'] == 'Movie'].groupby('decade')['duration'].mean().reset_index()
    fig, ax = plt.subplots()
    sns.lineplot(data=decade_avg, x='decade', y='duration', marker='o', ax=ax)
    st.pyplot(fig)
else:
    st.write("No data available for the current filters.")

st.subheader("Top Genres in Selection")
if not df.empty:
    top_genres = df['genre'].value_counts().head(10)
    st.bar_chart(top_genres)

# Show filtered data table
if st.checkbox("Show raw data"):
    st.dataframe(df)
