#import os
import pandas as pd
import plotly.graph_objects as go
from yahoo_fin import stock_info as si
import yfinance as yf
import streamlit as st

# Automate stock pages after reading in excel file
# def initialize_pages(stock_list):
# #clear or create pages folder
#     """
#     current_directory = os.getcwd()
#     final_directory = os.path.join(current_directory, r'pages')
#     if not os.path.exists(final_directory):
#         os.makedirs(final_directory)
#
#     OR clear
#
#     directory = './pages'
#     for file in os.listdir(directory):
#         os.remove(os.path.join(directory, file))
#     """
# #save file for each stock with page layout


# Update df with live price
def update_df(df):

    counter = 0
    for ticker in df['SYMBOL']:
        df.at[counter,'CURRENT PRICE'] = round(si.get_live_price(ticker), 2)
        counter+=1
    df['CURRENT VALUE'] = df['QUANTITY'] * df['CURRENT PRICE']
    df['UNREALIZED P&L'] = df['CURRENT VALUE'] - df['PURCHASE COST']
    #df['AVG PURCHASE PRICE'] if needed for sidebar trading
    return df
    
# Dataframe for portfolio performance
def pf_performance(df):
    # Set up dataframe with stock['close']
    performance_df = pd.DataFrame()
    for stock in df['SYMBOL']:
        stock_data = yf.Ticker(stock)
        stock_df = stock_data.history(period='1d', start='2022-01-03', end=None)
        performance_df[stock]=(stock_df['Close'])

    # Multiply stock quantity to each column
    for stock in performance_df:
        performance_df[stock] = performance_df[stock]*10 #shortcut 10 stocks for each stock
        performance_df['Total'] = round(performance_df[['TSLA', 'AAPL', 'MSFT', 'AMZN', 'JNJ']].sum(axis=1),2)

    return performance_df

def prev_close(ticker):
    prev_close = yf.Ticker(ticker).history()
    prev_close = prev_close['Close'].iloc[-2]
    return prev_close


def fig2(df):

    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=df.index, y=df['Total'], mode='lines'))
    fig2.update_xaxes(type='category')
    fig2.update_layout(margin=dict(t=30, b=0, l=0, r=0))
    return fig2

def fig1(df):
    a = df.at[0,'PURCHASE COST']
    b = df.at[1,'PURCHASE COST']
    c = df.at[2,'PURCHASE COST']
    d = df.at[3,'PURCHASE COST']
    e = df.at[4,'PURCHASE COST']
    f = df.at[0,'CURRENT VALUE']
    g = df.at[1,'CURRENT VALUE']
    h = df.at[2,'CURRENT VALUE']
    i = df.at[3,'CURRENT VALUE']
    j = df.at[4,'CURRENT VALUE']

    data = [# Portfolio (inner donut)
    go.Pie(values=[a, b, c, d, e],
    labels=['TSLA', 'AAPL', 'MSFT', 'AMZN', 'JNJ'],
    domain={'x':[0.15,0.85], 'y':[0.15,0.85]},
    hole=0.4,
    direction='clockwise',
    sort=False),
    #marker={'colors':['#CB4335','#2E86C1']}),
    # Individual components (outer donut)
    go.Pie(values=[ f, g, h, i, j],
    labels=['TSLA', 'AAPL', 'MSFT', 'AMZN', 'JNJ'],
    domain={'x':[0,1], 'y':[0,1]},
    hole=0.74,
    direction='clockwise',
    sort=False,
    marker={'colors':['#EC7063','#F1948A','#5DADE2','#85C1E9']},
    showlegend=False,
    opacity=0.9,
    rotation=38)]

    fig = go.Figure(data=data, layout={'title':'Portfolio Allocation'})
    fig.update_layout(
        margin=dict(t=35, b=20, l=30, r=20), 
        title={'x':0.45},
        font=dict(size=18))
    return fig


def fig2(df):

    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=df.index, y=df['Total'], mode='lines'))
    fig2.update_xaxes(type='category')
    fig2.update_layout(margin=dict(t=30, b=0, l=0, r=0))
    return fig2

# SIDEBAR TRADING FUNCTIONS
# def pf_history(stock_list):
#     '''
#     total_asset = 0
#     for stock in stock_list:
#     '''    

# def buy_stock(amount, stock, df):
#     '''df.at[]'''

# def sell_stock(amount, stock, df):
#     """"""