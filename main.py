from flask import Flask
from flask import jsonify


app = Flask(__name__)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""

    import pandas as pd
    import requests
    import io
    
    #quote to GOOG historical data
    url = 'https://query1.finance.yahoo.com/v7/finance/download/GOOG'

    #url to csv
    r = requests.get(url)
    if r.ok:
        data = r.content.decode('utf8')
        df = pd.read_csv(io.StringIO(data),nrows=9)
    return df.to_html()
    #return 'Hi! I am using emacs <br> continue test CI/CD <br> Today is snow day'

@app.route('/echo/<name>')
def echo(name):
    print(f"This was placed in the url: new-{name}")
    val = {"new-name": name}
    return jsonify(val)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
