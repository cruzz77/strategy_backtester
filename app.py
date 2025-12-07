import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from strategies import momentum_strategy, mean_reversion_strategy
from backtester import Backtester

st.set_page_config(page_title="Quant Backtester", layout="wide")
st.title("Strategy Backtester")

st.sidebar.header("Upload Data")
file = st.sidebar.file_uploader("Upload CSV with 'price' column", type=["csv"])

st.sidebar.header("Strategy Type")
strategy_type = st.sidebar.radio("Choose Strategy", ("Momentum", "Mean Reversion"))

st.sidebar.header("Parameters")

if strategy_type == "Momentum":
    window = st.sidebar.number_input("Momentum Window", 1, 100, 5)
    threshold = st.sidebar.number_input("Return Threshold (%)", 0.0, 5.0, 1.0) / 100
else:
    window = st.sidebar.number_input("Mean Reversion Window", 5, 200, 20)
    z_threshold = st.sidebar.number_input("Z-score Threshold", 0.1, 5.0, 1.5)


if file:
    df = pd.read_csv(file)

    if "price" not in df:
        st.error("CSV needs a `price` column.")
        st.stop()

    prices = df["price"]

    # Generate signals
    if strategy_type == "Momentum":
        signals = momentum_strategy(prices, window, threshold)
    else:
        signals = mean_reversion_strategy(prices, window, z_threshold)

    # Run backtest
    bt = Backtester(prices, signals)
    result = bt.run()

    st.subheader("📊 Equity Curve")
    st.line_chart(result["equity_curve"])

    st.subheader("📈 Price + Signals")
    st.line_chart(result[["price", "signal"]])

    st.subheader("📄 Metrics")
    sharpe = Backtester.sharpe(result["strategy_returns"].dropna())
    mdd = Backtester.max_drawdown(result["equity_curve"])

    st.metric("Sharpe Ratio", f"{sharpe:.2f}")
    st.metric("Max Drawdown", f"{mdd:.2%}")

    st.subheader("📄 Full Backtest Output")
    st.dataframe(result)
else:
    st.info("Upload a CSV to start backtesting.")
