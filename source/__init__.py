from .libraries import Flask, LoginManager, MongoFlask, register_config
from .config import *
from .main import main
# from .register_config import register_config

pos = Flask(__name__)
pos.config.from_object(Config)

# Login Manager configuration
login_manager = LoginManager(pos)
# login_manager.blueprint_login_views = { 'main' : '/login' }
login_manager.login_message = "Enter your credentials"
login_manager.session_protection = 'strong'

@login_manager.user_loader
def load_user(uid):
    pass

# MongoDB configuration
mongo = MongoFlask(pos)
mongo.set_Database('pyregister')

# This context processor will be used to add global variables that
# can be used in jinja templating
@pos.context_processor
def set_jinja_globals():
    return {
        'company' : register_config.json_data.get('compnay', 'PyRegister')
    }

# Blueprint Registry
pos.register_blueprint(main)