import os
import pandas as pd


def load(file_path: str = "dataset/material.xlsx") -> pd.DataFrame:
    """
    Loads demand data from the excel file and returns a DataFrame where:
      - index   = monthly periods (PeriodIndex, freq='M')
      - columns = material numbers
      - values  = demand
    """

    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"Data file not found: {file_path}\n"
            "Place the Excel file in the workspace or provide a correct path."
        )

    raw = pd.read_excel(file_path)

    if raw.shape[1] < 2:
        raise ValueError("Excel file seems to have too few columns.")

    first_col_name = raw.columns[0]
    first_col_values = raw.iloc[:, 0].astype(str)

    looks_like_periods = first_col_values.str.match(r"^\d{4}-\d{2}(-\d{2})?$").mean() > 0.6

    if looks_like_periods:
        df = raw.set_index(first_col_name)
        df.columns = df.columns.map(str)
    else:
        df = raw.set_index(first_col_name).T
        df.columns = df.columns.map(str)

    # Convert index safely to PeriodIndex
    idx_str = df.index.astype(str)
    idx_as_datetime = pd.to_datetime(idx_str, format="%Y-%m", errors="coerce")

    valid = ~idx_as_datetime.isna()
    df = df.loc[valid]
    idx_as_datetime = idx_as_datetime[valid]

    df.index = idx_as_datetime.to_period("M")

    # Ensure numeric values
    df = df.apply(pd.to_numeric, errors="coerce").fillna(0)

    return df


def main():

    try:
        df = load()
    except Exception as e:
        print("Error loading data:", e)
        return

    print("\n=== Dataset Description (describe()) ===\n")

    description = df.describe()

    print(description)

    print("\nShape:", description.shape)


if __name__ == "__main__":
    main()