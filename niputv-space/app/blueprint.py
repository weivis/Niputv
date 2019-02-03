from app import app, Flask
from app.index import index
from app import login_manager
from app.account import Account

@login_manager.user_loader
def load_user(id):  
    return Account.query.get(int(id))

app.config['SERVER_NAME'] = 'niputv.com'
app.register_blueprint(index, subdomain='space')