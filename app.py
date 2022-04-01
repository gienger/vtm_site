from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', pageTitle='Home')

@app.route('/about')
def about():
    return render_template('about.html', pageTitle='About')

@app.route('/estimate')
def estimate():
    return render_template('estimate.html', pageTitle='Estimate')

if __name__ == '__main__':
    app.run(debug=True)
