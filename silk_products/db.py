import os
from pymongo import MongoClient

_client = None
_db = None

def get_db():
    global _client, _db
    if _db is not None:
        return _db
    uri = os.environ.get('MONGODB_URI')
    if not uri:
        raise RuntimeError('MONGODB_URI is not set')
    client = MongoClient(uri, tlsAllowInvalidCertificates=True)
    db_name = os.environ.get('MONGODB_DB')
    if not db_name:
        # Try to parse from URI path
        try:
            db_name = uri.rsplit('/', 1)[-1].split('?')[0]
        except Exception:
            db_name = None
    if not db_name:
        raise RuntimeError('MONGODB_DB is not set and could not be inferred from URI')
    _client = client
    _db = client[db_name]
    return _db

def get_products():
    return get_db()['products']
