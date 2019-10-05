from flask import Flask
from flask_login import LoginManager
from source.config import Development

pos = Flask(__name__)
pos.config.from_object(Development)
login_manager = LoginManager(pos)
login_manager.init_app(pos)
login_manager.login_view = 'login'
login_manager.login_message = "Enter your credentials"
login_manager.session_protection = 'strong'

# from source import routes