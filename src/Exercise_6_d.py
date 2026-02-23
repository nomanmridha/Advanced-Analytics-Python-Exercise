import os
import pandas as pd


def load(file_path: str = "dataset/material.xlsx") -> pd.DataFrame:
    """
    Loads demand data and returns a DataFrame where:
      - index   = monthly periods (PeriodIndex)
      - columns = material numbers
      - values  = demand
    """

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Data file not found: {file_path}")

    raw = pd.read_excel(file_path)

    first_col_name = raw.columns[0]
    first_col_values = raw.iloc[:, 0].astype(str)

    looks_like_periods = first_col_values.str.match(r"^\d{4}-\d{2}(-\d{2})?$").mean() > 0.6

    if looks_like_periods:
        df = raw.set_index(first_col_name)
        df.columns = df.columns.map(str)
    else:
        df = raw.set_index(first_col_name).T
        df.columns = df.columns.map(str)

    idx_str = df.index.astype(str)
    idx_as_datetime = pd.to_datetime(idx_str, format="%Y-%m", errors="coerce")

    valid = ~idx_as_datetime.isna()
    df = df.loc[valid]
    idx_as_datetime = idx_as_datetime[valid]

    df.index = idx_as_datetime.to_period("M")

    df = df.apply(pd.to_numeric, errors="coerce").fillna(0)

    return df


def main():

    try:
        df = load()
    except Exception as e:
        print("Error loading data:", e)
        return


    # Extract Series for period '2018-12'
    period_series = df.loc["2018-12"]

    print("\n=== Demand series for period 2018-12 ===\n")
    print(period_series)

    print("\nSeries info:")
    print("Type:", type(period_series))
    print("Length:", len(period_series))


if __name__ == "__main__":
    main()