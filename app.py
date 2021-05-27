import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
from flask_paginate import Pagination, get_page_args

app = Flask(__name__)

app.config["SECRET_KEY"] = os.environ.get('SECRET_KEY')

"""
Database (mongoDB) confugirations:
"""
app.config["MONGO_DBNAME"] = 'cook_book'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)


def get_recipes(offset=0, per_page=10):
    """
    Pagination mongoDB query
    """
    recipes = mongo.db.recipes.find()
    return recipes[offset: offset + per_page]


@app.route('/')
@app.route('/index')
def index():
    """
    Routes and views
    index - View of the landing page with 4 rancom recipes from the database
    """
    recipe_numbers = mongo.db.recipes.count()
    _samples = mongo.db.recipes.aggregate([{'$sample': {'size': 4}}])
    return render_template(
                            'index.html',
                            allrecipes=recipe_numbers,
                            samples=_samples
                            )


@app.route('/new_recipe')
def new_recipe():
    """
    View from the newrecipe.html to add new recipes to the database
    """
    return render_template(
                            'newrecipe.html',
                            categories=mongo.db.categories.find().sort(
                                        'category_name', pymongo.ASCENDING),
                            difficulty=mongo.db.difficulty.find()
                            )


@app.route('/file/<filename>')
def file(filename):
    """
    Receiving the picture for the recipe from the database
    """
    return mongo.send_file(filename)


@app.route('/insert_recipe', methods=["GET", "POST"])
def insert_recipe():
    """
    Insert_recipe function to add the recipe into the database
    """
    recipes = mongo.db.recipes
    ingredients = request.form.get('ingredients').splitlines()
    instructions = request.form.get('recipe_instructions').splitlines()
    you_will_need = request.form.get('you_will_need').splitlines()
    recipe_image = request.files['recipe_image']

    if request.method == 'POST':
        mongo.save_file(recipe_image.filename, recipe_image)
        recipes.insert_one({
            "recipe_name": request.form.get('recipe_name'),
            "recipe_info": request.form.get('recipe_info'),
            "cooking_time": request.form.get('cooking_time'),
            "category_name": request.form.get('category_name'),
            "servings_size": request.form.get('servings_size'),
            "recipe_difficulty": request.form.get('recipe_difficulty'),
            "ingredients": ingredients,
            "instructions": instructions,
            "you_will_need": you_will_need,
            "recipe_image_name": recipe_image.filename
        })
    return redirect(url_for('recipes'))


@app.route('/recipes')
def recipes():
    """
    Show all existing recipes from the database
    """
    page, per_page, offset = get_page_args(
                                            page_parameter='page',
                                            per_page_parameter='per_page'
                                            )
    total = mongo.db.recipes.count()
    pagination_recipes = get_recipes(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')

    return render_template(
                            'recipes.html',
                            recipes=pagination_recipes,
                            page=page,
                            per_page=per_page,
                            pagination=pagination
                            )


@app.route('/show_recipe/<recipe_id>')
def show_recipe(recipe_id):
    """
    Detailed page form the selected recipe
    """
    _recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template('showrecipe.html', recipe=_recipe)


@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    """
    Deleting a recipe
    """
    """
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    """
    return redirect(url_for('recipes'))


@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    """
    Editting recipe page
    """
    _recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    _categories = mongo.db.categories.find().sort(
                                                    'category_name',
                                                    pymongo.ASCENDING
                                                    )
    _difficulty = mongo.db.difficulty.find()

    return render_template(
                            'updaterecipe.html',
                            recipe=_recipe,
                            categories=_categories,
                            difficulty=_difficulty
                            )


@app.route('/update_recipe/<recipe_id>', methods=["GET", "POST"])
def update_recipe(recipe_id):
    """
    Updating recipe function
    """
    recipes = mongo.db.recipes
    ingredients = request.form.get('ingredients').splitlines()
    instructions = request.form.get('recipe_instructions').splitlines()
    you_will_need = request.form.get('you_will_need').splitlines()
    recipe_image = request.files['recipe_image']
    if request.method == 'POST':
        mongo.save_file(recipe_image.filename, recipe_image)
        recipes.update(
                        {'_id': ObjectId(recipe_id)},
                        {
                            "recipe_name": request.form.get('recipe_name'),
                            "recipe_info": request.form.get('recipe_info'),
                            "cooking_time": request.form.get('cooking_time'),
                            "category_name": request.form.get('category_name'),
                            "servings_size": request.form.get('servings_size'),
                            "recipe_difficulty": request.form.get(
                                'recipe_difficulty'),
                            "ingredients": ingredients,
                            "instructions": instructions,
                            "you_will_need": you_will_need,
                            "recipe_image_name": recipe_image.filename
                        })
    return redirect(url_for('recipes'))


@app.route('/navbar_search', methods=["GET", "POST"])
def navbar_search():
    """
    Navbar search function
    """
    search_input = request.args.get('navbar_search')
    recipe_found = list(mongo.db.recipes.find(
        {"$text": {"$search": search_input}}))
    return render_template(
                            'result.html',
                            results=recipe_found,
                            search_input=search_input
                            )


@app.route('/contact_us', methods=["GET", "POST"])
def contact_us():
    """
    Contact us page with a form and emailJS script
    """
    return render_template('contactus.html')


@app.route('/our_brand')
def our_brand():
    """
    Our brand information page
    """
    return render_template('ourbrand.html')


@app.route('/add_file', methods=["GET", "POST"])
def add_file():
    """
    File (picture) upload function to MongoDB
    """
    recipe_image = request.files['recipe_image']
    mongo.save_file(recipe_image.filename, recipe_image)
    mongo.db.recipes.insert({
        "recipe_name": request.form.get('recipe_name'),
        "recipe_image_name": recipe_image.filename
    })
    return 'done'


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=False)
