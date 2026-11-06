# Data Dictionary

| Column | Description | Quality rule |
|---|---|---|
| `show_id` | Unique catalog identifier | Required and unique |
| `type` | `Movie` or `TV Show` | Must be one of the two values |
| `title` | Catalog title | Required |
| `director` | Director or directors | Nullable |
| `cast` | Cast members | Nullable |
| `country` | Production country or countries | Nullable |
| `date_added` | Date added to the catalog | Nullable; parse as a date |
| `release_year` | Original release year | Numeric and plausible |
| `duration` | Movie minutes or TV seasons | Numeric; interpret using `type` |
| `description` | Catalog description | Nullable |
| `genre` | Primary dataset genre label | Required for segmentation |

`duration` has different business meaning by content type: minutes for movies
and seasons for TV shows. The dashboard therefore uses movie duration metrics
only when `type = 'Movie'`.
