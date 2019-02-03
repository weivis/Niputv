from app import app, Flask
from app.index import index
from app.review import review
from app.bangumi import bangumi
from app.account import Account
from flask_login import current_user, login_required, login_user
from app import login_manager

app.config['SERVER_NAME'] = 'niputv.com'
app.register_blueprint(index, subdomain='management')
app.register_blueprint(review, subdomain='management', url_prefix='/review')
app.register_blueprint(bangumi, subdomain='management', url_prefix='/bangumi')

@login_manager.user_loader
def load_user(id):
    return Account.query.get(int(id))