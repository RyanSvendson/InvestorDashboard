## Imports
import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go
from pandas_datareader import data as pdr
yf.pdr_override()

## Start/Stop dates for charts
start_date = "2020-01-1"
end_date = "2023-01-4"

## Indices data from yahoo finance
SP500 = pdr.get_data_yahoo('^GSPC', start = start_date, end=end_date)
SP500['Returns'] = SP500['Close'].pct_change()

DJIA = pdr.get_data_yahoo('^DJI', start = start_date, end=end_date)
DJIA['Returns'] = DJIA['Close'].pct_change()

NASDAQ = pdr.get_data_yahoo('^IXIC', start = start_date, end=end_date)
NASDAQ['Returns'] = NASDAQ['Close'].pct_change()

RUSSELL = pdr.get_data_yahoo('^RUT', start = start_date, end=end_date)
RUSSELL['Returns'] = RUSSELL['Close'].pct_change()

VIX = pdr.get_data_yahoo('^VIX', start = start_date, end=end_date)
VIX['Returns'] = VIX['Close'].pct_change()

## streamlit code
st.title('Broad Market Indices')
st.header('Key Economic Indicators')
st.write('This dashboard page shows several indices charting the overall market conditions of the past 3 years.')
Index_1 = st.selectbox("Select an Index:", ('S&P 500', 'Dow Jones Industrial Average', 'Nasdaq Composite', 'Russell 2000', 'CBOE Volatility Index'))
    
if Index_1 == 'S&P 500':
    st.write("The Standard and Poor's 500 is a stock market index tracking the stock performance of 500 large companies listed on the stock exchanges in the United States and has a market cap of $35.1 trillion (as of August 31, 2022).")
    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(x=SP500.index, y=SP500['Close'], mode='lines', name='S&P 500'))
    fig1.update_xaxes(type='category')
    fig1.update_layout(height=600, width=400)
    st.plotly_chart(fig1, use_container_width=True)
    st.dataframe(SP500)
    st.write('Source: Yahoo Finance')

if Index_1 == 'Dow Jones Industrial Average':
    st.write("The Dow Jones Industrial Average is a stock market index of 30 prominent companites listed on stock exchanges in the United States.  It is one of the oldest and most commonly followed equity indices and has a market cap of $10.35 trillion")
    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=DJIA.index, y=DJIA['Close'], mode='lines', name='Dow Jones Industrial Average'))
    fig2.update_xaxes(type='category')
    fig2.update_layout(height=600, width=400)
    st.plotly_chart(fig2, use_container_width=True)
    st.dataframe(DJIA)
    st.write('Source: Yahoo Finance')

if Index_1 == 'Nasdaq Composite':
    st.write("the Nasdaq Composite is a stock market index that includes almost all stocks listed on the Nasdaq stock exchange.")
    fig3 = go.Figure()
    fig3.add_trace(go.Scatter(x=NASDAQ.index, y=NASDAQ['Close'], mode='lines', name='Nasdaq Composite'))
    fig3.update_xaxes(type='category')
    fig3.update_layout(height=600, width=400)
    st.plotly_chart(fig3, use_container_width=True)
    st.dataframe(NASDAQ)
    st.write('Source: Yahoo Finance')

if Index_1 == 'Russell 2000':
    st.write("the Russell 2000 is a small-cap stock market index that makes up the smallest 2,000 stocks in the Russell 3000 index.")
    fig4 = go.Figure()
    fig4.add_trace(go.Scatter(x=RUSSELL.index, y=RUSSELL['Close'], mode='lines', name='Russell 2000'))
    fig4.update_xaxes(type='category')
    fig4.update_layout(height=600, width=400)
    st.plotly_chart(fig4, use_container_width=True)
    st.dataframe(RUSSELL)
    st.write('Source: Yahoo Finance')
    
if Index_1 == 'CBOE Volatility Index':
    st.write("the Chicago Board Options Exchange's Volatility Index is a popular measure of the stock market's expectation of volatility based on S&P 500 index options.")
    fig5 = go.Figure()
    fig5.add_trace(go.Scatter(x=VIX.index, y=VIX['Close'], mode='lines', name='VIX'))
    fig5.update_xaxes(type='category')
    fig5.update_layout(height=600, width=400)
    st.plotly_chart(fig5, use_container_width=True)
    st.dataframe(VIX)
    st.write('Source: Yahoo Finance')