import os
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from alpha_vantage.timeseries import TimeSeries
import numpy as np

FS = 24
FN = 'times new roman'
font = {'family':'serif', 'size':FS}
plt.rc('font', **font)

st.title('Define stock parameters')
ticker = None
ticker = st.text_input('Ticker (e.g. TSLA):')

month = None
month = st.text_input('Month (e.g. 3 or March):')

year = None
year = st.text_input('Year (e.g. 2019):')

myKey = os.getenv('ALPHAVANTAGE_API_KEY')

if (ticker is not None) & (month is not None) & (year is not None):
    st.title(ticker)
    ts = TimeSeries(key=myKey, output_format='pandas')
    #data, meta_data = ts.get_daily_adjusted(symbol=ticker, outputsize='full')
    test = np.linspace(1, 100, 30)
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(test, test*2)
    ax.set_ylabel('USD')
    ax.set_xlabel('Date')
    ax.set_title('test')
    #ax.set_title('Closing price in ' + month.capitalize() + '-' + year +' for the ' + ticker.upper() + ' stock')
    st.pyplot(fig)


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
