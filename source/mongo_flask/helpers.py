from werkzeug.local import Local, LocalProxy
from flask import has_request_context, _request_ctx_stack, current_app

current_db = LocalProxy(lambda: _get_db())

def _get_db():
    if has_request_context() and not hasattr(_request_ctx_stack.top, 'db'):
        current_app.mongo_flask._load_db()
    
    return getattr(_request_ctx_stack.top, 'db', None)

def _db_context_processor():
    return dict(current_db=_get_db())
