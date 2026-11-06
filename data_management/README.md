# Data Management

This folder documents the dataset contract and provides a repeatable quality
report. Run:

```bash
python data_management/data_quality_check.py
```

The report includes data types, missing-value counts and percentages, and
distinct-value counts. Recommended next steps for a production pipeline are
schema validation, source freshness checks, row-level lineage, and loading
validated data into a warehouse rather than querying the raw CSV directly.
