__author__ = 'Ran'

from flask import Blueprint
auth = Blueprint('auth', __name__, template_folder='../templates', static_folder='../static') #t
from ..auth import views