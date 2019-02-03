__author__ = 'Ran'
from app import Flask, cache, login_manager
from ..index import index
from app.account import Account
from flask_login import current_user, login_required
from flask import render_template, request, session, redirect

#首页
@index.route('/')
@login_required
def home():
    return render_template('creation/index.html')