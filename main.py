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
    #import pandas_datareader.data as web
    
    url = 'https://query1.finance.yahoo.com/v7/finance/download/AAPL?period1=1580232167&period2=1611854567&interval=1d&events=history&includeAdjustedClose=true'#"https://query1.finance.yahoo.com/v7/finance/download/GOOG"
    
    r = requests.get(url)
    if r.ok:
        df = r.content.decode('utf8')
        data = pd.read_csv(io.StringIO(df))

    stock = "AAPL"
    end = datetime.date.today()
    start = today + datetime.timedelta(days=-365)
    #data = web.DataReader(stock, 'yahoo', start, end)
    #data.to_html()
    #eturn_table = df.to_html()
    return_table = data.to_html()
    return '<h1>AAPL historical stock price</h1>' + return_table

@app.route('/echo/<name>')
def echo(name):
    print(f"This was placed in the url: new-{name}")
    val = {"new-name": name}
    return jsonify(val)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
