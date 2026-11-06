-- SQL analysis examples for a table named netflix_data.
-- Load netflix_data.csv into your SQL database before running these queries.

-- 1. Catalog overview
SELECT
    type,
    COUNT(*) AS title_count,
    ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 2) AS share_percent
FROM netflix_data
GROUP BY type
ORDER BY title_count DESC;

-- 2. Yearly release trend
SELECT
    release_year,
    type,
    COUNT(*) AS title_count
FROM netflix_data
GROUP BY release_year, type
ORDER BY release_year, type;

-- 3. Top genres
SELECT
    genre,
    COUNT(*) AS title_count,
    ROUND(AVG(duration), 1) AS average_duration_minutes
FROM netflix_data
WHERE genre IS NOT NULL
GROUP BY genre
ORDER BY title_count DESC
LIMIT 10;

-- 4. 1990s movie analysis
SELECT
    genre,
    COUNT(*) AS movie_count,
    ROUND(AVG(duration), 1) AS average_duration_minutes
FROM netflix_data
WHERE type = 'Movie'
  AND release_year BETWEEN 1990 AND 1999
GROUP BY genre
ORDER BY movie_count DESC;

-- 5. Data-quality profile
SELECT
    COUNT(*) AS total_rows,
    SUM(CASE WHEN title IS NULL OR TRIM(title) = '' THEN 1 ELSE 0 END) AS missing_titles,
    SUM(CASE WHEN release_year IS NULL THEN 1 ELSE 0 END) AS missing_release_years,
    SUM(CASE WHEN genre IS NULL OR TRIM(genre) = '' THEN 1 ELSE 0 END) AS missing_genres,
    SUM(CASE WHEN duration IS NULL THEN 1 ELSE 0 END) AS missing_durations
FROM netflix_data;
