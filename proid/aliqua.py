import pandas as pd
import yfinance as yf

cvc_data = yf.download('CVC', start='2020-01-01', end='2022-12-31')['Adj Close']
cvc_data.columns = ['Close']
cvc_data.index.name = 'Date'
cvc_data.index = pd.to_datetime(cvc_data.index)

cvc_investor_data = pd.read_csv('https://raw.githubusercontent.com/quantopian/catalyst/master/examples/data/cvc_investor_data.csv')
cvc_investor_data['Date'] = pd.to_datetime(cvc_investor_data['Date'])
cvc_investor_data.set_index('Date', inplace=True)
