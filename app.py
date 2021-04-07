import os
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from alpha_vantage.timeseries import TimeSeries

FS = 24
FN = 'times new roman'
font = {'family':'serif', 'size':FS}
plt.rc('text', usetex=True)
plt.rc('font', **font)

st.text('This is some text.')

"""
myKey = os.getenv('ALPHAVANTAGE_API_KEY')

ticker = input('ticker: ')
month =  input('month: ')
year = input('year: ')

ts = TimeSeries(key=myKey, output_format='pandas')
data, meta_data = ts.get_daily_adjusted(symbol=ticker, outputsize='full')

plt.figure(figsize=(10, 6))
data['4. close'].loc[year+'-'+month].plot()
plt.title('Closing price in ' + month.capitalize() + '-' + year +' for the ' + ticker.upper() + ' stock')
plt.ylabel('USD')
plt.xlabel('Date')
plt.show()
"""
