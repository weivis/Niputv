__author__ = 'Ran'

from flask import Blueprint
bangumi = Blueprint('bangumi', __name__, template_folder='../templates', static_folder='../static') #t
from ..bangumi import views