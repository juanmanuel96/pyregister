from source.cash_register import cash_register
from flask import render_template, redirect, url_for

@cash_register.route('/')
def index():
    pass