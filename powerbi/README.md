# Power BI Implementation

The repository includes Power BI-ready documentation, but a `.pbix` file
requires Power BI Desktop and cannot be generated reliably in this Linux
development environment.

## Import the data

1. Open Power BI Desktop and choose **Get data → Text/CSV**.
2. Select `netflix_data.csv`.
3. Confirm `release_year` and `duration` are numeric.
4. Parse `date_added` as a date in Power Query.
5. Add a calculated `Decade` column:

```DAX
Decade = INT('netflix_data'[release_year] / 10) * 10
```

6. Add the measures in `measures.dax`.
7. Build cards for title count, movie share, average movie duration, and
   missing-value count. Add slicers for type, genre, release year, and decade.

## Suggested report pages

- **Executive Overview:** KPI cards, yearly title trend, and type split.
- **Content Mix:** genre share, country distribution, and director ranking.
- **Movie Deep Dive:** duration distribution and decade comparison.
- **Data Quality:** missing values, duplicates, and refresh timestamp.

This gives the project a BI deliverable path while keeping the source data and
logic version-controlled in GitHub.
