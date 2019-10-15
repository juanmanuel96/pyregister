from flask import Flask
from flask_login import LoginManager
from source.config import Development
from source.cash_register import cash_register

pos = Flask(__name__)
pos.config.from_object(Development)
login_manager = LoginManager(pos)
login_manager.init_app(pos)
login_manager.login_view = 'login'
login_manager.login_message = "Enter your credentials"
login_manager.session_protection = 'strong'

@login_manager.user_loader
def load_user(uid):
    pass

# Blueprint registration
pos.register_blueprint(cash_register)