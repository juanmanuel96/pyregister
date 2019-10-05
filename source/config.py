import os

class Config(object):
    SECRET_KEY = "mysecret"
    DEBUG = True

class Development(Config):
    ENV = 'development'

class Testing(Config):
    DEBUG = False
    TESTING = True
    ENV = "production"

class Production(Config):
    ENV = 'production'
    DEBUG = False