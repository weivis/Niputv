from app import app, Flask
from app.index import index
from app.upload import upload
from app.works import works
from app.account import Account
from app import login_manager

app.config['SERVER_NAME'] = 'niputv.com'
app.register_blueprint(index, subdomain='creation')
app.register_blueprint(upload, subdomain='creation', url_prefix='/upload')
app.register_blueprint(works, subdomain='creation', url_prefix='/works')

@login_manager.user_loader
def load_user(id):  
    return Account.query.get(int(id))