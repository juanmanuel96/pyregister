import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'mysecretkey'
    ENV = os.environ.get('ENV')
    MONGO_HOST = os.environ.get('MONGO_HOST') or '127.0.0.1'
    MONGO_PORT = os.environ.get('MONGO_PORT') or '27017'
    COMPANY = 'PyRegister'

class Development(Config):
    DEBUG = True

class Testing(Config):
    DEBUG = False
    TESTING = True

class Production(Config):
    DEBUG = False