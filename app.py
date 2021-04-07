import os
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from alpha_vantage.timeseries import TimeSeries

st.title('Define stock parameters')
ticker = st.text_input('Ticker (e.g. TSLA):')
month = st.text_input('Month (e.g. 3 or March):')
year = st.text_input('Year (e.g. 2019):')

myKey = os.getenv('ALPHAVANTAGE_API_KEY')

FS = 20
FN = 'times new roman'
font = {'fontname':FN, 'size':FS}
plt.rc('font', **font)
if st.button('Plot'):
    ts = TimeSeries(key=myKey, output_format='pandas')
    data, meta_data = ts.get_daily_adjusted(symbol=ticker, outputsize='full')
    fig, ax = plt.subplots(figsize=(10, 6))
    data['4. close'].loc[year+'-'+month].plot()
    ax.set_ylabel('USD')
    ax.set_xlabel('Date')
    ax.set_title('Closing price in ' + month.capitalize() + '-' + year +' for the ' + ticker.upper() + ' stock')
    st.pyplot(fig)
