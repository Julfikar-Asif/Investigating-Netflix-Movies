# 🎬 Investigating Netflix Movies

Explore Netflix movie data through an interactive Streamlit dashboard and a
Jupyter Notebook analysis focused on movie trends, genres, directors, and the
1990s.

## 🚀 Live Demo

**[Open the Netflix Content Analysis Dashboard](https://investigating-netflix-movies-ehimlffv3atmdxcr3dkrmw.streamlit.app/)**

## 🖼️ Website Preview

![Netflix Content Analysis Dashboard](assets/netflix-dashboard.png)

## 📌 Overview

This project analyzes Netflix content using Python and presents the results in
an interactive dashboard. The dashboard includes historical trends, a focused
analysis of 1990s movies, genre and director breakdowns, descriptive
statistics, and an optional raw-data table.

## ✨ Features

- Filter titles by genre.
- View total titles, average movie duration, and the most common genre.
- Compare average movie duration and movie volume by decade.
- Explore movie-duration distributions.
- Analyze 1990s movie durations and top genres.
- Review genre share and the most prolific directors.
- Inspect correlation, numeric statistics, categorical statistics, and raw data.

## 🧰 What I Used

- **Python** to build the analysis and dashboard.
- **Pandas** to load, clean, filter, group, and summarize the Netflix dataset.
- **Matplotlib** and **Seaborn** to create charts such as line plots, bar charts,
  histograms, pie charts, and the correlation heatmap.
- **Streamlit** to turn the analysis into an interactive web application with
  genre filters, tabs, metrics, tables, and visualizations.
- **Jupyter Notebook** to document and rerun the exploratory 1990s analysis.
- **GitHub** to store the source code and dataset, with **Streamlit Community
  Cloud** used to publish the live dashboard.

## 🔬 How I Used These Tools

1. Loaded `netflix_data.csv` with Pandas and derived a decade column from each
   title's release year.
2. Filtered the catalog to movies and created reusable summaries for duration,
   genre, decade, and director analysis.
3. Investigated movies released from 1990 through 1999 to find the most common
   duration and count short Action movies.
4. Built charts with Matplotlib and Seaborn to show duration distributions,
   decade trends, genre share, director counts, and correlations.
5. Added the analysis to Streamlit so users can filter genres, switch between
   dashboard sections, inspect statistics, and view the raw data.
6. Deployed `app.py` to Streamlit Community Cloud and linked the live app above.

## 🔎 Key Findings

The original 1990s analysis found:

- The most frequent movie duration was **94 minutes**.
- There were **7 Action movies shorter than 90 minutes**.

## 📂 Dataset

The project uses [`netflix_data.csv`](netflix_data.csv), which contains Netflix
title metadata including:

- Title and content type
- Genre
- Release year
- Movie duration
- Director and other catalog information

## 🛠️ Tech Stack

- Python
- Streamlit
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook

## ⚙️ Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Julfikar-Asif/Investigating-Netflix-Movies.git
cd Investigating-Netflix-Movies
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start the dashboard

```bash
streamlit run app.py
```

Streamlit will provide a local URL, usually
`http://localhost:8501`.

### 4. Explore the notebook

Open `Investigating_Netflix_Movies.ipynb` in Jupyter Notebook or JupyterLab to
review and rerun the exploratory analysis.

## 📁 Project Structure

```text
Investigating-Netflix-Movies/
├── app.py                              # Streamlit dashboard
├── Investigating_Netflix_Movies.ipynb # Exploratory analysis
├── netflix_data.csv                    # Netflix dataset
├── assets/netflix-dashboard.png        # Dashboard screenshot
├── requirements.txt                    # Python dependencies
└── README.md                           # Project documentation
```

## 🤝 Contributing

1. Fork the repository.
2. Create a feature branch.
3. Make your changes.
4. Open a pull request.

## 👤 Author

**Julfikar-Asif** · [GitHub](https://github.com/Julfikar-Asif)
