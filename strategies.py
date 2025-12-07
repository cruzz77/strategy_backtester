import pandas as pd

def sma_strategy(df, short_window=20, long_window=50):
    df["SMA_short"] = df["price"].rolling(short_window).mean()
    df["SMA_long"] = df["price"].rolling(long_window).mean()

    df["signal"] = 0
    df.loc[df["SMA_short"] > df["SMA_long"], "signal"] = 1
    df.loc[df["SMA_short"] < df["SMA_long"], "signal"] = -1

    # Avoid lookahead bias
    df["signal"] = df["signal"].shift(1).fillna(0)
    

    return df
