
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Netflix Movie Trends Analysis")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('/content/netflix_data.csv')
    df['decade'] = (df['release_year'] // 10) * 10
    return df

df = load_data()

st.header("Key Statistics")
col1, col2 = st.columns(2)
with col1:
    st.metric("Top Genre", "Dramas")
with col2:
    st.metric("Peak Year", "2017")

st.subheader("Average Movie Duration per Decade")
decade_avg = df[df['type'] == 'Movie'].groupby('decade')['duration'].mean().reset_index()
fig, ax = plt.subplots()
sns.lineplot(data=decade_avg, x='decade', y='duration', marker='o', ax=ax)
st.pyplot(fig)

st.subheader("Top 5 Genres")
top_5 = df['genre'].value_counts().head(5)
st.bar_chart(top_5)
