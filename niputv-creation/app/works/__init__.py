__author__ = 'Ran'

from flask import Blueprint
works = Blueprint('works', __name__, template_folder='../templates', static_folder='../static') #t
from ..works import views