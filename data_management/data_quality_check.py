"""Create a data-quality report for netflix_data.csv."""

import argparse
from pathlib import Path

import pandas as pd


def build_quality_report(data_path: str) -> pd.DataFrame:
    data = pd.read_csv(data_path)
    report = pd.DataFrame(
        {
            "column": data.columns,
            "dtype": data.dtypes.astype(str).values,
            "missing_count": data.isna().sum().values,
            "missing_percent": (data.isna().mean().mul(100).round(2)).values,
            "distinct_count": data.nunique(dropna=True).values,
        }
    )
    return report.sort_values(["missing_percent", "column"], ascending=[False, True])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", default="netflix_data.csv")
    parser.add_argument("--output", default="artifacts/data_quality_report.csv")
    args = parser.parse_args()
    report = build_quality_report(args.data)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    report.to_csv(output, index=False)
    print(report.to_string(index=False))
