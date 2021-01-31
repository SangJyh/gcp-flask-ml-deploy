from flask import Flask
from flask import jsonify


app = Flask(__name__)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""

    import pandas as pd
    import requests
    import io
    import datetime
    import pandas_datareader.data as pdr
    #stock name
    stock = "AAPL"
    
    #set up the start and end time point I want
    end = datetime.date.today()
    start = end + datetime.timedelta(days=-365)
    
    #using data_reader to retrieve stock data from yahoo finance
    data = pdr.DataReader(stock, 'yahoo', start, end)
    
    #data preprocessing
    data = data.round(3)
    data["Volume"] = data.apply(lambda x: "{:,.0f}".format(x["Volume"]), axis=1)
    data = data.reset_index()
    
    #return the table into html format and modify the look
    return_table = data.to_html(table_id=stock, justify="center")
    return_table = return_table[:6] + " align = 'center'" + return_table[6:]
    
    # add header
    title = '<h1 align="center">{0} historical stock price (from {1} to {2})</h1>'.format(stock, start, end)

    return title + return_table

#@app.route('/echo/<name>')
#def echo(name):
#    print(f"This was placed in the url: new-{name}")
#    val = {"new-name": name}
#    return jsonify(val)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
