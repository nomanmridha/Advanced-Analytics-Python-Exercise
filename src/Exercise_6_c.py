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


    # PART 1: Extract material '1500' as Series
    material_1500 = df["1500"]

    print("\n=== Demand series for material 1500 ===\n")
    print(material_1500)


    # PART 2: Calculate sum of material '1057'
    sum_1057 = df["1057"].sum()

    print("\n=== Total demand for material 1057 ===\n")
    print(sum_1057)


if __name__ == "__main__":
    main()