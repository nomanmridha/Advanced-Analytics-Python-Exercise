import os
import pandas as pd


def load(file_path: str = "dataset/material.xlsx") -> pd.DataFrame:
    """
    Loads demand data and returns a DataFrame where:
      - index   = DatetimeIndex (monthly, YYYY-MM)
      - columns = material numbers (as strings)
      - values  = demand (float64)
    """

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Data file not found: {file_path}")

    raw = pd.read_excel(file_path)

    if raw.shape[1] < 2:
        raise ValueError("Excel file seems to have too few columns.")

    first_col_name = raw.columns[0]
    first_col_values = raw.iloc[:, 0].astype(str)

    looks_like_periods = first_col_values.str.match(r"^\d{4}-\d{2}(-\d{2})?$").mean() > 0.6

    # Orient to: rows = periods, columns = materials
    if looks_like_periods:
        df = raw.set_index(first_col_name)
        df.columns = df.columns.map(str)
    else:
        df = raw.set_index(first_col_name).T
        df.columns = df.columns.map(str)

    # Convert index to datetime (monthly)
    idx_str = df.index.astype(str)

    # Expecting YYYY-MM (e.g., 2017-01). If there are metadata rows, they'll become NaT and be dropped.
    idx_dt = pd.to_datetime(idx_str, format="%Y-%m", errors="coerce")

    valid = ~idx_dt.isna()
    df = df.loc[valid]
    idx_dt = idx_dt[valid]

    if df.empty:
        raise ValueError("No valid YYYY-MM date rows found after cleaning. Check Excel format.")

    # Set datetime index; normalize to month start (MS-like)
    df.index = idx_dt

    # Ensure numeric float64
    df = df.apply(pd.to_numeric, errors="coerce").astype("float64")

    return df


def main():
    df = load()
    print(df.head())
    print("\nShape:", df.shape)
    print("Index type:", type(df.index))
    print("Index min/max:", df.index.min(), "→", df.index.max())


if __name__ == "__main__":
    main()