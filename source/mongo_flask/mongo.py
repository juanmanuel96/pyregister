from .wrappers import MongoConnect, MongoDatabase, MongoCollection
from flask import _request_ctx_stack
from .helpers import _db_context_processor

class MongoFlask(object):
    def __init__(self, app = None, db_name = None, add_context_processor = True):
        self.client = None
        self.db = None
        self.collection = None

        if app is not None:
            self.init_app(app, add_context_processor = True)

    def init_app(self, app, db_name = None, add_context_processor = True):
        host = app.config.get('MONGO_HOST', 'localhost')
        port = app.config.get('MONGO_PORT', '27017')
        username = app.config.get('MONGO_USER', None)
        pwd = app.config.get('MONGO_PWD', None)
        if username is None:
            connect = f'mongodb://{host}:{port}'
        else:
            connect = f'mongodb://{username}:{pwd}@{host}:{port}'
        
        self.client = MongoConnect(connect)
        if db_name is not None:
            db_name = str(db_name)
            self.db = self.set_Database(db_name)
        
        app.mongo_flask = self
        if add_context_processor:
            app.context_processor(_db_context_processor)

    def set_Database(self, db_name):
        self.db = MongoDatabase(self.client, db_name)
        return self.db
    
    def set_Collection(self, collection_name):
        self.collection = MongoCollection(self.db, collection_name)
        return self.collection
    
    def _update_request_context_with_db(self, db=None):
        ctx = _request_ctx_stack.top
        ctx.db = None if db is None else self.db

    def _load_db(self):
        return self._update_request_context_with_db(db=self.db)