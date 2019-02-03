from app import app, Flask
from app.auth import auth
from app.user import user
from app.register import register
from app.Database.account import Account

app.config['SERVER_NAME'] = 'niputv.com'
app.register_blueprint(auth, subdomain='account', url_prefix='/sign-in')
app.register_blueprint(register, subdomain='account', url_prefix='/register')
app.register_blueprint(user, subdomain='account', url_prefix='/user')