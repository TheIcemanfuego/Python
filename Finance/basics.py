# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt
import pandas as pd


# Define the instruments to download. We would like to see Apple, Microsoft
# and the S&P500 index.
#tickers = ['AAPL', 'MSFT', '^GSPC']

# We would like all available data from 01.01.2000 until 31.12.2016.
#start_date = '2010-01-01'
#end_date   = '2016-12-31' 

# User pandas_reader.data.DataReader to load the desired data. As simple as that.
#panel_data = data.DataReader('INPX', 'google', start_date, end_date)

# Getting just the adjusted closing prices. This will return a Pandas DataFrame
# The index in this DataFrame is the major index of the panel_data.
#close = panel_data['Close']


# Getting all weekdays between 01.01.2000 and 31.12.2016
#all_weekdays = pd.date_range(start=start_date, end=end_date, freq='B')

# How do we align the existing proces in adj_close with our new set of dates?
# All we need to do is reindex close using all_weekdays as the new index
#close = close.reindex(all_weekdays)

# Reindexing will insert missing values (NaN) for the dates that were nor present
# in the original set. To cope with this, we can fill the missing by replacing them
# with the latest available price for each instrument.
#close = close.fillna(method='ffill')

#print(all_weekdays)




if __name__ == "__main__":
    start = datetime.datetime(2015, 2, 9)
    end   = datetime.datetime(2017 ,5 ,24)
    
    f = web.DataReader('F', 'morningstar', start, end)
    
    print(str(f.head()))

    