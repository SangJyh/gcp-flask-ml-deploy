from flask import Flask
from flask import jsonify


app = Flask(__name__)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""

    import pandas as pd
    import requests
    import io
    
    #quote historical data
    url = 'https://query1.finance.yahoo.com/v7/finance/download/AAPL?period1=1580232167&period2=1611854567&interval=1d&events=history&includeAdjustedClose=true'

    #url to csv
    r = requests.get(url)
    if r.ok:
        data = r.content.decode('utf8')
        df = pd.read_csv(io.StringIO(data))
    #print('Hi! I am using emacs <br> continue test CI/CD <br> Today is snow day')
    #print()
    return '<h1>AAPL historical stock price</h1>' + df.to_html()

@app.route('/echo/<name>')
def echo(name):
    print(f"This was placed in the url: new-{name}")
    val = {"new-name": name}
    return jsonify(val)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
