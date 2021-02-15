import numpy as np
import pandas as pd
from pandas_datareader import data as data
import matplotlib.pyplot as plt 


tickers=['XLF']
stocks=[]
for n in range(5):
    tickers.append(input(f"Enter stock ticker ({n+1} of 5): ").upper())
start_date = '2020-01-01'
end_date = '2020-12-31'
for ticker in tickers:
    stocks.append({'ticker': ticker})

def get_plot(stocks):
    df = pd.DataFrame()
    for stock in stocks:
        df[stock['ticker']] = data.DataReader(stock['ticker'], data_source='yahoo', start= start_date, end=end_date)['Adj Close']
    multiplier = 100
    returns = df.apply(lambda x: (x/x[0]*multiplier))
    plt.style.use('dark_background')
    for stock in stocks:
        plt.plot(returns[stock['ticker']], label=stock['ticker'])
    plt.legend()
    plt.xlabel('Date')
    plt.ylabel('Value (USD)')
    plt.title('Historical Growth')
    plt.show()

get_plot(stocks)



