__author__ = 'Ran'

from flask import Blueprint
bangumi = Blueprint('bangumi', __name__)
from ..bangumi import views