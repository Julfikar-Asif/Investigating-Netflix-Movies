# SQL Analysis

`netflix_analysis.sql` contains portable SQL queries for catalog summaries,
release trends, genre analysis, the 1990s deep dive, and data-quality checks.

Example with SQLite:

```bash
sqlite3 netflix.db
```

```sql
.mode csv
.import netflix_data.csv netflix_data
.read sql/netflix_analysis.sql
```

The queries are intentionally written against a simple `netflix_data` table so
they can be adapted to PostgreSQL, MySQL, SQL Server, or a cloud warehouse.
