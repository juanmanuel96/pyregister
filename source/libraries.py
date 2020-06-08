from flask import Flask, render_template, redirect, abort, current_app, url_for, Blueprint
from flask_login import LoginManager, login_required, current_user, UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from .mongo_flask import MongoFlask