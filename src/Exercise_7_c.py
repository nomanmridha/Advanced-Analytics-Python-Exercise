import os
import pandas as pd
import matplotlib.pyplot as plt


def load(file_path: str = "dataset/material.xlsx") -> pd.DataFrame:
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
    if extra_periods < 0:
        raise ValueError("extra_periods must be >= 0")
    if n <= 0:
        raise ValueError("n must be > 0")
    if len(d) < n:
        raise ValueError(f"Not enough history: need at least n={n} periods, got {len(d)}")

    d = d.copy().sort_index()
    last_date = d.index.max()
    future_index = pd.date_range(start=last_date + pd.offsets.MonthBegin(1), periods=extra_periods, freq="MS")

    d_ext = pd.concat(
        [d, pd.DataFrame(index=future_index, columns=d.columns, dtype="float64")],
        axis=0
    )
    if extra_periods > 0:
        d_ext.loc[future_index, :] = float("nan")

    f = pd.DataFrame(index=d_ext.index, columns=d_ext.columns, dtype="float64")
    f.loc[d.index, :] = d.rolling(window=n).mean().shift(1)

    if extra_periods > 0:
        first_future = future_index[0]
        f.loc[first_future, :] = d.tail(n).mean(axis=0).values
        for dt in future_index[1:]:
            f.loc[dt, :] = f.loc[first_future, :].values

    return d_ext.astype("float64"), f.astype("float64")


def main():
    d = load()
    d_ext, f = moving_average(d, extra_periods=3, n=4)

    # Copy column 1057 to a new dataframe for plotting
    demand_1057 = d_ext[["1057"]].rename(columns={"1057": "Demand"})
    forecast_1057 = f[["1057"]].rename(columns={"1057": "Forecast"})

    plot_df = pd.concat([demand_1057, forecast_1057], axis=1)

    plot_df.plot(title="Material 1057: Demand vs Moving Average Forecast")
    plt.show()


if __name__ == "__main__":
    main()