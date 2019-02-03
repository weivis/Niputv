__author__ = 'Ran'
from app import Flask, cache, login_manager
from ..index import index
from app.account import Account
from flask_login import current_user, login_required
from flask import render_template, request, session, redirect

@login_manager.user_loader
def load_user(id):  
    return Account.query.get(int(id))

#首页
@index.route('/')
def home():
    return render_template('index/home.html', headernav_tab='index')