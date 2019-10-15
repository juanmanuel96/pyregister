from flask import Blueprint

cash_register = Blueprint('cash_register', __name__)

from source.cash_register import views