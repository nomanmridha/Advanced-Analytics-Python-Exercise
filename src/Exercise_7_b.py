import os
import pandas as pd


def load(file_path: str = "dataset/material.xlsx") -> pd.DataFrame:
    """Same load as Exercise_7_a: returns demand with DatetimeIndex and float64 values."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Data file not found: {file_path}")

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

    idx_dt = pd.to_datetime(df.index.astype(str), format="%Y-%m", errors="coerce")
    valid = ~idx_dt.isna()
    df = df.loc[valid]
    idx_dt = idx_dt[valid]
    if df.empty:
        raise ValueError("No valid YYYY-MM date rows found after cleaning. Check Excel format.")

    df.index = idx_dt
    df = df.apply(pd.to_numeric, errors="coerce").astype("float64")
    return df


def moving_average(d: pd.DataFrame, extra_periods: int, n: int) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Returns (d_ext, f):

    d_ext: original demand dataframe extended by extra_periods rows with NaN,
           with correct subsequent monthly DatetimeIndex.

    f: forecast dataframe (float64), same index/columns as d_ext.
       - For historical periods: forecast(t) = mean(demand[t-n : t])  (previous n actuals)
         so it begins at period n+1.
       - For future periods: first extra period forecast = mean(last n actuals),
         remaining extra periods carry-forward that same value.
    """
    if extra_periods < 0:
        raise ValueError("extra_periods must be >= 0")
    if n <= 0:
        raise ValueError("n must be > 0")
    if len(d) < n:
        raise ValueError(f"Not enough history: need at least n={n} periods, got {len(d)}")

    d = d.copy()
    d = d.sort_index()

    # --- extend demand index by extra_periods months ---
    last_date = d.index.max()
    future_index = pd.date_range(
        start=last_date + pd.offsets.MonthBegin(1),
        periods=extra_periods,
        freq="MS",
    )

    d_ext = pd.concat(
        [d, pd.DataFrame(index=future_index, columns=d.columns, dtype="float64")],
        axis=0
    )

    # Ensure NaN in the added rows (explicit)
    if extra_periods > 0:
        d_ext.loc[future_index, :] = float("nan")

    # --- build forecast dataframe f (same shape/index/columns) ---
    f = pd.DataFrame(index=d_ext.index, columns=d_ext.columns, dtype="float64")

    # Historical moving average forecasts (start at n+1):
    # rolling(n).mean() gives mean including current row, so shift(1) to use previous n only
    hist_forecast = d.rolling(window=n).mean().shift(1)
    f.loc[d.index, :] = hist_forecast

    # Future forecasts: only first future period computed, remaining carried forward
    if extra_periods > 0:
        first_future = future_index[0]
        first_future_forecast = d.tail(n).mean(axis=0)  # mean of last n actuals per material

        f.loc[first_future, :] = first_future_forecast.values

        if extra_periods > 1:
            # carry forward unchanged for remaining future periods
            for dt in future_index[1:]:
                f.loc[dt, :] = f.loc[first_future, :].values

    return d_ext.astype("float64"), f.astype("float64")


def main():
    d = load()
    d_ext, f = moving_average(d, extra_periods=3, n=4)

    print("\n=== demand (extended) ===")
    print(d_ext.tail(12))

    print("\n=== forecast (moving average) ===")
    print(f.tail(12))

    print("\nShapes:")
    print("d_ext:", d_ext.shape, "f:", f.shape)


if __name__ == "__main__":
    main()
    