from flask import Flask
from flask import jsonify


app = Flask(__name__)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""

    import pandas as pd
    import requests
    import io
    import pandas_datareader.data as web

    stock = "AAPL"
    end = datetime.date.today()
    start = today + datetime.timedelta(days=-365)
    data = web.DataReader(stock, 'yahoo', start, end)
    return_table = data.to_html()
    return '<h1>AAPL historical stock price</h1>' + return_table

@app.route('/echo/<name>')
def echo(name):
    print(f"This was placed in the url: new-{name}")
    val = {"new-name": name}
    return jsonify(val)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
