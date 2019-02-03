__author__ = 'Ran'

from flask import Blueprint
api = Blueprint('api', __name__)
from ..api import views