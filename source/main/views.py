from ..libraries import render_template, redirect, url_for, current_app, mongo
from . import main

@main.route('/')
def home():
    print(mongo.db)
    return render_template('main/home.html')