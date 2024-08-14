from flask import render_template
from . import create_app

app = create_app()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')