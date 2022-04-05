from configparser import MissingSectionHeaderError
from crypt import methods
from flask import Flask
from flask import render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', pageTitle='Home')

@app.route('/about')
def about():
    return render_template('about.html', pageTitle='About')

@app.route('/estimate', methods=['GET','POST'])
def estimate():
    if request.method == 'POST':
        form = request.form
        radius = float(form['radius'])
        height = float(form['height'])
        pi= 3.14
        tank_top= pi*radius**2
        tank_sides= 2*(pi*(radius*height))
        total_area= tank_top+tank_sides
        area_sqft= total_area/144
        material_cost= area_sqft*25
        labor_cost= area_sqft*15
        total_estimate= "${:,.2f}".format(round(material_cost+labor_cost,2))
        return render_template('estimate.html', estimate= total_estimate)
    return render_template('estimate.html', pageTitle='VTM Estimate')

if __name__ == '__main__':
    app.run(debug=True)
