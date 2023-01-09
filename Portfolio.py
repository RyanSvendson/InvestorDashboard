import pandas as pd
import datetime
import streamlit as st
import plotly.graph_objects as go
import time
import dashboard_features as dbf

st.set_page_config(
    page_title="Investor Dashboard",
    page_icon="👋",
    layout="wide"
)

# Read in portfolio data
portfolio_df = pd.read_excel("./portfolio_example.xlsx")
# transact_df = portfolio_df.copy()

#tickers = portfolio_df['SYMBOL']

# Header
st.write("# Portfolio Overview")
st.write("Current performance of your investment portfolio...")
st.write("")
st.write("")

st.sidebar.write("Feature below is under construction.")
# Sidebar for stock transaction
buysell_stock = st.sidebar.selectbox(
    "Select stock to buy or sell.",
    ("TSLA","AAPL","MSFT","AMZN","JNJ")
)

# Quantity input
amount = st.sidebar.number_input("Quantity", min_value=0)

#Buy or Sell w/ transact button
buysell = st.sidebar.selectbox("Would you like to buy or sell?", ("Buy", "Sell"))
if st.sidebar.button("Transact"):

    if buysell_stock == "TSLA":
        buysell_stock = 0
    elif buysell_stock == "AAPL":
        buysell_stock = 1
    elif buysell_stock == "MSFT":
        buysell_stock = 2
    elif buysell_stock == "AMZN":
        buysell_stock = 3
    else: #buysell_stock == "JNJ":
        buysell_stock = 4

    if buysell == "Buy":
        #can add check balance feature
        #dbf.buy_stock(amount, buysell_stock, portfolio_df)
        st.sidebar.success("Transaction confirmed!", icon = "✅")   
    elif buysell == "Sell" and amount <= portfolio_df.at[buysell_stock, 'QUANTITY']:
        #dbf.sell_stock(amount, buysell_stock, portfolio_df)
        st.sidebar.success("Transaction confirmed!", icon = "✅")
    elif buysell == "Sell" and amount >= portfolio_df.at[buysell_stock, 'QUANTITY']:
        st.sidebar.write("Transaction canceled.")
        st.sidebar.write(" Warning: You do not have enough stocks to sell, you may only input value at or below total stock. ")





# Live dashboard
placeholder = st.empty()

for seconds in range(100):

    # Update ticker price & info in df (DASHBOARD FEATURES)
    dbf.update_df(portfolio_df)
    unrealized_pl = portfolio_df['UNREALIZED P&L'].sum()
    current_pf_value = portfolio_df['CURRENT VALUE'].sum()
    

    with placeholder.container():

        fig_col1, fig_col2, fig_col3, fig_col4, fig_col5 = st.columns([5.5,0.25,1,0.25,1], gap='small')
        #col2 and col4 acts as placeholders/spacers for adjacent columns
        
        # Pie Chart
        with fig_col1:
            st.write(dbf.fig1(portfolio_df))

        #Total Asset Performance Indicator
        with fig_col3:
            st.metric(
                label="Total Assets", 
                value = round(current_pf_value, 2),
                delta = str(round(unrealized_pl, 2))
                )

        #Daily Stock Performance Indicator
        with fig_col5:
            st.metric(
                label="TSLA (Daily)", 
                value = round(portfolio_df.at[0,'CURRENT PRICE'], 2),
                delta = round(portfolio_df.at[0,'CURRENT PRICE'] - dbf.prev_close('TSLA'), 2)
            )

            st.metric(
                label="AAPL (Daily)", 
                value = round(portfolio_df.at[1,'CURRENT PRICE'], 2),
                delta = round(portfolio_df.at[1,'CURRENT PRICE'] - dbf.prev_close('AAPL'), 2)
            )
            st.metric(
                label="MSFT (Daily)", 
                value = round(portfolio_df.at[2,'CURRENT PRICE'], 2),
                delta = round(portfolio_df.at[2,'CURRENT PRICE'] - dbf.prev_close('MSFT'), 2)
            )
            st.metric(
                label="AMZN (Daily)", 
                value = round(portfolio_df.at[3,'CURRENT PRICE'], 2),
                delta =round(portfolio_df.at[3,'CURRENT PRICE'] - dbf.prev_close('AMZN'), 2)
            )
            st.metric(
                label="JNJ (Daily)", 
                value = round(portfolio_df.at[4,'CURRENT PRICE'], 2),
                delta = round(portfolio_df.at[4,'CURRENT PRICE'] - dbf.prev_close('JNJ'), 2)
            )

        st.write("")    

        st.dataframe(portfolio_df)

        st.write("### Portfolio Performance")
        st.write(dbf.fig2(dbf.pf_performance(portfolio_df)))
        st.dataframe(dbf.pf_performance(portfolio_df))
      

        time.sleep(5)