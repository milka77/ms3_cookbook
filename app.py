import os
from flask import Flask, flash, render_template, redirect, request, url_for
import env as config
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)

''' Database (mongoDB) confugirations: '''
app.config["MONGO_DBNAME"] = 'cook_book'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)

''' Routes and viwes '''
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/new_recipe')
def new_recipe():
    return render_template('newrecipe.html',
    categories=mongo.db.categories.find(),
    difficulty=mongo.db.difficulty.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=os.environ.get('PORT'),
        debug=True)