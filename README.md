# Strategy Backtester

A lightweight, fast, and modular Streamlit-based backtesting tool for exploring quantitative trading strategies such as SMA crossover on sample market data.

This project allows you to:

*   Upload your own CSV price data
*   Automatically compute indicators (SMA short, SMA long)
*   Generate buy/sell signals
*   Backtest the strategy to compute returns, equity curve, Sharpe ratio & drawdowns
*   Visualize everything in an interactive dashboard

## Features

### 1. CSV File Upload
Upload a CSV containing data with the following required columns:
`time`, `price`, `volume`


### 2. SMA Crossover Strategy
This backtester applies a classic technical strategy:
*   **SMA Short Window** (default: 10)
*   **SMA Long Window** (default: 50)

**Signal Rules:**
*   If `SMA_short > SMA_long` → BUY (`signal = 1`)
*   If `SMA_short < SMA_long` → SELL (`signal = -1`)
*   Else → HOLD (`signal = 0`)

A 1-bar shift is applied to avoid lookahead bias.

### 3. Strategy Backtesting
The backtest calculates:
*   Daily returns
*   Strategy returns
*   Cumulative equity curve
*   Sharpe Ratio
*   Maximum Drawdown

### 4. Streamlit UI
The dashboard displays:
*   📈 Equity Curve
*   📉 Price chart with SMA overlays
*   🔁 Signal Chart
*   🧮 Performance Metrics
*   📄 Full Backtest Output Table

Everything is interactive and updates instantly when parameters change.
