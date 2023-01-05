import pandas as pd
import yfinance as fy
import datetime
import streamlit as st
import plotly
import plotly.graph_objects as go
from pandas_datareader import data as wb
import requests

st.set_page_config(
    page_title="Investor Dashboard",
    page_icon="👋",
)

tickers = ["TSLA", "AAPL", "MSFT","AMZN", "JNJ"]



st.write("# Portfolio Overview")
st.write("Current performance of your investment portfolio")
st.selectbox("Select an asset:", tickers, 0)
st.sidebar.success("Select a demo above.")

st.markdown(
    """
"""
)

