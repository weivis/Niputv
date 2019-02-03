from app import Flask, db, cache
from app.account import Account

#@cache.cached(timeout=60*10,key_prefix="middleware-account-%s")
def get_middleware_account(id):
    data = Account.query.filter_by(id=id).first()
    return data