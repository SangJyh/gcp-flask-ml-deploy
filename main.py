from flask import Flask
from flask import jsonify
import pandas as pd
import requests
import io
import datetime
import pandas_datareader.data as pdr

import tensorflow as tf
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout
from keras.layers import Masking
from keras.optimizers import Adam
from keras.layers import Flatten

#ml function


app = Flask(__name__)
@app.route('/')
def hello():
    """Return a table of AAPL stock price features"""

    #stock name
    stock = "AAPL"
    
    #set up the start and end time point I want
    end = datetime.date.today()
    start = end + datetime.timedelta(days=-365)
    
    #using data_reader to retrieve stock data from yahoo finance
    data = pdr.DataReader(stock, 'yahoo', start, end)
    
    #data preprocessing
    data = data.round(3)
    #make model based on the original data
    #tomorrow = lstm(data)

    #change data type and index of the datafram for better visualization
    data["Volume"] = data.apply(lambda x: "{:,.0f}".format(x["Volume"]), axis=1)
    data = data.reset_index()
    
    #return the table into html format and modify the look
    return_table = data.to_html(table_id=stock, justify="center")
    return_table = return_table[:6] + " align = 'center'" + return_table[6:]
    
    #if tomorrow > data["Close"].iloc[-1]:
    #    future = '<h2 align="center">{0} Bull</h2>'
    #elif tomorrow < data["Close"].iloc[-1]:
    #    future = '<h2 align="center">{0} Bear</h2>'
    #else tomorrow == data["Close"].iloc[-1]:
    #    future = '<h2 align="center">{0} Same</h2>'
    
    # add header
    title = '<h1 align="center">{0} historical stock price (from {1} to {2})</h1>'.format(stock, start, end)
    import sys
    subtitle = '<h3 align="center"> Python rt = {0}, tf = {1} </h3>'.format(sys.version, tf.__version__)
    return title + subtitle + return_table#  + future

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
