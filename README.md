# 🎬 Investigating Netflix Movies

![Netflix](https://img.shields.io/badge/Netflix-E50914?style=for-the-badge&logo=netflix&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37726?style=for-the-badge&logo=jupyter&logoColor=white)
![Data Analysis](https://img.shields.io/badge/Data%20Analysis-EDA-blue?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

> A comprehensive exploratory data analysis (EDA) of Netflix movies from the 1990s, uncovering trends, patterns, and insights in the golden age of cinema.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Key Objectives](#key-objectives)
- [Key Findings](#key-findings)
- [Dataset](#dataset)
- [Requirements](#requirements)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technologies](#technologies)
- [Key Insights](#key-insights)
- [Contributing](#contributing)
- [License](#license)

---

## 📊 Overview

This project performs an **in-depth exploratory data analysis (EDA)** on Netflix's 1990s movie catalog, revealing fascinating trends about movie durations, genres, and production patterns during this pivotal decade in cinema history.

Whether you're a data enthusiast, filmmaker, or film historian, this analysis provides valuable insights into how movies were made and distributed during the 1990s.

---

## 🎯 Key Objectives

| Objective | Description |
|-----------|-------------|
| **Filter Data** | Identify all movies released between 1990 and 1999 |
| **Find Frequent Duration** | Determine the most common movie length (in minutes) during this period |
| **Count Short Action Movies** | Count how many 'Action' movies from the 1990s are shorter than 90 minutes |

---

## 🔍 Key Findings

| Finding | Result |
|---------|--------|
| 📌 **Most Frequent Movie Duration** | **94 minutes** |
| 🎬 **Short Action Movies (<90 min)** | **7 movies** |

These findings reveal interesting patterns about how movies were packaged and distributed during the 1990s era.

---

## 📦 Dataset

**File**: `netflix_data.csv`

**Contents**:
- Movie titles
- Genres (Action, Drama, Comedy, etc.)
- Release years (1990-1999 focus)
- Movie durations (in minutes)
- Additional metadata

---

## 🛠️ Requirements

- Python 3.7+
- Jupyter Notebook
- pandas
- numpy
- matplotlib
- seaborn

---

## 📥 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Julfikar-Asif/Investigating-Netflix-Movies.git
cd Investigating-Netflix-Movies
```

### 2. Install Dependencies
```bash
pip install pandas numpy matplotlib seaborn jupyter
```

### 3. Launch Jupyter Notebook
```bash
jupyter notebook
```

---

## 🚀 Usage

1. **Open the notebook**: Click on the Jupyter Notebook file in your browser
2. **Run the cells**: Execute each cell sequentially to see the analysis unfold
3. **Explore the visualizations**: Review charts, graphs, and statistical summaries
4. **Modify & experiment**: Feel free to change parameters and explore further

### Example Analysis Steps:
```python
# Filter 1990s movies
movies_1990s = netflix_data[netflix_data['release_year'].between(1990, 1999)]

# Find most common duration
most_common_duration = movies_1990s['duration'].mode()[0]

# Count short action movies
short_action_movies = movies_1990s[(movies_1990s['genre'] == 'Action') & 
                                    (movies_1990s['duration'] < 90)]
```

---

## 📁 Project Structure

```
Investigating-Netflix-Movies/
├── README.md                    # This file
├── netflix_data.csv            # Main dataset
├── analysis_notebook.ipynb      # Primary analysis notebook
└── output/                      # Generated visualizations & reports
    └── findings_summary.txt
```

---

## 💻 Technologies

- **Python 3** - Programming language
- **Jupyter Notebook** - Interactive analysis environment
- **Pandas** - Data manipulation & analysis
- **NumPy** - Numerical computations
- **Matplotlib & Seaborn** - Data visualization

---

## 💡 Key Insights

### Duration Trends
The 94-minute sweet spot suggests filmmakers in the 1990s aimed for a specific runtime that balanced theatrical requirements with audience engagement.

### Action Genre Analysis
Finding only 7 short action movies (<90 minutes) indicates that action films during this era were typically feature-length productions, not short-form content.

### What This Means
These patterns reflect the pre-streaming era when movies were primarily distributed through theaters, requiring specific runtime standards.

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your work (`git commit -m 'Add improvement'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Open a Pull Request

---

## 📄 License

This project is open source and available under the MIT License.

---

## 👤 Author

**Julfikar-Asif**
- GitHub: [@Julfikar-Asif](https://github.com/Julfikar-Asif)

---

### ⭐ If you found this analysis helpful, please consider starring the repository!
