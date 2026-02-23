import os
import pandas as pd


def load(file_path: str = "dataset/material.xlsx") -> pd.DataFrame:
    """
    Loads demand data from the excel file and returns a DataFrame where:
      - index   = monthly periods (PeriodIndex, freq='M')
      - columns = material numbers
      - values  = demand
    """

    # 1) Read Excel into a DataFrame
    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"Data file not found: {file_path}\n"
            "Place the Excel file in the workspace or provide a correct path."
        )

    raw = pd.read_excel(file_path)

    # 2) Decide orientation
    # We want: rows = months/periods, columns = materials
    if raw.shape[1] < 2:
        raise ValueError("Excel file seems to have too few columns. Expected periods and materials.")

    first_col_name = raw.columns[0]
    first_col_values = raw.iloc[:, 0].astype(str)

    # If first column looks like 'YYYY-MM' or 'YYYY-MM-DD', treat it as periods
    looks_like_periods = first_col_values.str.match(r"^\d{4}-\d{2}(-\d{2})?$").mean() > 0.6

    if looks_like_periods:
        # Case A: first column is period
        df = raw.set_index(first_col_name)
        df.columns = df.columns.map(str)
    else:
        # Case B: first column is material id -> transpose
        df = raw.set_index(first_col_name).T
        df.columns = df.columns.map(str)

    # 3) Convert index from string to PeriodIndex (monthly) WITHOUT warning
    idx_str = df.index.astype(str)

    # Most common format in your output is YYYY-MM (e.g., 2017-01)
    idx_as_datetime = pd.to_datetime(idx_str, format="%Y-%m", errors="coerce")

    # Drop rows that are not valid dates (e.g., metadata rows)
    valid = ~idx_as_datetime.isna()
    df = df.loc[valid]
    idx_as_datetime = idx_as_datetime[valid]

    if df.empty:
        raise ValueError(
            "After removing non-date rows, no valid period index remained. "
            "Check that the input file contains monthly period rows/columns."
        )

    df.index = idx_as_datetime.to_period("M")

    # 4) Ensure numeric demand values (safe for Excel mixed types)
    df = df.apply(pd.to_numeric, errors="coerce").fillna(0)

    return df


def main():
    try:
        df = load()
    except Exception as e:
        print("Error loading data:", e)
        return

    # Clean, academic output (avoid printing 1000 columns in full)
    print(df.head())
    print("\nShape:", df.shape)
    print("Index type:", type(df.index))
    print("Index freq:", df.index.freqstr)


if __name__ == "__main__":
    main()