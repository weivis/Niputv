__registeror__ = 'Ran'

from flask import Blueprint
register = Blueprint('register', __name__, template_folder='../templates', static_folder='../static') #t
from ..register import views