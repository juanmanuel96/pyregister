import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'mysecretkey'
    ENV = os.environ.get('ENV')
    MONGO_HOST = os.environ.get('MONGO_HOST') or '127.0.0.1'
    MONGO_PORT = os.environ.get('MONGO_PORT') or '27017'
    # Register related stuff should go to a register config file, not application 
    # configuration. It should be easy to change regsiter settings, not complicated 
    # by changing app configuration
    # COMPANY = os.environ.get('COMPANY') or 'PyRegister' 
    DEBUG = True if os.environ.get('ENV') == 'development' else False
    TESTING = False if os.environ.get('ENV') != 'testing' else False
    PAYPAL_ID = os.environ.get('PAYPAL_ID') or None
    PAYPAL_SECRET = os.environ.get('PAYPAL_SECRET') or None

# class Development(Config):
#     DEBUG = True

# class Testing(Config):
#     DEBUG = False
#     TESTING = True

# class Production(Config):
#     DEBUG = False