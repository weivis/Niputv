from app import app, login_manager
from app.index import index
from app.watch import watch
from app.user import user
from app.category import category
from app.api import api
from app.bangumi import bangumi

from app.account import Account

app.config['SERVER_NAME'] = 'niputv.com'

app.register_blueprint(index, subdomain='www', )
app.register_blueprint(watch, subdomain='www', url_prefix='/watch')
app.register_blueprint(user, subdomain='www', url_prefix='/user')
app.register_blueprint(bangumi, subdomain='www', url_prefix='/bangumi')
app.register_blueprint(category, subdomain='www', url_prefix='/category')
app.register_blueprint(api, subdomain='www', url_prefix='/api')

@login_manager.user_loader
def load_user(id):
    return Account.query.get(int(id))