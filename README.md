# InvestorDashboard

An investor dashboard showing current holdings and allocation as well as dedicated research pages to each position owned, a page to compair to an indicies, a page to research any ticker, and a page to trade. 

## Instillation Instructions

    Streamlit --> pip install streamlit
    Plotly --> pip install plotly
    yfinance --> pip install yfinance
    yahoo_fin --> pip install yahoo-fin
    
    In terminal:
    clone repo
    streamlit run Portfolio.py

## Usage

The investor Dashboard uses an excel spreadsheet for initial stock data and can be loaded into '''portfolio_df'''

Once loaded, the live dashboard will show the portfolio's allocation to each asset as well as trading activity, performance, and pages on each stock owned. 

![portfolio_overview1](https://user-images.githubusercontent.com/61864923/211941578-d3437a71-8305-428a-807e-deac90b167ba.png)
![portfolio_overview2](https://user-images.githubusercontent.com/61864923/211941635-2ea18ea1-b3be-4072-bafd-71ecf9e442f2.png)

### Sidebar Navigation
The idea behind the sidebar navigation is that once a portfolio is uploaded, the pages or tabs with individual stock information would be automated to refelct what is owned within the portfolio. By separating information to designated pages we can efficiently organize the information so that users can easily navigate the app to quickly access necessary information. Pages are broken down as from top to bottom as homepage/overview, individual stocks within portfolio, indices, and a stock search page.

*Buy and sell feature is placed on page for viewing purposes, implementation is yet to be complete.*

![sidebar_pages](https://user-images.githubusercontent.com/61864923/211941814-4101c0d1-5068-4522-92f5-098a15365c3c.png)

### Individial Stock Information
Based on the portfolio, pages pertaining to each stock would be automated. Each page will show essential information for users that will available through checkboxes on the sidebar. The purpose of the sidebar checkboxes is to keep the page organized and clean, while preventing an overload of information to users. The additional information are...
- Stock Actions
- Quarterly Financials
- Institutional Shareholders
- Quarterly Balance Sheet
- Quarterly Cashflow
- Quarterly Earnings
- Analysts Recommendation

![tsla_info_page1](https://user-images.githubusercontent.com/61864923/211941863-6e86da91-4d7e-4fbd-9cd7-e07cd34822b3.png)
![tsla_info_page2](https://user-images.githubusercontent.com/61864923/211941867-beda9051-192b-4711-ae99-2755c07099c7.png)

### Indices 
This page allows user to view several indices and to compare user's portfolio performance with other indices.
![indices_page](https://user-images.githubusercontent.com/61864923/211941888-b18ae6a6-cfd8-42fe-a94f-83fc753b9dfc.png)

### Search Feature
The search page will help users to look into any potential stocks that the user has in mind to invest in. The layout of these are exactly the same as the individual stock pages.
![search_stock_page](https://user-images.githubusercontent.com/61864923/211941898-b15c0b89-8dd5-4065-bf69-ef132e07aa1f.png)



## Contributors

* Cuong Ha
* Kenny Pham
* Ryan Svendson
