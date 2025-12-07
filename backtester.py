import pandas as pd

def run_backtest(df):
    df["returns"] = df["price"].pct_change().fillna(0)

    df["strategy_returns"] = df["signal"] * df["returns"]

    df["equity_curve"] = (1 + df["strategy_returns"]).cumprod()

    return df
