import os
from flask import Flask, flash, render_template, redirect, request, url_for

app = Flask(__name__)


## Routes and views
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=os.environ.get('PORT'),
        debug=True)