__author__ = 'Ran'

from flask import Blueprint
upload = Blueprint('upload', __name__, template_folder='../templates', static_folder='../static') #t
from ..upload import views