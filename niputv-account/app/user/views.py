__author__ = 'Ran'
from app import Flask, cache
from ..user import user
from flask import render_template, request, redirect, url_for, session
from flask_login import current_user

#登陆
@user.route('/', methods=["GET","POST"])
def user():
    return str(current_user.id)