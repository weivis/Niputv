__useror__ = 'Ran'

from flask import Blueprint
user = Blueprint('user', __name__, template_folder='../templates', static_folder='../static') #t
from ..user import views