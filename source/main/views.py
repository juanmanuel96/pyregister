from ..libraries import render_template, redirect, url_for, current_app
from . import main

@main.route('/')
def home():
    return render_template('main/home.html')