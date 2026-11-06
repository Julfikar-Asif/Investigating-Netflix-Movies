# 🎬 Investigating Netflix Movies

Explore Netflix movie data through an interactive Streamlit dashboard and a
Jupyter Notebook analysis focused on movie trends, genres, directors, and the
1990s.

## 🚀 Live Demo

**[Open the Netflix Content Analysis Dashboard](https://investigating-netflix-movies-ehimlffv3atmdxcr3dkrmw.streamlit.app/)**

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
