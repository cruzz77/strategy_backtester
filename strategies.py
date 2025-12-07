# long if > threshold | short if < -threshold
import pandas as pd

def momentum_strategy(prices: pd.Series, window: int = 5, threshold: float = 0.01):
    returns = prices.pct_change(window)
    signal = (returns > threshold).astype(int)       
    signal[returns < -threshold] = -1                
    return signal.fillna(0)


def mean_reversion_strategy(prices: pd.Series, window: int = 20, z_threshold: float = 1.5):
    ma = prices.rolling(window).mean()
    std = prices.rolling(window).std()

    zscore = (prices - ma) / std

    signal = (-zscore).apply(lambda z: 1 if z > z_threshold else (-1 if z < -z_threshold else 0))

    return signal.fillna(0)
