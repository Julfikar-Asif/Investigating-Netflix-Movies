
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download Filtered Data",
        data=csv,
        file_name='netflix_filtered_data.csv',
        mime='text/csv',
    )

# Visualizations
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("Average Movie Duration per Decade")
    if not df.empty and (df['type'] == 'Movie').any():
        decade_avg = df[df['type'] == 'Movie'].groupby('decade')['duration'].mean().reset_index()
        fig1, ax1 = plt.subplots()
        sns.lineplot(data=decade_avg, x='decade', y='duration', marker='o', ax=ax1)
        st.pyplot(fig1)
    else:
        st.write("No data available.")

with col_right:
    st.subheader("Genre Distribution (Pie Chart)")
    if not df.empty:
        genre_counts = df['genre'].value_counts()
        top_10 = genre_counts.head(10)
        others = genre_counts.iloc[10:].sum()
        if others > 0:
            plot_data = pd.concat([top_10, pd.Series({'Others': others})])
        else:
            plot_data = top_10

        fig_pie, ax_pie = plt.subplots()
        ax_pie.pie(plot_data, labels=plot_data.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
        ax_pie.axis('equal')
        st.pyplot(fig_pie)
    else:
        st.write("No data available.")

st.subheader("Top 10 Most Prolific Directors")
if not df.empty:
    valid_directors = df[df['director'].notna()]
    if not valid_directors.empty:
        top_10_dir = valid_directors['director'].value_counts().head(10).reset_index()
        top_10_dir.columns = ['Director', 'Movie Count']
        fig2, ax2 = plt.subplots(figsize=(10, 6))
        sns.barplot(data=top_10_dir, x='Movie Count', y='Director', hue='Director', palette='rocket', legend=False, ax=ax2)
        st.pyplot(fig2)
    else:
        st.write("No director information available.")

# Show filtered data table
if st.checkbox("Show raw data"):
    st.dataframe(df)
