import streamlit as st
import pandas as pd
from backtester import run_backtest
from strategies import sma_strategy
from utils import sharpe_ratio, max_drawdown

st.set_page_config(page_title="Quant Backtester", layout="wide")

st.title("📈 Quant Strategy Backtester")

uploaded = st.file_uploader("Upload CSV with 'price' column", type=['csv'])

# Strategy parameters
short_window = st.sidebar.number_input("SMA Short Window", 2, 200, 20)
long_window = st.sidebar.number_input("SMA Long Window", 5, 300, 50)

if uploaded:
    df = pd.read_csv(uploaded)

    if "price" not in df.columns:
        st.error("CSV must contain a 'price' column.")
        st.stop()

    df = sma_strategy(df, short_window, long_window)
    df = run_backtest(df)

    # PLOTS
    st.subheader("📊 Equity Curve")
    st.line_chart(df["equity_curve"])

    st.subheader("📈 Price + SMA Lines")
    st.line_chart(df[["price", "SMA_short", "SMA_long"]])

    st.subheader("📉 Signals")
    st.line_chart(df["signal"])

    # METRICS
    st.header("📄 Metrics")

    sharpe = sharpe_ratio(df["strategy_returns"])
    drawdown = max_drawdown(df["equity_curve"])

    st.write("### Sharpe Ratio")
    st.write(f"{sharpe:.2f}")

    st.write("### Max Drawdown")
    st.write(f"{drawdown * 100:.2f}%")

    # TABLE
    st.header("📄 Full Backtest Output")
    st.dataframe(df)

else:
    st.info("Upload a CSV file to begin.")
