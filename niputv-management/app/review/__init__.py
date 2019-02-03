__author__ = 'Ran'

from flask import Blueprint
review = Blueprint('review', __name__, template_folder='../templates', static_folder='../static') #t
from ..review import views