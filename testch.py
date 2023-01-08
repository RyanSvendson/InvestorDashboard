##Imports
import streamlit as st
import os
import pandas as pd
import yfinance as yf
import datetime
import requests
import plotly.graph_objects as go
from pandas_datareader import data as pdr
yf.pdr_override()
from datetime import date, datetime as dt



#Today = datetime.date.today()
#Start2021 = datetime.date(2021, 1, 1)
#diff = Start2021 - Today

#purchase_date = '2008-01-01'
start_date = "2020-01-1"
end_date = "2023-01-4"


#AAPL = pdr.get_data_yahoo('AAPL', start = start_date, end=end_date)
#AAPL['Returns'] = AAPL['Close'].pct_change()

VIX = pdr.get_data_yahoo('^VIX', start = start_date, end=end_date)
VIX['Returns'] = VIX['Close'].pct_change()

SNP_IDX = pdr.get_data_yahoo('^GSPC', start = start_date, end=end_date)
SNP_IDX['Returns'] = SNP_IDX['Close'].pct_change()

##streamlit code
st.title('Tracking Monitor')

option = st.sidebar.selectbox("Select a dashboard:", ('KEI', 'ITA'))

if option == 'KEI':
    st.header('Key Economic Indicators')
    st.write('This dashboard screen showss key economic indicators.')
    Indicator_1 = st.selectbox("Select an Indicator:", ('VIX', 'S&P Index'))
    if Indicator_1 == 'VIX':
        fig1 = go.Figure()
        fig1.add_trace(go.Scatter(x=VIX.index, y=VIX['Close'], mode='lines', name='VIX'))
        fig1.update_xaxes(type='category')
        fig1.update_layout(height=600, width=400)
        st.plotly_chart(fig1, use_container_width=True)
        st.dataframe(AAPL)
        st.write('Source: Yahoo Finance')

    if Indicator_1 == 'S&P Index':
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=SNP_IDX.index, y=SNP_IDX['Close'], mode='lines', name='SNP_IDX'))
        fig2.update_xaxes(type='category')
        fig2.update_layout(height=600, width=400)
        st.plotly_chart(fig2, use_container_width=True)
        st.dataframe(SNP_IDX)
        st.write('Source: Yahoo Finance')

    
