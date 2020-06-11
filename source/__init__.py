from .libraries import Flask, LoginManager, MongoFlask, register_config
from .config import *
from .main import main
from .staff import Staff

pos = Flask(__name__)
pos.config.from_object(Config)

# Login Manager configuration
login_manager = LoginManager(pos)
# login_manager.blueprint_login_views = { 'main' : '/login' }
login_manager.login_message = "Enter your credentials"
login_manager.session_protection = 'strong'

@login_manager.user_loader
def load_user(uid):
    _user = Staff.get_user(uid)
    if _user is None:
        return None
    else:
        return Staff(
            eid= _user['eid'],
            username= _user['username'],
            first_name= _user['first_name'],
            last_name= _user['last_name'],
            account_type= _user['account_type'],
            is_approved= _user['is_approved']
        )

# MongoDB configuration
mongo = MongoFlask(pos)
mongo.set_Database('pyregister')

# This context processor will be used to add global variables that
# can be used in jinja templating
@pos.context_processor
def set_jinja_globals():
    return {
        'company_brand' : register_config.json_data.get('compnayBrand', 'PyRegister')
    }

# Blueprint Registry
pos.register_blueprint(main)