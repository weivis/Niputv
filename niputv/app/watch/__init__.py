__author__ = 'Ran'

from flask import Blueprint
watch = Blueprint('watch', __name__)
from ..watch import views