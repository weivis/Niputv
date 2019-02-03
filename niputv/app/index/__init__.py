__author__ = 'Ran'

from flask import Blueprint
index = Blueprint('index', __name__)
from ..index import views