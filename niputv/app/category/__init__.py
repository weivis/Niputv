__author__ = 'Ran'

from flask import Blueprint
category = Blueprint('category', __name__)
from ..category import views