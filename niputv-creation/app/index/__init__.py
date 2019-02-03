__author__ = 'Ran'

from flask import Blueprint
index = Blueprint('index', __name__, template_folder='../templates', static_folder='../static') #t
from ..index import views