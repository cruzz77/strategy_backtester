# 1 = long, -1 = short, 0 = flat
import pandas as pd
import numpy as np

class Backtester:
    def __init__(self, prices: pd.Series, signals: pd.Series):
        self.prices = prices
        self.signals = signals 

    def run(self):
        df = pd.DataFrame({
            "price": self.prices,
            "signal": self.signals
        })

        # daily returns
        df["returns"] = df["price"].pct_change()

        # strategy returns = returns * previous signal
        df["strategy_returns"] = df["returns"] * df["signal"].shift(1)

        df["equity_curve"] = (1 + df["strategy_returns"].fillna(0)).cumprod()

        return df

    @staticmethod
    def sharpe(returns):
        return np.sqrt(252) * returns.mean() / returns.std() if returns.std() != 0 else 0

    @staticmethod
    def max_drawdown(equity_curve):
        roll_max = equity_curve.cummax()
        drawdown = equity_curve / roll_max - 1
        return drawdown.min()
