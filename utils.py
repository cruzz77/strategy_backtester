import numpy as np

def sharpe_ratio(returns, freq=252):
    std = returns.std()
    if std == 0:
        return 0
    return (returns.mean() / std) * np.sqrt(freq)

def max_drawdown(series):
    rolling_max = series.cummax()
    dd = (series - rolling_max) / rolling_max
    return dd.min()
