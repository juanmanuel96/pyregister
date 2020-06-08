from .libraries import Flask, LoginManager, MongoFlask
from source.config import *
from .main import main

pos = Flask(__name__)
pos.config.from_object(Development)
login_manager = LoginManager(pos)
# login_manager.blueprint_login_views = { 'main' : '/login' }
login_manager.login_message = "Enter your credentials"
login_manager.session_protection = 'strong'
mongo = MongoFlask(pos)
mongo.set_Database('pyregister')

@login_manager.user_loader
def load_user(uid):
    pass

@pos.context_processor
def set_jinja_globals():
    return {
        'company' : pos.config['COMPANY']
    }

# Blueprint Registry
pos.register_blueprint(main)